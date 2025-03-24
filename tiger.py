from animal import Animal
from enum import Enum, auto

from field import Field


class TigerState(Enum):
    TRACK = auto()
    ATTACK = auto()
    HOME = auto()



class Tiger(Animal):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.state = TigerState.TRACK

    def turn(self, field: Field):
        if self.state == TigerState.TRACK:
            self.track(field)
        elif self.state == TigerState.ATTACK:
            self.attack(field)
        elif self.state == TigerState.HOME:
            self.home(field)

    def track(self, field: Field):
        pass

    def attack(self, field: Field):
        pass

    def home(self, field: Field):
        pass
