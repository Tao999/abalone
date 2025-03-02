from typing import Optional
from game_nodes.abalone_node.game_states.game_state import GameState
import game_nodes.abalone_node.game_states.push_state as pus
from utils.constants import Dir, VisuConst
from utils.singletons import mouse, abalone
from utils.vec import vec2

FULL_BALL_SIZE = VisuConst.BALL_SIZE + VisuConst.BALL_SPACE
HALF_BALL_SIZE = VisuConst.BALL_SIZE//2


class SelectionState(GameState):
    def __init__(self) -> None:
        self._is_first_ball_selected: bool = False
        self._first_selected: Optional[vec2] = None
        self._selected_direction: int = Dir.LEFT
        self._nb_selected_ball: int = 1


    def update(self, delta: float) -> Optional[GameState]:
        if not mouse.is_button_pressed(mouse.LEFT_BUTTON) and not self._is_first_ball_selected:
            self._hover_first_ball()

        elif mouse.is_button_pressed(mouse.LEFT_BUTTON) and not self._is_first_ball_selected:
            self._select_first_ball()

        elif mouse.is_button_pressed(mouse.LEFT_BUTTON) and self._first_selected:
            self._select_firection_and_nb_ball()

        elif not mouse.is_button_pressed(mouse.LEFT_BUTTON) and self._first_selected:
            return pus.PushState()
        return None

    def _hover_first_ball(self) -> None:
        position = SelectionState._world_coord_to_board_coord(
            mouse.get_position())
        if position:
            abalone.select_balls_to_move(position, 0, 1)

    def _select_first_ball(self) -> None:
        pre_select = SelectionState._world_coord_to_board_coord(
            mouse.get_position())
        if abalone.get_ball_at(pre_select) == abalone.get_player_turn():
            self._first_selected = pre_select
        if self._first_selected:
            self._is_first_ball_selected = True

    def _select_firection_and_nb_ball(self) -> None:
        second_position = SelectionState._world_coord_to_board_coord(
            mouse.get_position())
        if second_position:

            self._selected_direction = Dir.get_direction_code(
                self._first_selected, second_position)  # type: ignore

            self._nb_selected_ball = Dir.get_nb_selected_ball(
                self._first_selected, second_position)  # type: ignore
            abalone.select_balls_to_move(
                self._first_selected, self._selected_direction, self._nb_selected_ball)  # type: ignore

    @staticmethod
    def _world_coord_to_board_coord(mouse_position: vec2) -> Optional[vec2]:
        abalone_coord = SelectionState._get_board_coord(mouse_position)

        if abalone.is_in_board(abalone_coord) and SelectionState._is_mouse_in_ball(mouse_position):
            return abalone_coord
        return None

    @staticmethod
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

    @staticmethod
    def _get_board_coord(mouse_position: vec2) -> vec2:
        x = mouse_position.x - VisuConst.PADDING
        y = mouse_position.y - VisuConst.PADDING

        y //= FULL_BALL_SIZE
        if y % 2:
            x -= HALF_BALL_SIZE
        x //= FULL_BALL_SIZE

        return vec2(x, y)
