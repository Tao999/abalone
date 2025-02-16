import tkinter as tk
import time

from game_nodes.game_node import GameNode

class App:
    def __init__(self, width: int, height: int):
        self._root = tk.Tk()
        self._root.title("Tkinter Canvas Loop")
        self._root.resizable(False, False)
        self._canvas = tk.Canvas(self._root, width=width, height=height, bg="white")
        self._canvas.pack()
        self._frame_delay = 1.0 / 120.0
        self._last_time = time.time()

        self._nodes: list[GameNode] = []


    def run(self):
        self.update()
        self._root.mainloop()

    def update(self):
        current_time = time.time()
        delta_time = current_time - self._last_time
        self._last_time = current_time
        self._root.title(f"FPS {int(1/delta_time)}")

        for node in self._nodes:
            node.update(delta_time)
        
        for node in self._nodes:
            node.draw(self._canvas)

        elapsed_time = time.time() - current_time
        delay = int((self._frame_delay - elapsed_time) * 1000)
        self._root.after(max(1, delay), self.update, delta_time)
    

if __name__ == "__main__":
    app = App(800, 800)
    app.run()
