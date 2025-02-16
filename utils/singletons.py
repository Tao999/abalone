from utils.vec import vec2


class Mouse:
    def __init__(self):
        self._position = vec2(0, 0)

    def set_position(self, position: vec2):
        self._position = position

    def get_position(self) -> vec2:
        return self._position


mouse = Mouse()
