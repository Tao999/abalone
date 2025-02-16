from tkinter import Canvas
from game_nodes.abalone_node.abalone import Abalone
from game_nodes.game_node import GameNode
from utils.constants import Constant
from utils.vec import vec2


PADDING = 10
BALL_SIZE = 50
BALL_SPACE = 5
DRAW_WIDTH = 3

PLAYER_COLOR = ["", "white", "black"]


class AbaloneNode(GameNode):
    def __init__(self) -> None:
        super().__init__()
        self._abalone = Abalone()
    
    

    def update(self, delta: float) -> None:
        super().update(delta)
        # TODO
    
    def draw(self, canvas: Canvas) -> None:
        super().draw(canvas)
        
        for y in range(Constant.GRID_SIZE):
            for x in range(Constant.GRID_SIZE):
                ball = self._abalone.get_ball_at(vec2(x, y))
                if ball >= 0:
                    offset = 0
                    if y % 2:
                        offset = BALL_SIZE//2
                    ball_origin = vec2(self._ball_transform(x) + offset, self._ball_transform(y))
                    ball_end = vec2(ball_origin.x + BALL_SIZE, ball_origin.y + BALL_SIZE)
                    color = PLAYER_COLOR[ball]
                    canvas.create_oval(ball_origin.x, ball_origin.y, ball_end.x, ball_end.y, fill=color, width=DRAW_WIDTH)
    
    def _ball_transform(self, i: int) -> int:
        return PADDING+i*BALL_SIZE + i*BALL_SPACE