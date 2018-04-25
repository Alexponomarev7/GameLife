import sys


from . import rule_manager
from . import settings


class Game:
    NONE = "The game is empty now."
    LOADED = "The game is loaded, %s moves have passed."


    def __init__(self):
        self.status = Game.NONE
        self.cnt_moves = 0
        
        self.manager = rule_manager.RuleManager()


    def upload(self, file=None):
        f_r = sys.stdin

        if not file is None:
            f_r = open(file, "r")

        self.height, self.width, self.generations = map(int, f_r.readline().split())
        self.desk = []
        for _ in range(self.height):
            row = [None] * self.width

            row_str = f_r.readline()
            for j in range(self.width):
                row[j] = self.manager.inits[settings.UPLOADED_BLOCKS[row_str[j]]]
            self.desk.append(row)
        self.status = Game.LOADED
        self.cnt_moves = 0
        if not file is None:
            f_r.close()


    def download(self, file=None):
        f_w = sys.stdout

        if not file is None: 
            f_w = open(file, "w")

        for i in range(self.height):
            for j in range(self.width):
                print(settings.UPLOADED_BLOCKS_REV[self.desk[i][j].name], end="", file=f_w)
            print(file=f_w)


    def info(self):
        if self.status == Game.LOADED:
            print(self.status % self.cnt_moves)
        else:
            print(self.status)


    def next_iteration(self):
        new_condition = [[None] * self.width for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                new_condition[i][j] = self.manager.generate(self, i, j)
        self.desk = new_condition


    def make_generation(self, count=1):
        for i in range(count):
            self.next_iteration()
