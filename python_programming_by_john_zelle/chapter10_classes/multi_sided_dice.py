import random


class MSDie:
    def __init__(self, sides):
        self._sides = sides
        self._value = 1

    @property
    def sides(self):
        return self._sides

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, number):
        self._value = number

    def roll(self):
        self.value = random.randrange(1, self.sides + 1)


d1 = MSDie(6)
print(d1.value)
d1.roll()
print(d1.value)
