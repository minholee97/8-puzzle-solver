import random
import math

class Board:
    def __init__(self, value=None):
        self.state = [1, 2, 3, 4, 5, 6, 7, 8, ""] if value is None else value.state[:]
        self.x = 0 if value is None else value.x
        self.y = 0 if value is None else value.y
        self.moveCount = 0 if value is None else value.moveCount
        self.mDistance = 0 if value is None else value.mDistance
        self.properLoc = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)]
        self.heuristic = 0 if value is None else value.heuristic
        self.path = [] if value is None else value.path[:]
        self.st = 0 if value is None else value.st

    def set(self):
        while True:
            random.shuffle(self.state)
            dis = 0
            for i in range(9):
                if self.state[i] == "":
                    self.x = i // 3
                    self.y = i % 3
                    continue
                for j in range(i + 1, 9, 1):
                    if i == 9:
                        print("WARNING!")
                    if self.state[j] == "":
                        continue
                    if self.state[i] > self.state[j]:
                        dis += 1
            if dis % 2 == 0:
                break

    def check(self):
        self.mDistance = 0
        for i in range(9):
            if self.state[i] == "":
                continue
            if self.state[i] != i + 1:
                self.mDistance += abs(self.properLoc[self.state[i] - 1][0] - (i // 3)) + abs(
                    self.properLoc[self.state[i] - 1][1] - (i % 3))
        self.heuristic = self.mDistance + self.moveCount


class Storage:
    def __init__(self):
        self.list = []
        self.index = 0

    def push(self, new):
        self.list.append(new)
        self.list.sort(key=lambda object: object.heuristic, reverse=True)
