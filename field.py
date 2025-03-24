import constants
import random

from rabbit import Rabbit


class Field:
    def __init__(self, width: int, height: int, rabbit_quantity: int, tiger_quantity: int):
        self.width = width
        self.height = height
        self.rabbit_quantity = rabbit_quantity
        self.rabbits = {}
        self.tiger_quantity = tiger_quantity
        self.matrix = []

        for i in range(self.height):
            line = []
            for j in range(self.width):
                line.append(constants.EMPTY)
            self.matrix.append(line)

    def display(self):
        for i in range(self.height):
            print()
            for j in range(self.width):
                print(self.matrix[i][j], end=" ")

    def place_rabbits_randomly(self):
        for i in range(self.rabbit_quantity):
            while True:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if not self.matrix[y][x] == constants.EMPTY:
                    continue
                self.matrix[y][x] = constants.RABBIT
                self.rabbits[i] = Rabbit(x, y)