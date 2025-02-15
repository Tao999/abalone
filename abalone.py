from math import ceil, floor, sin
from constants import Constant, Dir
from hexgrid import HexGrid
from vec import vec2

class Abalone:
    def __init__(self) -> None:
        self._board = HexGrid(Constant.GRID_SIZE)
        self._select_balls: list[vec2] = []
        self._current_player: int = 1
        self._init_balls()
    
    def _init_balls(self) -> None:
        for i in range(2, 7):
            self._board.set_item(vec2(i, 0), Constant.PLAYER_TWO)
        
        for i in range(1, 7):
            self._board.set_item(vec2(i, 1), Constant.PLAYER_TWO)
        
        for i in range(3, 6):
            self._board.set_item(vec2(i, 2), Constant.PLAYER_TWO)
        
        for i in range(2, 7):
            self._board.set_item(vec2(i, 8), Constant.PLAYER_ONE)
        
        for i in range(1, 7):
            self._board.set_item(vec2(i, 7), Constant.PLAYER_ONE)

        for i in range(3, 6):
            self._board.set_item(vec2(i, 6), Constant.PLAYER_ONE)
    
    def get_grid_str(self, print_separator=True) -> str:
        # Affichage des coordonnés x
        output = "y\\x)0)1)2)3)4)5)6)7)8)\n"
        for i in range(Constant.GRID_SIZE):
            # Affichage des coordonnés x
            output = f"{output}{i}."
            if i%2:
                # Décalage due à la grille hex
                output = f"{output} "
            if print_separator:
                separator = "(" if i % 2 == 0 else ")"
            else:
                separator = " "
            output = f"{output}{separator}"

            for j in range(Constant.GRID_SIZE):
                if self._is_in_board(vec2(j, i)):
                    # On affiche que les boules dans la grilles
                    output = f"{output}{self._board.get_item(vec2(j, i))}{separator}"
                else:
                    output = f"{output} {separator}"
            output = f"{output}\n"
        return f"{output}y/x)0)1)2)3)4)5)6)7)8)"
    
    def _is_in_board(self, pos: vec2) -> bool:
        center = ceil(Constant.GRID_SIZE/2)
        pos.y -= center
        
        rognage = abs(0.5*pos.y+0.5)

        return floor(rognage) <= pos.x < Constant.GRID_SIZE- ceil(rognage)
    
    def select_balls_to_move(self, selected_pos: vec2, direction: Dir, nb_ball: int) -> bool:
        if nb_ball > 3 or nb_ball < 1:
            return False
        selected_balls = [selected_pos]

        for _ in range(nb_ball-1):
            selected_balls.append(self._get_next_position(selected_balls[-1], direction))
        
        self._select_balls = selected_balls
        return self._is_selected_balls_from_current_player(selected_balls)

    def _is_selected_balls_from_current_player(self, selected_balls: list[vec2]) -> bool:
        for ball in selected_balls:
            if self._board.get_item(ball) != self._current_player:
                return False
        return True


    def _get_next_position(self, current_pos: vec2, direction: Dir) -> vec2:
        dir_v = direction.value
        x = floor(dir_v*1.6-2)/2 if dir_v <= 3 else -dir_v+4.5
        if current_pos.y % 2:
            x+=0.5
        y = floor(sin(-dir_v)+0.5)
        next_pos = vec2(int(x+current_pos.x), int(y+current_pos.y))
        return next_pos

a = Abalone()

print(a.get_grid_str())
print(a.select_balls_to_move(vec2(2, 8), Dir.UP_LEFT, 3))
