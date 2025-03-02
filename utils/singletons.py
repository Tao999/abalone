from utils.abalone import Abalone
from utils.vec import vec2


class Mouse:
    RIGHT_BUTTON = 0b10
    LEFT_BUTTON = 0b01
    def __init__(self):
        self._position = vec2(0, 0)
        self._press_state = 0b00

    def set_position(self, position: vec2):
        self._position = position

    def get_position(self) -> vec2:
        return self._position
    
    def press_button(self, button_pressed: int) -> None:
        self._press_state |= button_pressed
    
    def unpress_button(self, button_pressed: int) -> None:
        self._press_state &= ~button_pressed

    def is_button_pressed(self, button: int) -> bool:
        return self._press_state & button


mouse = Mouse()
abalone = Abalone()
