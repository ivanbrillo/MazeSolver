from Constants import *

class Brick:

    def __init__(self, row: int, col: int, mazeCreator):
        self.position = (col * RECT_SIZE, row * RECT_SIZE, (col + 1) * RECT_SIZE, (row + 1) * RECT_SIZE)
        self.color = dict(fill="white", outline="black")
        self.mazeCreator = mazeCreator

    def clicked(self, event) -> None:
        self.color["fill"] = "black"
        self.mazeCreator.print_grid()

