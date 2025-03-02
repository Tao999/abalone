from tkinter import Canvas
from typing import Optional
import game_nodes.abalone_node.abalone_node as abno
from game_nodes.abalone_node.game_states.game_state import GameState
import game_nodes.abalone_node.game_states.selection_state as sels
from utils.constants import Dir, VisuConst
from utils.singletons import mouse, abalone
from utils.vec import vec2
import game_nodes.abalone_node.abalone_node as an


class PushState(GameState):
    def __init__(self) -> None:
        self._center_of_selected_ball: vec2 = self._get_center_of_selection()
        self._is_triggerd: bool = False
        self._direction_code: int = 0
        self._next_positions: list[vec2] = []

    def update(self, delta) -> Optional[GameState]:
        self._direction_code = Dir.get_direction_code(
            self._center_of_selected_ball, mouse.get_position())
        
        self._next_positions = []
        for ball in abalone.get_selected_balls():
            self._next_positions.append(abalone._get_next_position(ball, self._direction_code))



        if mouse.is_button_pressed(mouse.LEFT_BUTTON):
            self._is_triggerd = True
        elif self._is_triggerd and abalone.move_selected_balls(self._direction_code):
            abalone.next_turn()
            return sels.SelectionState()
        elif mouse.is_button_pressed(mouse.RIGHT_BUTTON):
            return sels.SelectionState()
        else:
            self._is_triggerd = False

        return None

    def _get_center_of_selection(self) -> vec2:
        pos_sum = vec2(0, 0)
        balls = abalone.get_selected_balls()
        for ball_pos in balls:
            corrected = abno.AbaloneNode._board_pos_to_canvas_pos(ball_pos)
            pos_sum += corrected

        return pos_sum//len(balls)
    
    def draw_ball(self, position: vec2, canvas: Canvas) -> None:
        ball = abalone.get_ball_at(position)
        if ball < 0:
            return

        ball_origin = an.AbaloneNode._board_pos_to_canvas_pos(position)
        ball_end = vec2(ball_origin.x + VisuConst.BALL_SIZE,
                        ball_origin.y + VisuConst.BALL_SIZE)

        ball_color = VisuConst.PLAYER_COLOR[ball]
        outline_color = VisuConst.NOT_HOVERED_BALL

        if position in self._next_positions:
            outline_color = VisuConst.NEXT_BALL_POSITION
        if position in abalone.get_selected_balls():
            outline_color = VisuConst.HOVERED_BALL

        canvas.create_oval(ball_origin.x, ball_origin.y, ball_end.x, ball_end.y,
                        fill=ball_color, width=VisuConst.OUTLINE_WIDTH, outline=outline_color)
