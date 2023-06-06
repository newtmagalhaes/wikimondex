from enum import Enum


class Poketipo(Enum):
    NORMAL = 'normal'
    GRASS = 'grass'
    WATER = 'water'
    FIRE = 'fire'
    ELETRIC = 'eletric'

    def __str__(self) -> str:
        return self.value
