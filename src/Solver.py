from MazeCreator import *
from Brick import *


class Solver:

    def __init__(self, start_brick: Brick, target: Brick, maze):
        self.start_brick = start_brick
        self.target = target
        self.maze = maze
        self.edge_brick: list = None

    def _add_adj_brick(self) -> bool:
        adj = self.maze.get_adjatient(self.edge_brick[0])

        for brick in adj:
            brick.father = self.edge_brick[0]
            brick.visited = True
            if brick.get_str() == "r":
                return True

        self.edge_brick = self.edge_brick + adj
        self.edge_brick.pop(0)
        return False

    def solve(self) -> bool:
        self.edge_brick = [self.start_brick, ]
        self.edge_brick[0].visited = True

        while len(self.edge_brick) != 0:
            if self._add_adj_brick():
                return True

        return False
