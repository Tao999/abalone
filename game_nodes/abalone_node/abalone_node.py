from tkinter import Canvas
from game_nodes.abalone_node.game_states.game_state import GameState
from game_nodes.abalone_node.game_states.selection_state import SelectionState
from game_nodes.game_node import GameNode
from utils.constants import Const, VisuConst
from utils.vec import vec2
from utils.singletons import abalone


class AbaloneNode(GameNode):
    def __init__(self) -> None:
        super().__init__()
        self.state: GameState = SelectionState()

    def update(self, delta: float) -> None:
        super().update(delta)
        futur_state = self.state.update(delta)
        if futur_state:
            self.state = futur_state
        
    def draw(self, canvas: Canvas) -> None:
        super().draw(canvas)

        for y in range(Const.GRID_SIZE):
            for x in range(Const.GRID_SIZE):
                self.state.draw_ball(vec2(x, y), canvas)

    # def _draw_ball(self, position: vec2, canvas: Canvas) -> None:
    #     ball = abalone.get_ball_at(position)
    #     if ball < 0:
    #         return

    #     ball_origin = AbaloneNode._board_pos_to_canvas_pos(position)
    #     ball_end = vec2(ball_origin.x + VisuConst.BALL_SIZE,
    #                     ball_origin.y + VisuConst.BALL_SIZE)

    #     ball_color = VisuConst.PLAYER_COLOR[ball]
    #     outline_color = VisuConst.NOT_HOVERED_BALL
    #     if position in abalone.get_selected_balls():
    #         outline_color = VisuConst.HOVERED_BALL

    #     canvas.create_oval(ball_origin.x, ball_origin.y, ball_end.x, ball_end.y,
    #                     fill=ball_color, width=VisuConst.OUTLINE_WIDTH, outline=outline_color)

    @staticmethod    
    def _board_pos_to_canvas_pos(pos: vec2) -> vec2:
        offset = 0
        if pos.y % 2:
            offset = VisuConst.BALL_SIZE//2
        x = VisuConst.PADDING+pos.x*VisuConst.BALL_SIZE + \
            pos.x*VisuConst.BALL_SPACE + offset
        y = VisuConst.PADDING+pos.y*VisuConst.BALL_SIZE + pos.y*VisuConst.BALL_SPACE
        return vec2(x, y)

