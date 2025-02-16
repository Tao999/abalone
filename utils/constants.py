
from utils.vec import vec2


class Const:
    NO_PLAYER = 0
    PLAYER_ONE = 1
    PLAYER_TWO = 2

    GRID_SIZE = 9
    LOSING_SCORE = 8


class VisuConst:
    PADDING = 10
    BALL_SIZE = 50
    BALL_SPACE = 5
    OUTLINE_WIDTH = 3

    PLAYER_COLOR = ["", "#c4c4c4", "#3a3a3a"]

    BACKGROUND_COLOR = "#654526"

    HOVERED_BALL = "#00bf00"
    NOT_HOVERED_BALL = "#000000"


class Dir:
    LEFT = 0
    UP_LEFT = 1
    UP_RIGHT = 2
    RIGHT = 3
    DOWN_RIGHT = 4
    DOWN_LEFT = 5

    @staticmethod
    def get_direction_code(first_pos: vec2, second_pos: vec2) -> int:
        first_center = vec2(first_pos.x, first_pos.y)
        first_center *= 2
        if (first_center.y//2) % 2:
            first_center.x += 1

        second_center = vec2(second_pos.x, second_pos.y)
        second_center *= 2
        if (second_center.y//2) % 2:
            second_center.x += 1
        angle = (first_center.get_degree_angle(second_center)+210) % 360

        return angle // 60

    @staticmethod
    def get_nb_selected_ball(first_pos: vec2, second_pos: vec2) -> int:
        first_center = vec2(first_pos.x, first_pos.y)
        first_center *= 2
        if (first_center.y//2) % 2:
            first_center.x += 1

        second_center = vec2(second_pos.x, second_pos.y)
        second_center *= 2
        if (second_center.y//2) % 2:
            second_center.x += 1
        nb_x = abs(first_center.x - second_center.x)
        nb_y = abs(first_center.y - second_center.y)
        return min((nb_x + nb_y)//2 + 1, 3)
