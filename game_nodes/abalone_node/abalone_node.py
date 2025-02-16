from tkinter import Canvas
from game_nodes.abalone_node.abalone import Abalone
from game_nodes.game_node import GameNode
from utils.constants import Const, VisuConst
from utils.vec import vec2


class AbaloneNode(GameNode):
    def __init__(self) -> None:
        super().__init__()
        self._abalone = Abalone()

    def update(self, delta: float) -> None:
        super().update(delta)
        # TODO

    def draw(self, canvas: Canvas) -> None:
        super().draw(canvas)

        for y in range(Const.GRID_SIZE):
            for x in range(Const.GRID_SIZE):
                ball = self._abalone.get_ball_at(vec2(x, y))
                if ball >= 0:
                    offset = 0
                    if y % 2:
                        offset = VisuConst.BALL_SIZE//2
                    ball_origin = vec2(self._ball_transform(
                        x) + offset, self._ball_transform(y))
                    ball_end = vec2(ball_origin.x + VisuConst.BALL_SIZE,
                                    ball_origin.y + VisuConst.BALL_SIZE)
                    color = VisuConst.PLAYER_COLOR[ball]
                    canvas.create_oval(ball_origin.x, ball_origin.y, ball_end.x, ball_end.y,
                                       fill=color, width=VisuConst.DRAW_WIDTH, outline="green")

    def _ball_transform(self, i: int) -> int:
        return VisuConst.PADDING+i*VisuConst.BALL_SIZE + i*VisuConst.BALL_SPACE
