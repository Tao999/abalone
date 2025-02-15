from abalone import Abalone
import re

from constants import Constant
from vec import vec2


class CliApp():

    def __init__(self):
        self._abalone = Abalone()
    
    def play(self):
        wining_player = self._abalone.player_who_win()
        while wining_player == 0:
            print(self._abalone.get_grid_str())
            print(f"P1:{self._abalone.get_score_of(Constant.PLAYER_ONE)} |", end=" ")
            print(f"{self._abalone.get_score_of(Constant.PLAYER_TWO)}:P2")
            print(f"Tour du joueur : {self._abalone.get_player_turn()}")
            while not self._ball_selection():
                print("Les boulles séléctionnées ne respecte pas les conditions de séléction")
            
            push_direction = self._select_push_direction()
            if self._abalone.move_selected_balls(push_direction):
                self._abalone.next_turn()
            else:
                print("\n/!\\Les boules séléctionnées ne pouvent pas bouger./!\\")
                input("Entrée pour continuer.")
            wining_player = self._abalone.player_who_win()
        
        print(f"Le joueur {wining_player} à gagné !")

    def _ball_selection(self) -> bool:
        tmp_input = ""
        while not re.match(r"^\d,\d$", tmp_input):
            tmp_input = input("Choisir une case au format n,p : ")

        x, y = tmp_input.split(",")
        selected_ball =  vec2(int(x), int(y))

        direction = ""
        while direction not in ("z", "e", "q", "d", "w", "x"):
            print(" Z   E")
            print("  ↖ ↗")
            print("Q←   →D")
            print("  ↙ ↘")
            print(" W   X")
            direction = input("Sélectionner la direction de séléction comme indiqué : ").lower()
        
        selected_direction = "qzedxw".index(direction)

        nb_ball = -1
        while nb_ball < 1 or nb_ball > 3:
            tmp_input = input("Sélectionner le nombre de boule (entre 1 et 3) : ")
            if re.match(r"^\d$", tmp_input):
                nb_ball = int(tmp_input)

        return self._abalone.select_balls_to_move(selected_ball, selected_direction, nb_ball)
    
    def _select_push_direction(self):
        direction = ""
        while direction not in ("z", "e", "q", "d", "w", "x"):
            print(" Z   E")
            print("  ↖ ↗")
            print("Q←   →D")
            print("  ↙ ↘")
            print(" W   X")
            direction = input("Sélectionner la direction dans laquelle pousser les boules : ").lower()
        
        return "qzedxw".index(direction)        

if __name__ == "__main__":
    app = CliApp()
    app._abalone._board._grid = [[0, 0, 0, 1, 2, 0, 0, 0, 0], [0, 2, 0, 2, 2, 0, 0, 0, 0], [2, 0, 0, 2, 2, 0, 1, 0, 0], [2, 0, 0, 2, 0, 0, 1, 0, 0], [2, 0, 0, 0, 0, 0, 0, 1, 1], [2, 2, 0, 0, 0, 0, 0, 1, 1], [2, 2, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    app._abalone.current_turn = 1
    app.play()