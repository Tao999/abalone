from abc import ABC
from tkinter import Canvas
import tkinter as tk

class GameNode(ABC):
    def __init__(self, parent: "GameNode", root: tk.Tk) -> None:
        super().__init__()
        self._root: tk.Tk = root
        self._nodes: list[GameNode] = []
        self._parent: GameNode = parent

    def update(self, delta: float) -> None:
        for node in self._nodes:
            node.update(delta)

    def draw(self, canvas: Canvas) -> None:
        for node in self._nodes:
            node.draw(canvas)
    
    def clear_nodes(self) -> None:
        self._nodes = []
    
    def add_node(self, node: "GameNode") -> None:
        self._nodes.append(node)
