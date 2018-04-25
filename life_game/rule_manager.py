from .blocks import *
from . import settings


class RuleManager(object):
    def __init__(self):
        self.inits = [eval(x)() for x in settings.ADDS]


    def get_type(self, game, i, j):
        if i < 0 or i >= game.height:
            return settings.EmptyBlock
        if j < 0 or j >= game.width:
            return settings.EmptyBlock
        
        return game.desk[i][j].name


    def generate(self, game, i, j):        
        if game.desk[i][j].type_id == settings.ALIVE:
            for rule in game.desk[i][j].rule:
                cnt = 0
                for pos in rule[settings.POSITIONS]:
                    if self.get_type(game, i + pos[settings.ROW_COORDINATE],
                                     j + pos[settings.COLUMN_COORDINATE]) == rule[settings.TYPE]:
                        cnt += 1
                if cnt < rule[settings.MIN_VALUE] or cnt > rule[settings.MAX_VALUE]:
                    return self.inits[settings.EmptyBlock]
            return game.desk[i][j]
        else:
            for rule in game.desk[i][j].rule:
                cnt = 0
                for pos in rule[settings.POSITIONS]:
                    if self.get_type(game, i + pos[settings.ROW_COORDINATE],
                                     j + pos[settings.COLUMN_COORDINATE]) == rule[settings.TYPE]:
                        cnt += 1
                if cnt >= rule[settings.MIN_VALUE] and cnt <= rule[settings.MAX_VALUE]:
                    return self.inits[rule[settings.TYPE]]
            return game.desk[i][j]
