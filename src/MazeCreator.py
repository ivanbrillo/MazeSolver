import customtkinter as ctk
import tkinter as tk
from Brick import *


class MazeCreator(ctk.CTkFrame):
    GRID_SIZE: int = 10
    RECT_SIZE: int = 50

    def __init__(self, master):
        super().__init__(master, width=self.GRID_SIZE * self.RECT_SIZE, height=self.GRID_SIZE * self.RECT_SIZE)
        self.canvas = ctk.CTkCanvas(self, width=self.GRID_SIZE * self.RECT_SIZE, height=self.GRID_SIZE * self.RECT_SIZE, highlightthickness=0)
        self.matrix = None
        self.create(self.GRID_SIZE)

    def create(self, size: int):

        self.GRID_SIZE = size
        if size > 12:
            self.RECT_SIZE = 12*50/size

        self.GRID_SIZE = size
        self.matrix = [[Brick(row, column, self.RECT_SIZE, self) for column in range(self.GRID_SIZE)] for row in range(self.GRID_SIZE)]
        self.canvas.destroy()

        self.canvas = ctk.CTkCanvas(self, width=self.GRID_SIZE * self.RECT_SIZE, height=self.GRID_SIZE * self.RECT_SIZE, highlightthickness=0)
        self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.print_grid()

    def print_grid(self) -> None:
        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                brick = self.matrix[row][col]
                rect_id = self.canvas.create_rectangle(*brick.position, **brick.color)
                self.canvas.tag_bind(rect_id, '<Button-1>', brick.clicked)
