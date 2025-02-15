from math import ceil, floor
from constants import Constant
from hexgrid import HexGrid
from vec import vec2

class Abalone:
    def __init__(self) -> None:
        self._board = HexGrid(Constant.GRID_SIZE)
        self._init_balls()
    
    def _init_balls(self) -> None:
        for i in range(2, 7):
            self._board.set_item(vec2(0, i), Constant.PLAYER_TWO)
        
        for i in range(1, 7):
            self._board.set_item(vec2(1, i), Constant.PLAYER_TWO)
        
        for i in range(3, 6):
            self._board.set_item(vec2(2, i), Constant.PLAYER_TWO)
        
        for i in range(2, 7):
            self._board.set_item(vec2(8, i), Constant.PLAYER_ONE)
        
        for i in range(1, 7):
            self._board.set_item(vec2(7, i), Constant.PLAYER_ONE)

        for i in range(3, 6):
            self._board.set_item(vec2(6, i), Constant.PLAYER_ONE)
    
    def __str__(self) -> str:
        output = ""
        for i in range(Constant.GRID_SIZE):
            if i%2:
                output = f"{output} "
            for j in range(Constant.GRID_SIZE):
                current_pos = vec2(j, i)
                if self._is_in_board(current_pos):
                    output = f"{output}{self._board.get_item(current_pos)} "
                else:
                    output = f"{output}  "
            output = f"{output}\n"
        return output
    
    def _is_in_board(self, pos: vec2) -> bool:
        center = ceil(Constant.GRID_SIZE/2)
        pos.y -= center
        
        rognage = abs(0.5*pos.y+0.5)

        return floor(rognage) <= pos.x < Constant.GRID_SIZE- ceil(rognage)
    



a = Abalone()

print(a)