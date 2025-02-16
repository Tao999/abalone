from game_nodes.abalone_node.abalone import Abalone
from game_nodes.game_node import GameNode


class AbaloneNode(GameNode):
    def __init__(self):
        self._abalone = Abalone()
    
    def update(self, delta):
        # TODO
        ...
    
    def draw(self, canvas):
        # TODO
        ...