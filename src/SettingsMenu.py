import tkinter
from abc import ABC

import customtkinter as ctk
from UI import *


def _update_size(master, size: int):
    master.update(size)


class SettingsMenu(ctk.CTkFrame, ABC):

    def __init__(self, master):
        super().__init__(master, width=240, border_width=1)
        self.mode = tkinter.StringVar(value="Normal Mode")
        self._menu_setup(master)

    def _menu_setup(self, master):
        self.grid_columnconfigure(0, weight=1)

        textbox = ctk.CTkLabel(self, fg_color="gray45", corner_radius=5, text="MENU")
        textbox.grid(row=0, column=0, sticky="nsew", pady=(0, 30))

        # self.grid_rowconfigure(0, weight=1)

        self._configuration_frame(master)

    def _mode_frame_setup(self):
        mode_frame = ctk.CTkFrame(self, border_width=2)
        mode_frame.grid(row=2, column=0, padx=(20, 20), pady=(5, 0), sticky="nwse")
        mode_frame.grid_columnconfigure(index=0, weight=1)

        textbox = ctk.CTkLabel(mode_frame, fg_color="gray25", corner_radius=5, text="Select the solving Alghorithm")
        textbox.grid(row=0, column=0, sticky="nsew")

        available_mode = (("BFS", (10, 5)), ("DFS", (5, 5)))

        for mode in available_mode:
            button = ctk.CTkRadioButton(mode_frame, variable=self.mode, value=mode[0].strip(), text=mode[0])
            button.grid(row=available_mode.index(mode) + 1, column=0, pady=mode[1])

        tkButton = ctk.CTkButton(mode_frame, fg_color="gray25", border_width=1, text="Solve", state="disabled")
        tkButton.grid(row=3, column=0, padx=(25, 25), pady=(10, 5), sticky="nwse")

    def _configuration_frame(self, master):
        self._mode_frame_setup()

        slider = ctk.CTkSlider(self, from_=10, to=25, number_of_steps=15, command=lambda value: _update_size(master, int(value)))
        slider.grid(row=6, column=0, pady=(10, 0), sticky="nsew", padx=(20, 20))
        slider.set(10)
