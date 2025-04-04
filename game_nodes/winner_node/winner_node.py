from tkinter import Canvas
from game_nodes.game_node import GameNode
import game_nodes.menu_node.menu_node as mn
from utils.constants import Const
import tkinter as tk

class WinnerNode(GameNode):
    def __init__(self, parent, root: tk.Tk, winner: int) -> None:
        super().__init__(parent, root)
        self._winner = winner
        self._objects: list[tk.Widget] = []

        text = tk.Text(root, width = 40, height = 1, wrap = "none")
        color = "blancs" if self._winner == Const.PLAYER_ONE else "noirs"
        text.insert(1.0, f"Les {color} ont gagnés !")
        text.place(relx=0.0, rely=0.1, relwidth=1)
        self._objects.append(text)

        button = tk.Button(parent._root, text="Retour au Menu", command=self._go_to_menu)
        button.place(relx=0.0, rely=0.2, relwidth=1)
        self._objects.append(button)

    def update(self, delta: float) -> None:
        for node in self._nodes:
            node.update(delta)

    def draw(self, canvas: Canvas) -> None:
        super().draw(canvas)

    def _go_to_menu(self):
        self.clear_objects()
        self.clear_nodes()
        self._parent.clear_nodes()
        self._parent.add_node(mn.MenuNode(self._parent, self._root))
    
    def clear_objects(self) -> None:
        for o in self._objects:
            o.destroy()