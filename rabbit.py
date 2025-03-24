from animal import Animal


class Rabbit(Animal):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)