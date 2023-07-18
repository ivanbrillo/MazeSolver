from MazeCreator import *
from SettingsMenu import *


class UI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Maze Solver")
        self.resizable(False, False)
        self.geometry("+20+20")  # top left corner

        self.maze = MazeCreator(self)
        menu = SettingsMenu(self)

        menu.grid(row=0, column=0, padx=(10, 10), pady=(20, 20), sticky="nsew")
        self.maze.grid(row=0, column=1, padx=(10, 10), pady=(20, 20), sticky="nsew")

    def update(self, size):
        self.maze.create(size)


if __name__ == "__main__":
    app = UI()
    app.mainloop()
