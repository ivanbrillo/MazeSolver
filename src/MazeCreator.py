import customtkinter as ctk
import tkinter as tk
from Brick import *
from Solver import *


class MazeCreator(ctk.CTkFrame):
    GRID_SIZE: int = 10
    RECT_SIZE: int = 50

    def __init__(self, master, brick_type):
        super().__init__(master, width=self.GRID_SIZE * self.RECT_SIZE, height=self.GRID_SIZE * self.RECT_SIZE)
        self.canvas = ctk.CTkCanvas(self, width=self.GRID_SIZE * self.RECT_SIZE, height=self.GRID_SIZE * self.RECT_SIZE, highlightthickness=0)
        self.ui = master
        self.maze = None
        self.brick_type = brick_type
        self.create(self.GRID_SIZE)
        self.start: Brick = None
        self.end: Brick = None
        self.solved = False

    def create(self, size: int):

        self.GRID_SIZE = size
        if size > 12:
            self.RECT_SIZE = int(12 * 50 / size)

        self.GRID_SIZE = size
        self.maze = [[Brick(row, column, self.RECT_SIZE, self) for column in range(self.GRID_SIZE)] for row in range(self.GRID_SIZE)]
        self.canvas.destroy()

        self.canvas = ctk.CTkCanvas(self, width=self.GRID_SIZE * self.RECT_SIZE, height=self.GRID_SIZE * self.RECT_SIZE, highlightthickness=0)
        self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.print_grid()

    def print_grid(self) -> None:
        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                brick = self.maze[row][col]

                if brick.get_str() == "g":
                    self.start = brick
                    self.ui.disable_brick("StartPoint")
                if brick.get_str() == "r":
                    self.end = brick
                    self.ui.disable_brick("EndPoint")

                rect_id = self.canvas.create_rectangle(*brick.position, **brick.color)
                self.canvas.tag_bind(rect_id, '<Button-1>', brick.clicked)
                self.canvas.tag_bind(rect_id, '<Button-3>', brick.cleared)

    def update_grid(self, brick: Brick, create_new: bool, old_str: str):

        if self.solved:
            self.clear()

        if old_str == "g":
            self.start = None
        if old_str == "r":
            self.end = None

        self.ui.enable_brick(old_str)

        if create_new:
            brick.set_type(self.brick_type.get())

        if self.brick_type.get() == "StartPoint":
            self.start = brick
        if self.brick_type.get() == "EndPoint":
            self.end = brick

        self.ui.disable_brick(self.brick_type.get())
        rect_id = self.canvas.create_rectangle(*brick.position, **brick.color)
        self.canvas.tag_bind(rect_id, '<Button-1>', brick.clicked)
        self.canvas.tag_bind(rect_id, '<Button-3>', brick.cleared)

    def save_maze_to_file(self):
        with open("maze.txt", "w") as file:
            for row in self.maze:
                row_str = ''.join([cell.get_str() for cell in row])
                file.write(row_str + '\n')

    def load_maze_from_file(self):
        with open("maze.txt", "r") as file:
            rows = file.readlines()
            for i, row in enumerate(rows):
                row = row.strip()
                for j, type_str in enumerate(row):
                    self.maze[i][j] = Brick(i, j, self.RECT_SIZE, self, type_str)
        self.print_grid()

    def get_adjatient(self, brick: Brick) -> list:
        position = brick.indexes

        adj = list()
        if position[0] + 1 < self.GRID_SIZE and self.maze[position[0] + 1][position[1]].get_str() != "b" and not self.maze[position[0] + 1][
            position[1]].visited:
            adj.append(self.maze[position[0] + 1][position[1]])
        if position[0] - 1 >= 0 and self.maze[position[0] - 1][position[1]].get_str() != "b" and not self.maze[position[0] - 1][position[1]].visited:
            adj.append(self.maze[position[0] - 1][position[1]])
        if position[1] + 1 < self.GRID_SIZE and self.maze[position[0]][position[1] + 1].get_str() != "b" and not self.maze[position[0]][
            position[1] + 1].visited:
            adj.append(self.maze[position[0]][position[1] + 1])
        if position[1] - 1 >= 0 and self.maze[position[0]][position[1] - 1].get_str() != "b" and not self.maze[position[0]][position[1] - 1].visited:
            adj.append(self.maze[position[0]][position[1] - 1])

        return adj

    def solve(self):

        if (self.start or self.end) is None:
            return

        solver = Solver(self.start, self.end, self)
        if solver.solve():
            self.solved = True
        else:
            return

        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                brick = self.maze[row][col]
                if brick.visited and brick != self.start and brick != self.end:
                    rect = self.canvas.create_rectangle(*brick.position, fill="gray60", outline="blue")
                    self.canvas.tag_bind(rect, '<Button-1>', lambda event: self.clear())
                    self.canvas.tag_bind(rect, '<Button-3>', lambda event: self.clear())

        brick = self.end.father
        while brick.father is not None:
            rect = self.canvas.create_rectangle(*brick.position, fill="orange", outline="black")
            self.canvas.tag_bind(rect, '<Button-1>', lambda event: self.clear())
            self.canvas.tag_bind(rect, '<Button-3>', lambda event: self.clear())
            brick = brick.father

    def clear(self):
        self.solved = False
        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                self.maze[row][col].visited = False
                self.maze[row][col].father = None
        self.print_grid()
