from MazeCreator import *
from SettingsMenu import *


class UI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Maze Solver")
        self.resizable(False, False)
        self.geometry("+20+20")  # top left corner

        self.menu = SettingsMenu(self)
        self.maze = MazeCreator(self, self.menu.get_brick_type())

        self.menu.grid(row=0, column=0, padx=(10, 10), pady=(20, 20), sticky="nsew")
        self.maze.grid(row=0, column=1, padx=(10, 10), pady=(20, 20), sticky="nsew")

    def update(self, size) -> None:
        self.maze.create(size)

    def disable_brick(self, brick_type: str):
        self.menu.disable_brick(brick_type)

    def load(self):
        self.maze.load_maze_from_file()

    def save(self):
        self.maze.save_maze_to_file()


if __name__ == "__main__":
    app = UI()
    app.mainloop()
