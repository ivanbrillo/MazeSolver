import customtkinter as ctk
import tkinter as tk
from Brick import *


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
                rect_id = self.canvas.create_rectangle(*brick.position, **brick.color)
                self.canvas.tag_bind(rect_id, '<Button-1>', brick.clicked)
                self.canvas.tag_bind(rect_id, '<Button-3>', brick.cleared)

    def update_grid(self, brick: Brick, color: bool):
        if color:
            brick.set_type(self.brick_type.get())

        self.ui.disable_brick(self.brick_type.get())

        rect_id = self.canvas.create_rectangle(*brick.position, **brick.color)
        self.canvas.tag_bind(rect_id, '<Button-1>', brick.clicked)
        self.canvas.tag_bind(rect_id, '<Button-3>', brick.cleared)
        self.save_maze_to_file()

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
