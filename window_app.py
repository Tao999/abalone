import tkinter as tk
import time

from game_nodes.game_node import GameNode
import game_nodes.menu_node.menu_node as mn
from utils.constants import Const, VisuConst
from utils.singletons import mouse
from utils.vec import vec2


class WindowApp(GameNode):
    def __init__(self, width: int, height: int) -> None:
        self._root = tk.Tk()
        self._root.resizable(False, False)
        self._canvas = tk.Canvas(
            self._root, width=width, height=height, bg=VisuConst.BACKGROUND_COLOR)
        self._canvas.pack()
        self._frame_delay = 1.0 / 120.0
        self._last_time = time.time()

        self._nodes: list[GameNode] = []

    def _mouse_motion_callback(self, e: tk.Event) -> None:
        mouse.set_position(vec2(e.x, e.y))

    def _mouse_pressed_callback(self, e: tk.Event) -> None:
        if e.num == 1:
            mouse.press_button(mouse.LEFT_BUTTON)
        elif e.num == 3:
            mouse.press_button(mouse.RIGHT_BUTTON)

    def _mouse_release_callback(self, e: tk.Event) -> None:
        if e.num == 1:
            mouse.unpress_button(mouse.LEFT_BUTTON)
        elif e.num == 3:
            mouse.unpress_button(mouse.RIGHT_BUTTON)

    def run(self) -> None:
        self._root.bind('<Motion>', self._mouse_motion_callback)
        self._root.bind('<ButtonPress>', self._mouse_pressed_callback)
        self._root.bind('<ButtonRelease>', self._mouse_release_callback)
        self._nodes.append(mn.MenuNode(self, self._root))
        self.update(0)
        self._root.mainloop()

    def update(self, _) -> None:
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
        self._root.after(max(1, delay), self.update, 0)


if __name__ == "__main__":
    app_width = VisuConst.PADDING*2+VisuConst.BALL_SIZE*(Const.GRID_SIZE+1)
    app_height = app_width + 100
    app = WindowApp(app_width, app_height)
    app.run()
