import tkinter as tk
from tkinter import Canvas
from game_nodes.abalone_node.abalone_node import AbaloneNode
from game_nodes.game_node import GameNode

class MenuNode(GameNode):
    def __init__(self, parent, root: tk.Tk) -> None:
        super().__init__(parent, root)
        self._nodes: list[GameNode] = []
        self._objects: list[tk.Widget] = []

        button = tk.Button(parent._root, text="Jouer", command=self._go_to_game)
        button.place(relx=0.0, rely=0.1, relwidth=1)
        self._objects.append(button)
        button = tk.Button(parent._root, text="Quitter", command=self._exit_game)
        button.place(relx=0.0, rely=0.2, relwidth=1)
        self._objects.append(button)
        

    def update(self, delta: float) -> None:
        for node in self._nodes:
            node.update(delta)

    def draw(self, canvas: Canvas) -> None:
        for node in self._nodes:
            node.draw(canvas)
    
    def _go_to_game(self):
        self.clear_objects()
        self.clear_nodes()
        game = AbaloneNode(self._parent, self._root)
        self._parent.clear_nodes()
        self._parent.add_node(game)
    
    def _exit_game(self):
        self._root.destroy()
    
    def clear_objects(self) -> None:
        for o in self._objects:
            o.destroy()
