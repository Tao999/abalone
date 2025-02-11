from typing import Union


class HexGrid:
    def __init__(self, size: int) -> None:
        if size < 0:
            raise ValueError("La taille du tableau ne pas être en dessous de 0")
        
        self._size = size
        self._board: list[list[int]] = []

        for _ in range(size):
            line = []
            for __ in range(size):
                line.append(0)
            self._board.append(line)
        
    def __str__(self) -> str:
        output = ""
        for i in range(self._size):
            if i%2:
                output = f"{output} "
            for j in range(self._size):
                output = f"{output}{self._board[i][j]} "
            output = f"{output}\n"
        return output

    def get_item(self, x: int, y: int) -> int:
        return self._board[x][y]
    
    def set_item(self, x: int, y: int, value: int) -> None:
        self._board[x][y] = value
