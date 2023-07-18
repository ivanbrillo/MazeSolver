from Constants import *

class Brick:

    def __init__(self, row: int, col: int, size: int, mazeCreator):
        self.position = (col * size, row * size, (col + 1) * size, (row + 1) * size)
        self.color = dict(fill="gray90", outline="black")
        self.mazeCreator = mazeCreator

    def clicked(self, event) -> None:
        self.color["fill"] = "black"
        self.mazeCreator.print_grid()

