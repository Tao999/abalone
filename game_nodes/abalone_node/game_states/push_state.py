from typing import Optional
import game_nodes.abalone_node.abalone_node as abno
from game_nodes.abalone_node.game_states.game_state import GameState
import game_nodes.abalone_node.game_states.selection_state as sels
from utils.constants import Dir
from utils.singletons import mouse, abalone
from utils.vec import vec2


class PushState(GameState):
    def __init__(self) -> None:
        self._center_of_selected_ball: vec2 = self._get_center_of_selection()
        self._is_triggerd: bool = False

    def update(self, delta) -> Optional[GameState]:
        direction_code = Dir.get_direction_code(
            self._center_of_selected_ball, mouse.get_position())


        if mouse.is_button_pressed(mouse.LEFT_BUTTON):
            self._is_triggerd = True
        elif self._is_triggerd and abalone.move_selected_balls(direction_code):
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
            print(corrected, mouse.get_position())
        

        return pos_sum//len(balls)
