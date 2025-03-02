from abc import abstractmethod, ABC
from tkinter import Canvas
from typing import Optional
from utils.singletons import abalone
import game_nodes.abalone_node.abalone_node as an
from utils.constants import VisuConst
from utils.vec import vec2


class GameState(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def update(self, delta: float) -> Optional["GameState"]:
        ...
    
    def draw_ball(self, position: vec2, canvas: Canvas) -> None:
        ball = abalone.get_ball_at(position)
        if ball < 0:
            return

        ball_origin = an.AbaloneNode._board_pos_to_canvas_pos(position)
        ball_end = vec2(ball_origin.x + VisuConst.BALL_SIZE,
                        ball_origin.y + VisuConst.BALL_SIZE)

        ball_color = VisuConst.PLAYER_COLOR[ball]
        outline_color = VisuConst.NOT_HOVERED_BALL
        if position in abalone.get_selected_balls():
            outline_color = VisuConst.HOVERED_BALL

        canvas.create_oval(ball_origin.x, ball_origin.y, ball_end.x, ball_end.y,
                        fill=ball_color, width=VisuConst.OUTLINE_WIDTH, outline=outline_color)

