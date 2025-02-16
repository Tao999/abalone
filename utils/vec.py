from dataclasses import dataclass


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
