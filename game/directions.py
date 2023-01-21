from enum import Enum
import pygame as py


class Direction(Enum):
    UP = py.math.Vector2(0, -1)
    DOWN = py.math.Vector2(0, 1)
    LEFT = py.math.Vector2(-1, 0)
    RIGHT = py.math.Vector2(1, 0)
    NONE = py.math.Vector2(0, 0)