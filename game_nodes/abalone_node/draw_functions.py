from tkinter import Canvas
from typing import Optional
from utils.abalone import Abalone
from utils.constants import VisuConst
from utils.singletons import mouse
from utils.vec import vec2


FULL_BALL_SIZE = VisuConst.BALL_SIZE + VisuConst.BALL_SPACE
HALF_BALL_SIZE = VisuConst.BALL_SIZE//2


def _draw_ball(abalone: Abalone, position: vec2, canvas: Canvas) -> None:
    ball = abalone.get_ball_at(position)
    if ball < 0:
        return

    ball_origin = _ball_transform(position)
    ball_end = vec2(ball_origin.x + VisuConst.BALL_SIZE,
                    ball_origin.y + VisuConst.BALL_SIZE)

    ball_color = VisuConst.PLAYER_COLOR[ball]
    outline_color = VisuConst.NOT_HOVERED_BALL
    if position in abalone.get_selected_balls():
        outline_color = VisuConst.HOVERED_BALL

    canvas.create_oval(ball_origin.x, ball_origin.y, ball_end.x, ball_end.y,
                       fill=ball_color, width=VisuConst.OUTLINE_WIDTH, outline=outline_color)


def _ball_transform(pos: vec2) -> vec2:
    offset = 0
    if pos.y % 2:
        offset = VisuConst.BALL_SIZE//2
    x = VisuConst.PADDING+pos.x*VisuConst.BALL_SIZE + \
        pos.x*VisuConst.BALL_SPACE + offset
    y = VisuConst.PADDING+pos.y*VisuConst.BALL_SIZE + pos.y*VisuConst.BALL_SPACE
    return vec2(x, y)


def _world_coord_to_board_coord(abalone: Abalone, mouse_position: vec2) -> Optional[vec2]:

    abalone_coord = _get_board_coord(mouse_position)

    if abalone.is_in_board(abalone_coord) and _is_mouse_in_ball(mouse_position):
        return abalone_coord
    return None


def _is_mouse_in_ball(mouse_position: vec2) -> bool:
    x = mouse_position.x - VisuConst.PADDING
    y = mouse_position.y - VisuConst.PADDING

    if (y // FULL_BALL_SIZE) % 2:
        x -= HALF_BALL_SIZE
    x %= FULL_BALL_SIZE
    y %= FULL_BALL_SIZE

    x -= HALF_BALL_SIZE
    y -= HALF_BALL_SIZE

    relative_pos = vec2(x, y)

    return vec2(0, 0).distance(relative_pos) <= HALF_BALL_SIZE + VisuConst.OUTLINE_WIDTH


def _get_board_coord(mouse_position: vec2) -> vec2:
    x = mouse_position.x - VisuConst.PADDING
    y = mouse_position.y - VisuConst.PADDING

    y //= FULL_BALL_SIZE
    if y % 2:
        x -= HALF_BALL_SIZE
    x //= FULL_BALL_SIZE

    return vec2(x, y)
