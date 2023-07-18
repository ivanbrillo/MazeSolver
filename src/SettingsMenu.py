import tkinter
from abc import ABC

import customtkinter as ctk
from UI import *


class SettingsMenu(ctk.CTkTabview, ABC):

    def __init__(self, master):
        super().__init__(master, state="disable", segmented_button_selected_color="chartreuse4", width=240)
        self.mode = tkinter.StringVar(value="Normal Mode")

        self._menu_setup()

    def _menu_setup(self):
        self.add("CONFIGURATION")
        self.tab("CONFIGURATION").grid_columnconfigure(0, weight=1)
        self._configuration_frame()

    def _mode_frame_setup(self):
        mode_frame = ctk.CTkFrame(self.tab("CONFIGURATION"))
        mode_frame.grid(row=2, column=0, padx=(20, 20), pady=(5, 0), sticky="nwse")
        # mode_frame.grid_columnconfigure(0, weight=1)

        available_mode = (("BFS", (10, 5)), ("DFS", (5, 5)))

        for mode in available_mode:
            ctk.CTkRadioButton(mode_frame, variable=self.mode, value=mode[0].strip(), text=mode[0]).grid(row=available_mode.index(mode),
                                                                                                         column=0, pady=mode[1],
                                                                                                         padx=10)

    def _appearance_frame_setup(self):
        appearance_frame = ctk.CTkFrame(self)
        appearance_frame.grid(row=7, column=0, pady=(6, 0), sticky="nsew")
        appearance_frame.grid_columnconfigure(0, weight=1)
        option = ctk.CTkOptionMenu(appearance_frame, values=["System", "Dark", "Light"], command=lambda app_mode: ctk.set_appearance_mode(app_mode))
        option.grid(pady=(8, 8))

    def _configuration_frame(self):
        self.option_COM = ctk.CTkOptionMenu(self.tab("CONFIGURATION"))
        self.option_COM.grid(row=0, column=0, padx=20, pady=(15, 5))

        self._mode_frame_setup()

        tkButton = ctk.CTkButton(self.tab("CONFIGURATION"), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Solve")
        tkButton.grid(row=3, column=0, padx=(20, 20), pady=(15, 5), sticky="nwse")

        self.textbox = ctk.CTkLabel(self, height=100, fg_color=("gray70", "gray10"), corner_radius=5, text="Select the settings and press ON")
        self.textbox.grid(row=5, column=0, pady=(10, 0), sticky="nsew")

        self._appearance_frame_setup()
