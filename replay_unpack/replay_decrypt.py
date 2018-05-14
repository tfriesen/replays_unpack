#!/usr/bin/python
# coding=utf-8
import json
import os
import struct
from cStringIO import StringIO

import zlib
from contextlib import contextmanager

from Crypto.Cipher import Blowfish
from tqdm import tqdm

BASE_DIR = os.path.dirname(__file__)
BLOWFISH_KEY = ''.join(['\xDE', '\x72', '\xBE', '\xA0', '\xDE', '\x04', '\xBE', '\xB1',
                        '\xDE', '\xFE', '\xBE', '\xEF', '\xDE', '\xAD', '\xBE', '\xEF'])




class WoWSReplayDecrypt(object):
    """
    # Header
    Every replay starts off with an 8 byte header, consisting of the following values:
    
    magic number - An unsigned 32 bit integer (4 bytes)
    block count - An unsigned 32 bit integer (4 bytes)
    The block count is an indication of how many data blocks (excluding the real replay data) are stored inside the replay. For replays generated by a World of Tanks version before 0.8.1, the presence of 2 blocks means the replay is considered "complete", meaning it has the match start information, as well as a match result. Replays generated by 0.8.1 and later versions are guaranteed to be complete if there are 2 or more blocks present.
    
    # Blocks
    Every data block starts with an unsigned 32 bit integer that holds the length of the data for the given block. The first block consists of a JSON encoded structure. In versions before 0.8.1, the second block is also a JSON encoded structure.
  
    # Reading
    Open the replay file
    Seek to offset 4 in the replay file (skipping the magic number)
    Read 4 bytes, and interpret these as an unsigned 32 bit integer, let this be "block count"
    For every block take the following action:
    Read 4 bytes, and interpret these as an unsigned 32 bit integer, let this be "data length"
    Read "data length" bytes
    Once all blocks have been read, the remainder of the data in the file is the compressed and encrypted replay data
    
    See http://wiki.vbaddict.net/pages/File_Replays for more details;
    """
    def __init__(self, replay_path, show_progress=False, dump_binary=False):
        self.__dump_binary_data = dump_binary
        self.__show_progress = show_progress
        self.__replay_path = replay_path
        self.__check_replay_exists()

    def get_replay_data(self):
        """
        Get open info about replay 
        (stored as Json at the beginning of file) 
        and closed one
        (after decrypt & decompress);
        :rtype: tuple[dict, str]
        """
        with open(self.__replay_path, 'rb') as f:
            f.seek(4)  # skip signature
            blocks_count = struct.unpack("i", f.read(4))[0]

            # # TODO: replay can contain up to 3 blocks
            # if blocks_count != 1:
            #     raise Exception("Not implemented replay data structure. "
            #                     "Expected blocks == 1, blocks == {0}".format(blocks_count))

            for _ in range(blocks_count):
                block_size = struct.unpack("i", f.read(4))[0]
                arena_info = json.loads(f.read(block_size))

            decrypted_data = zlib.decompress(self.__decrypt_data(f.read()))

            if self.__dump_binary_data:
                self.__save_decrypted_data(decrypted_data)

            return [], decrypted_data

    def __save_decrypted_data(self, decrypted_data):
        """
        Save decrypted data into file named as 
        given replay, but with '.hex' postfix;
        :type decrypted_data: str 
        :raises ParserException
        """
        try:
            replay_name = os.path.basename(self.__replay_path)
            with open('{}.hex'.format(replay_name), 'wb') as df:
                df.write(decrypted_data)
        except IOError, e:
            print 'Cannot dump replay: {}'.format(e)

    def __check_replay_exists(self):
        """
        Check if replay really exists. 
        Raises ParserException otherwise. 
        """
        if not os.path.exists(self.__replay_path):
            raise Exception("File does not exists: {}".format(self.__replay_path))

    @staticmethod
    def __chunkify_string(string, length=8):
        """
        Split string into blocks with given max len.
        :type string: str
        :type length: int|long
        :rtype: tuple[int, str]
        """
        for i in xrange(0, len(string), length):
            yield i, string[0 + i:length + i]

    @contextmanager
    def __progressbar(self, total_count):
        """
        Wrapper for tqdm written as context manager;
        Usage: 
        with self.__progressbar(len(x)) as pb:
          pb.update(y)
        :type total_count: int 
        """
        bar = tqdm(total=total_count, disable=not self.__show_progress)
        yield bar
        bar.close()

    def __decrypt_data(self, dirty_data):
        previous_block = None  # type: str
        blowfish = Blowfish.new(BLOWFISH_KEY)
        decrypted_data = StringIO()

        with self.__progressbar(len(dirty_data)) as pb:
            for index, chunk in self.__chunkify_string(dirty_data):
                # FIXME: what this chunk is used for??
                if index == 0:
                    continue

                decrypted_block = blowfish.decrypt(chunk)
                if previous_block:
                    decrypted_block = ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(decrypted_block, previous_block)])
                decrypted_data.write(decrypted_block)
                previous_block = decrypted_block

                pb.update(8)

        return decrypted_data.getvalue()
