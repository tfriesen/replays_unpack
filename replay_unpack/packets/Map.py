#!/usr/bin/python
# coding=utf-8
import struct

from replay_unpack.base.decorators import bigworld_packet
from replay_unpack.base.packets.PacketData import PacketDataBase
from replay_unpack.base.packets.types.Matrix4 import Matrix4

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=0x27)
class Map(PacketDataBase):
    def __init__(self, stream):
        self.spaceId, = struct.unpack('i', stream.read(4))
        self.arenaId, = struct.unpack('q', stream.read(8))
        # something new added in 0.7.9, just skip it
        _name_size, = struct.unpack('i', stream.read(4))
        if stream.pos + _name_size + 16 * 4 != stream.len - 1:
            stream.read(16 * 8 + 4)
            _name_size, = struct.unpack('i', stream.read(4))
        self.name = stream.read(_name_size)
