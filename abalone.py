from math import ceil, floor
from constants import Constant
from hexgrid import HexGrid

class Abalone:
    def __init__(self) -> None:
        self._board = HexGrid(Constant.GRID_SIZE)
        self._init_balls()
    
    def _init_balls(self) -> None:
        for i in range(2, 7):
            self._board.set_item(0, i, Constant.PLAYER_TWO)
        
        for i in range(1, 7):
            self._board.set_item(1, i, Constant.PLAYER_TWO)
        
        for i in range(3, 6):
            self._board.set_item(2, i, Constant.PLAYER_TWO)
        
        for i in range(2, 7):
            self._board.set_item(8, i, Constant.PLAYER_ONE)
        
        for i in range(1, 7):
            self._board.set_item(7, i, Constant.PLAYER_ONE)

        for i in range(3, 6):
            self._board.set_item(6, i, Constant.PLAYER_ONE)
    
    def __str__(self) -> str:
        output = ""
        for i in range(Constant.GRID_SIZE):
            if i%2:
                output = f"{output} "
            for j in range(Constant.GRID_SIZE):
                if self._is_in_board(j, i):
                    output = f"{output}{self._board.get_item(i, j)} "
                else:
                    output = f"{output}  "
            output = f"{output}\n"
        return output
    
    def _is_in_board(self, posx: int, posy: int) -> bool:
        center = ceil(Constant.GRID_SIZE/2)
        posy -= center
        
        rognage = abs(0.5*posy+0.5)

        return floor(rognage) <= posx < Constant.GRID_SIZE- ceil(rognage)


a = Abalone()

print(a)