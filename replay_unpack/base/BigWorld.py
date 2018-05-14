#!/usr/bin/python
# coding=utf-8
from build.entities.plugins.BattleController import BattleController

__author__ = "Aleksandr Shyshatsky"


class BigWorld(object):
    def __init__(self):
        self.entities = {}
        self.battle_controller = BattleController(self)

    @property
    def battleLogic(self):
        return next(e for e in self.entities.itervalues() if e.__class__.__name__ == 'BattleLogic')
