from tkinter import Canvas
from typing import Optional
from game_nodes.abalone_node.abalone import Abalone
from game_nodes.game_node import GameNode
from utils.constants import Const, VisuConst
from utils.vec import vec2
from utils.singletons import mouse

FULL_BALL_SIZE = VisuConst.BALL_SIZE + VisuConst.BALL_SPACE
HALF_BALL_SIZE = VisuConst.BALL_SIZE//2


class AbaloneNode(GameNode):
    def __init__(self) -> None:
        super().__init__()
        self._abalone = Abalone()

    def update(self, delta: float) -> None:
        super().update(delta)

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
                    mouse_position_in_board = self._world_grid_to_abalone_coord(mouse.get_position())
                    outline_color = VisuConst.NOT_HOVERED_BALL
                    if mouse_position_in_board == vec2(x, y):
                        outline_color = VisuConst.HOVERED_BALL
                    canvas.create_oval(ball_origin.x, ball_origin.y, ball_end.x, ball_end.y,
                                       fill=color, width=VisuConst.DRAW_WIDTH, outline=outline_color)

    def _ball_transform(self, i: int) -> int:
        return VisuConst.PADDING+i*VisuConst.BALL_SIZE + i*VisuConst.BALL_SPACE

    def _world_grid_to_abalone_coord(self, mouse_position: vec2) -> Optional[vec2]:

        abalone_coord = self._get_board_coord(mouse_position)

        if self._abalone.is_in_board(abalone_coord) and self._is_mouse_in_ball(mouse_position):
            return abalone_coord
        return None

    def _is_mouse_in_ball(self, mouse_position: vec2) -> bool:
        x = mouse_position.x - VisuConst.PADDING
        y = mouse_position.y - VisuConst.PADDING

        if (y // FULL_BALL_SIZE) % 2:
            x -= HALF_BALL_SIZE
        x %= FULL_BALL_SIZE
        y %= FULL_BALL_SIZE

        x -= HALF_BALL_SIZE
        y -= HALF_BALL_SIZE

        relative_pos = vec2(x, y)

        return vec2(0, 0).distance(relative_pos) <= HALF_BALL_SIZE

    def _get_board_coord(self, mouse_position: vec2) -> vec2:
        x = mouse_position.x - VisuConst.PADDING
        y = mouse_position.y - VisuConst.PADDING

        y //= FULL_BALL_SIZE
        if y % 2:
            x -= HALF_BALL_SIZE
        x //= FULL_BALL_SIZE

        return vec2(x, y)
