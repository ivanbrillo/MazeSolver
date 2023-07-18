import tkinter
from abc import ABC

import customtkinter as ctk
from UI import *


def _update_size(master, size: int):
    master.update(size)


class SettingsMenu(ctk.CTkTabview, ABC):

    def __init__(self, master):
        super().__init__(master, state="disable", segmented_button_selected_color="gray30", width=240)
        self.mode = tkinter.StringVar(value="Normal Mode")
        self._menu_setup(master)

    def _menu_setup(self, master):
        self.add("CONFIGURATION")
        self.tab("CONFIGURATION").grid_columnconfigure(0, weight=1)
        self._configuration_frame(master)

    def _mode_frame_setup(self):
        mode_frame = ctk.CTkFrame(self.tab("CONFIGURATION"), border_width=2)
        mode_frame.grid(row=2, column=0, padx=(20, 20), pady=(5, 0), sticky="nwse")
        mode_frame.grid_columnconfigure(index=0, weight=1)

        self.textbox = ctk.CTkLabel(mode_frame, fg_color="gray25", corner_radius=5, text="Select the solving Alghorithm")
        self.textbox.grid(row=0, column=0,  sticky="nsew")

        available_mode = (("BFS", (10, 5)), ("DFS", (5, 5)))

        for mode in available_mode:
            button = ctk.CTkRadioButton(mode_frame, variable=self.mode, value=mode[0].strip(), text=mode[0])
            button.grid(row=available_mode.index(mode)+1, column=0, pady=mode[1])

        tkButton = ctk.CTkButton(mode_frame, fg_color="gray25", border_width=1,  text="Solve", state="disabled")
        tkButton.grid(row=3, column=0, padx=(25, 25), pady=(10, 5), sticky="nwse")


    def _configuration_frame(self, master):

        self._mode_frame_setup()

        self.textbox = ctk.CTkLabel(self, height=100, fg_color=("gray70", "gray10"), corner_radius=5, text="Select the settings and press ON")
        self.textbox.grid(row=5, column=0, pady=(10, 0), sticky="nsew")

        slider = ctk.CTkSlider(self, from_=10, to=25, number_of_steps=15, command=lambda value: _update_size(master, int(value)))
        slider.grid(row=6, column=0, pady=(10, 0), sticky="nsew")
        slider.set(10)

