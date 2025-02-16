from abc import ABC, abstractmethod
from tkinter import Canvas

class GameNode(ABC):

    @abstractmethod
    def update(self, delta: float):
        ...
    
    @abstractmethod
    def draw(self, canvas: Canvas):
        ...