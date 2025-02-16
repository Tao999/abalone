from math import ceil
from tkinter import Canvas
from typing import Optional
from utils.abalone import Abalone
from game_nodes.game_node import GameNode
from utils.constants import Const, Dir
from utils.vec import vec2
from utils.constants import VisuConst
import game_nodes.abalone_node.draw_functions as df
from utils.singletons import mouse


class AbaloneNode(GameNode):
    def __init__(self) -> None:
        super().__init__()
        self._abalone = Abalone()
        self.state = SelectionState(self._abalone)

    def update(self, delta: float) -> None:
        super().update(delta)
        self.state.update()

    def draw(self, canvas: Canvas) -> None:
        super().draw(canvas)

        for y in range(Const.GRID_SIZE):
            for x in range(Const.GRID_SIZE):
                df._draw_ball(self._abalone, vec2(x, y), canvas)


class SelectionState:
    def __init__(self, abalone: Abalone) -> None:
        self._is_first_ball_selected: bool = False
        self._first_selected: Optional[vec2] = None
        self._selected_direction: int = Dir.LEFT
        self._nb_selected_ball: int = 1
        self._abalone = abalone

    def update(self):
        self._select_first_ball()

    def _select_first_ball(self) -> None:
        if not mouse.is_button_pressed() and not self._is_first_ball_selected:
            position = df._world_coord_to_board_coord(
                self._abalone, mouse.get_position())
            if position:
                self._abalone.select_balls_to_move(position, 0, 1)
        elif mouse.is_button_pressed() and not self._is_first_ball_selected:
            self._first_selected = df._world_coord_to_board_coord(
                self._abalone, mouse.get_position())
            if self._first_selected:
                self._is_first_ball_selected = True

        elif mouse.is_button_pressed() and self._first_selected:
            second_position = df._world_coord_to_board_coord(
                self._abalone, mouse.get_position())
            if second_position:

                self._selected_direction = Dir.get_direction_code(
                    self._first_selected, second_position)

                self._nb_selected_ball = Dir.get_nb_selected_ball(
                    self._first_selected, second_position)
                self._abalone.select_balls_to_move(
                    self._first_selected, self._selected_direction, self._nb_selected_ball)

        elif not mouse.is_button_pressed() and self._first_selected:
            # On doit sortir de cette état
            ...
