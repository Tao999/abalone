import tkinter as tk
import time

from game_nodes.abalone_node.abalone_node import AbaloneNode
from game_nodes.game_node import GameNode
from utils.constants import Const, VisuConst


class App:
    def __init__(self, width: int, height: int) -> None:
        self._root = tk.Tk()
        self._root.title("Tkinter Canvas Loop")
        self._root.resizable(False, False)
        self._canvas = tk.Canvas(
            self._root, width=width, height=height, bg=VisuConst.BACKGROUND_COLOR)
        self._canvas.pack()
        self._frame_delay = 1.0 / 120.0
        self._last_time = time.time()

        self._nodes: list[GameNode] = []

    def run(self) -> None:
        self._nodes.append(AbaloneNode())
        self.update()
        self._root.mainloop()

    def update(self) -> None:
        current_time = time.time()
        delta_time = current_time - self._last_time
        self._last_time = current_time
        self._root.title(f"FPS {int(1/delta_time):03}")

        for node in self._nodes:
            node.update(delta_time)

        self._canvas.delete('all')
        for node in self._nodes:
            node.draw(self._canvas)

        elapsed_time = time.time() - current_time
        delay = int((self._frame_delay - elapsed_time) * 1000)
        self._root.after(max(1, delay), self.update)


if __name__ == "__main__":
    app_width = VisuConst.PADDING*2+VisuConst.BALL_SIZE*(Const.GRID_SIZE+1)
    app_height = app_width + 100
    app = App(app_width, app_height)
    app.run()
