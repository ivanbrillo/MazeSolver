import tkinter
from abc import ABC

import customtkinter as ctk
from UI import *


def _update_size(master, size: int):
    master.update(size)


class SettingsMenu(ctk.CTkFrame, ABC):

    def __init__(self, master):
        super().__init__(master, width=240, border_width=1)
        self.alghoritm = tkinter.StringVar(value="")
        self.brick_type = tkinter.StringVar(value="Wall")

        self._menu_setup(master)

    def _menu_setup(self, master):
        self.grid_columnconfigure(0, weight=1)
        textbox = ctk.CTkLabel(self, fg_color="gray45", corner_radius=5, text="MENU")
        textbox.grid(row=0, column=0, sticky="nsew", pady=(0, 30))
        self._solving_frame_setup()
        self._creation_frame(master)


    def _solving_frame_setup(self):
        solving_frame = ctk.CTkFrame(self, border_width=2)
        solving_frame.grid(row=2, column=0, padx=(20, 20), pady=(5, 0), sticky="nwse")
        solving_frame.grid_columnconfigure(index=0, weight=1)

        textbox = ctk.CTkLabel(solving_frame, fg_color="gray25", corner_radius=5, text="Select the solving Alghorithm")
        textbox.grid(row=0, column=0, sticky="nsew")

        available_mode = (("BFS", (10, 5)), ("DFS", (5, 5)))
        for mode in available_mode:
            button = ctk.CTkRadioButton(solving_frame, variable=self.alghoritm, text=mode[0], border_width_unchecked=2, radiobutton_width=18, radiobutton_height=18)
            button.grid(row=available_mode.index(mode) + 1, column=0, pady=mode[1])

        tkButton = ctk.CTkButton(solving_frame, fg_color="gray25", border_width=1, text="Solve", state="disabled")
        tkButton.grid(row=3, column=0, padx=(25, 25), pady=(10, 5), sticky="nwse")

    def _creation_frame(self, master):

        creation_frame = ctk.CTkFrame(self, border_width=2)
        creation_frame.grid(row=6, column=0, padx=(20, 20), pady=(20, 0), sticky="nwse")
        creation_frame.grid_columnconfigure(index=0, weight=1)

        textbox = ctk.CTkLabel(creation_frame, fg_color="gray25", corner_radius=5, text="Maze Creation Box")
        textbox.grid(row=0, column=0, sticky="nsew", columnspan=2)

        slider = ctk.CTkSlider(creation_frame, from_=10, to=25, number_of_steps=15, command=lambda value: _update_size(master, int(value)), width=80)
        slider.grid(row=6, column=0, pady=(10, 0), sticky="nsew", padx=(10, 0))
        slider.set(10)
        textbox = ctk.CTkLabel(creation_frame, fg_color="gray15", corner_radius=5, text="10x10", height=10)
        textbox.grid(row=6, column=1, sticky="nsew", padx=(0, 10), pady=(6, 0))

        available_mode = (("Wall", (10, 2)), ("Start Point", (3, 3)), ("End Point", (2, 5)))
        for mode in available_mode:
            button = ctk.CTkRadioButton(creation_frame, variable=self.brick_type, text=mode[0], border_width_unchecked=2, radiobutton_width=18, radiobutton_height=18)
            button.grid(row=available_mode.index(mode) + 7, column=0, pady=mode[1], columnspan=2)

        tkButton = ctk.CTkButton(creation_frame, fg_color="gray25", border_width=1, text="Clear")
        tkButton.grid(row=11, column=0, padx=(25, 25), pady=(10, 10), sticky="nwse", columnspan=2)

