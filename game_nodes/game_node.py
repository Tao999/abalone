from abc import ABC
from tkinter import Canvas

class GameNode(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._nodes: list[GameNode] = []

    def update(self, delta: float) -> None:
        for node in self._nodes:
            node.update(delta)
    
    def draw(self, canvas: Canvas) -> None:
        for node in self._nodes:
            node.draw(canvas)