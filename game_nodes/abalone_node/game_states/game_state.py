from abc import abstractmethod, ABC
from typing import Optional


class GameState(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def update(self, delta: float) -> Optional["GameState"]:
        ...
