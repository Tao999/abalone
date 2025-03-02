from utils.abalone import Abalone
from utils.vec import vec2


class Mouse:
    def __init__(self):
        self._position = vec2(0, 0)
        self._is_button_pressed = False

    def set_position(self, position: vec2):
        self._position = position

    def get_position(self) -> vec2:
        return self._position
    
    def set_button_pressed(self, button_pressed: bool) -> None:
        self._is_button_pressed = button_pressed

    def is_button_pressed(self) -> bool:
        return self._is_button_pressed


mouse = Mouse()
abalone = Abalone()
