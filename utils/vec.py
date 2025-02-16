from cmath import sqrt
from dataclasses import dataclass
from math import atan2


@dataclass
class vec2():
    x: int
    y: int

    def __add__(self, b):
        return vec2(self.x+b.x, self.y+b.y)

    def __mul__(self, b):
        return vec2(int(self.x*b), int(self.y*b))

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __eq__(self, b):
        if not self:
            return False
        if not b:
            return False
        return self.x == b.x and self.y == b.y
    
    def distance(self, b) -> float:
        A = self.x - b.x
        B = self.y - b.y
        result = sqrt(A*A + B*B)
        return result.real

    def get_radian_angle(self, b) -> float:
        angle = atan2(b.y-self.y, b.x-self.x)
        return angle
    
    def get_degree_angle(self, b) -> int:
        angle = self.get_radian_angle(b)
        return int(angle * 180 / 3.141592)
