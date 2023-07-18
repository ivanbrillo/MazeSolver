import customtkinter as ctk
import tkinter as tk
from Brick import *

GRID_SIZE = 10
RECT_SIZE = 30

def create_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x1, y1 = col * RECT_SIZE, row * RECT_SIZE
            x2, y2 = x1 + RECT_SIZE, y1 + RECT_SIZE
            rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            canvas.tag_bind(rect_id, '<Button-1>', lambda event: print("aca"))

def toggle_wall(row, col):
    if maze[row][col] == 0:
        maze[row][col] = 1
        canvas.itemconfig(rectangles[row][col], fill="black")
    else:
        maze[row][col] = 0
        canvas.itemconfig(rectangles[row][col], fill="white")

root = tk.Tk()
root.title("Maze Creator")

canvas = tk.Canvas(root, width=GRID_SIZE * RECT_SIZE, height=GRID_SIZE * RECT_SIZE)
canvas.pack()

maze = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
rectangles = create_grid()

root.mainloop()


# class MazeCreator(ctk.CTk):
#
#     def __init__(self):
#         super().__init__()
#
#         self.title("Maze Solver")
#         self.resizable(False, False)
#         self.geometry("+20+20")  # top left corner
#
#         def clicked(event):
#             print('You clicked')
#
#         drawCanv = tk.Canvas(self, width=541, height=301, bd=0)
#         # drawCanv.bind('<Button>', clicked)
#
#         brick = Brick(60, 60)
#         obj1Id = drawCanv.create_line(0, 30, 100, 30, width=5)
#
#         rectangle = drawCanv.create_rectangle(brick.x, brick.y, brick.x + 60, brick.y + 60, outline='black', tags="obj1Tag")
#
#         drawCanv.tag_bind(rectangle, '<Button-1>', clicked)
#
#         # for x in range(1, 540, 60):
#         #     for y in range(1, 300, 60):
#         #         rectangle = drawCanv.create_rectangle(x, y, x + 60, y + 60, outline='black')
#         drawCanv.pack()
#
#
# if __name__ == "__main__":
#     app = MazeCreator()
#     app.mainloop()