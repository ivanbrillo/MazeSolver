from Constants import *

type_color_map = dict(Wall="black", StartPoint="green", EndPoint="red")
color_character_map = dict(gray90="-", black="b", green="g", red="r")


class Brick:

    def __init__(self, row: int, col: int, size: int, maze_creator, brick_type="-"):
        self.position = (col * size, row * size, (col + 1) * size, (row + 1) * size)
        self.indexes = (row, col)
        self.color = dict(fill=list(color_character_map.keys())[list(color_character_map.values()).index(brick_type)], outline="black")
        self.mazeCreator = maze_creator
        self.visited = False
        self.father = None

    def cleared(self, event) -> None:
        self.color["fill"] = "gray90"
        self.mazeCreator.update_grid(self, False)

    def clicked(self, event) -> None:
        self.color["fill"] = "black"
        self.mazeCreator.update_grid(self, True)

    def set_type(self, brick_type: str):
        self.color["fill"] = type_color_map[brick_type]
        # return self.color["fill"] == ("red" or "green")

    def get_str(self) -> str:
        return color_character_map[self.color["fill"]]

