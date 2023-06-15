from enum import Enum


class Poketipo(Enum):
    NORMAL = 'normal'
    GRASS = 'grass'
    WATER = 'water'
    FIRE = 'fire'
    ELETRIC = 'eletric'
    POISON = 'poison'
    FLYING = 'flying'

    def __str__(self) -> str:
        return self.value
