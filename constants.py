
from enum import Enum


class Constant:
    NO_PLAYER = 0
    PLAYER_ONE = 1
    PLAYER_TWO = 2
    
    GRID_SIZE = 9

class Dir(Enum):
    LEFT = 0
    UP_LEFT = 1
    UP_RIGHT = 2
    RIGHT = 3
    DOWN_RIGH = 4
    DOWN_LEFT = 5
