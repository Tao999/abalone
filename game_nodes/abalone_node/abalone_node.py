from tkinter import Canvas
from game_nodes.abalone_node.game_states.game_state import GameState
from game_nodes.abalone_node.game_states.selection_state import SelectionState
from game_nodes.game_node import GameNode
import game_nodes.menu_node.menu_node as mn
from utils.abalone import Abalone
from utils.constants import Const, VisuConst
from utils.vec import vec2
from utils.singletons import abalone
import tkinter as tk


class AbaloneNode(GameNode):
    def __init__(self, parent: GameNode, root: tk.Tk) -> None:
        super().__init__(parent, root)
        self.state: GameState = SelectionState()
        self._root.bind('<Escape>', self.back_to_menu)
        abalone.reset_game()


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
    
    def back_to_menu(self, canvas: Canvas) -> None:
        self._parent.clear_nodes()
        self._root.unbind('<Escape>')
        self._parent.add_node(mn.MenuNode(self._parent, self._root))

    @staticmethod    
    def _board_pos_to_canvas_pos(pos: vec2) -> vec2:
        offset = 0
        if pos.y % 2:
            offset = VisuConst.BALL_SIZE//2
        x = VisuConst.PADDING+pos.x*VisuConst.BALL_SIZE + \
            pos.x*VisuConst.BALL_SPACE + offset
        y = VisuConst.PADDING+pos.y*VisuConst.BALL_SIZE + pos.y*VisuConst.BALL_SPACE
        return vec2(x, y)

