from utils.vec import vec2


class HexGrid:
    def __init__(self, size: int) -> None:
        if size < 0:
            raise ValueError("La taille du tableau ne pas être en dessous de 0")

        self._size = size
        self._grid: list[list[int]] = []

        for _ in range(size):
            line = []
            for __ in range(size):
                line.append(0)
            self._grid.append(line)

    def __str__(self) -> str:
        output = ""
        for i in range(self._size):
            if i%2:
                output = f"{output} "
            for j in range(self._size):
                output = f"{output}{self._grid[i][j]} "
            output = f"{output}\n"
        return output

    def get_item(self, pos: vec2) -> int:
        return self._grid[pos.x][pos.y]

    def set_item(self, pos: vec2, value: int) -> None:
        self._grid[pos.x][pos.y] = value
