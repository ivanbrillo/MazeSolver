import customtkinter as ctk
import tkinter as tk
from Brick import *


class MazeCreator(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, width=600)

        self.matrix = [[Brick(row, column, self) for column in range(GRID_SIZE)] for row in range(GRID_SIZE)]

        self.canvas = ctk.CTkCanvas(self, width=GRID_SIZE * RECT_SIZE, height=GRID_SIZE * RECT_SIZE, highlightthickness=0)
        self.print_grid()
        self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



    def print_grid(self) -> None:
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                brick = self.matrix[row][col]
                rect_id = self.canvas.create_rectangle(*brick.position, **brick.color)
                self.canvas.tag_bind(rect_id, '<Button-1>', brick.clicked)
