from math import ceil, floor, sin
from constants import Constant, Dir
from hexgrid import HexGrid
from vec import vec2

class Abalone:
    def __init__(self) -> None:
        self._board = HexGrid(Constant.GRID_SIZE)
        self._select_balls: list[vec2] = []
        self._current_player: int = 1
        self._selection_direction: int = Dir.LEFT
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
        copy_pos = vec2(pos.x, pos.y)
        if copy_pos.y < 0 or copy_pos.y >= Constant.GRID_SIZE:
            return False
        center = ceil(Constant.GRID_SIZE/2)
        copy_pos.y -= center
        
        rognage = abs(0.5*copy_pos.y+0.5)

        return floor(rognage) <= copy_pos.x < Constant.GRID_SIZE- ceil(rognage)
    
    def select_balls_to_move(self, selected_pos: vec2, direction: int, nb_ball: int) -> bool:
        if nb_ball > 3 or nb_ball < 1:
            return False
        self._selection_direction = direction
        selected_balls = [selected_pos]

        for _ in range(nb_ball-1):
            selected_balls.append(self._get_next_position(selected_balls[-1], direction))
        
        for ball in selected_balls:
            if not self._is_in_board(ball):
                return False

        self._select_balls = selected_balls
        return self._is_selected_balls_from_current_player(selected_balls)

    def _is_selected_balls_from_current_player(self, selected_balls: list[vec2]) -> bool:
        for ball in selected_balls:
            if self._board.get_item(ball) != self._current_player:
                return False
        return True


    def _get_next_position(self, current_pos: vec2, direction: int) -> vec2:
        dir_v = direction
        x = floor(dir_v*1.6-2)/2 if dir_v <= 3 else -dir_v+4.5
        if current_pos.y % 2:
            x+=0.5
        y = floor(sin(-dir_v)+0.5)
        next_pos = vec2(int(x+current_pos.x), int(y+current_pos.y))
        return next_pos
    
    def move_selected_balls(self, direction: int) -> bool:
        if not self._is_move_legal(direction):
            return False
        
        if self._selection_direction == direction:
            self._select_balls.reverse()
            self._selection_direction = (self._selection_direction + 6) % 6

        if self._is_way_free(direction):
            for ball in self._select_balls:
                self._translate_ball(ball, direction)
        else:
            return self._do_sumito(direction)
        return True

    def _is_move_legal(self, direction: int) -> bool:
        for ball in self._select_balls:
            next_pos = self._get_next_position(ball, direction)
            if not self._is_in_board(next_pos):
                return False
        return True

    def _is_way_free(self, direction: int) -> bool:
        for ball in self._select_balls:
            target_pos = self._get_next_position(ball, direction)
            if (
                target_pos not in self._select_balls and
                self._board.get_item(target_pos) != Constant.NO_PLAYER
                ):
                return False
        return True
    
    def _translate_ball(self, ball: vec2, direction: int):
        player_moving = self._board.get_item(ball)
        target_pos = self._get_next_position(ball, direction)
        if self._board.get_item(target_pos) != Constant.NO_PLAYER:
            self._translate_ball(target_pos, direction)
        self._board.set_item(ball, Constant.NO_PLAYER)
        if self._is_in_board(target_pos):
            self._board.set_item(target_pos, player_moving)

    def _do_sumito(self, direction: int) -> bool:
        player_force = len(self._select_balls)
        oposite_force: int = 0

        target_dir = self._get_next_position(self._select_balls[0], direction)
        player_at_target = self._board.get_item(target_dir)
        while (
            self._is_in_board(target_dir) and
            player_at_target != Constant.NO_PLAYER
            ):
            if (
                player_at_target != self._current_player and
                player_at_target != Constant.NO_PLAYER
                ):
                oposite_force += 1
            target_dir = self._get_next_position(target_dir, direction)
            player_at_target = self._board.get_item(target_dir)
        
        if player_force <= oposite_force:
            return False

        for ball in self._select_balls:
            self._translate_ball(ball, direction)
        return True

a = Abalone()

print(a.get_grid_str(True))
a.select_balls_to_move(vec2(2, 8), Dir.UP_RIGHT, 3)
a.move_selected_balls(Dir.UP_RIGHT)
print(a.get_grid_str(False))
