from MazeCreator import *
from SettingsMenu import *
from LegendMap import *


class UI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Maze Solver")
        self.resizable(False, False)
        self.geometry("+20+20")  # top left corner

        self.menu = SettingsMenu(self)
        self.maze = MazeCreator(self, self.menu.get_brick_type())
        legend = LegendMap(self)

        self.menu.grid(row=0, column=0, padx=(10, 10), pady=(20, 10), sticky="nsew")
        self.maze.grid(row=0, column=1, padx=(10, 10), pady=(20, 10), sticky="nsew")
        legend.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="nsew", columnspan=2)


    def update(self, size) -> None:
        self.maze.create(size)

    def solve(self):
        self.menu.clear_button.configure(state="enabled")
        self.maze.solve()

    def disable_brick(self, brick_type: str):
        self.menu.disable_brick(brick_type)

    def load(self):
        self.maze.load_maze_from_file()

    def clear(self):
        self.maze.clear()

    def save(self):
        self.maze.save_maze_to_file()


if __name__ == "__main__":
    app = UI()
    app.mainloop()
