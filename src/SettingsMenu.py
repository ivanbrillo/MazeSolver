import tkinter
from abc import ABC
import customtkinter as ctk
from UI import *


class SettingsMenu(ctk.CTkFrame, ABC):

    def __init__(self, master):
        super().__init__(master, width=240, border_width=1)
        self.alghoritm = tkinter.StringVar(value="")
        self.brick_type = tkinter.StringVar(value="Wall")
        self.master = master
        self._menu_setup()

    def _menu_setup(self):
        self.grid_columnconfigure(0, weight=1)
        textbox = ctk.CTkLabel(self, fg_color="gray45", corner_radius=5, text="MENU")
        textbox.grid(row=0, column=0, sticky="nsew", pady=(0, 15))
        self._solving_frame_setup()
        self._creation_frame()
        self._saving_menu_setup()

    def _saving_menu_setup(self):
        saving_frame = ctk.CTkFrame(self, border_width=2)
        saving_frame.grid(row=12, column=0, padx=(20, 20), pady=(15, 15), sticky="nwse")
        saving_frame.grid_columnconfigure(index=0, weight=1)

        textbox = ctk.CTkLabel(saving_frame, fg_color="gray25", corner_radius=5, text="Saving Box")
        textbox.grid(row=0, column=0, sticky="nsew")

        load_button = ctk.CTkButton(saving_frame, fg_color="gray25", border_width=1, text="Load from File", command=self.master.load)
        load_button.grid(row=1, column=0, padx=(25, 25), pady=(10, 5), sticky="nwse")

        store_button = ctk.CTkButton(saving_frame, fg_color="gray25", border_width=1, text="Save to File", command=self.master.save)
        store_button.grid(row=2, column=0, padx=(25, 25), pady=(5, 10), sticky="nwse")

    def _solving_frame_setup(self):
        solving_frame = ctk.CTkFrame(self, border_width=2)
        solving_frame.grid(row=2, column=0, padx=(20, 20), pady=(5, 0), sticky="nwse")
        solving_frame.grid_columnconfigure(index=0, weight=1)

        textbox = ctk.CTkLabel(solving_frame, fg_color="gray25", corner_radius=5, text="Select the solving Alghorithm")
        textbox.grid(row=0, column=0, sticky="nsew")

        available_mode = (("BFS", (10, 5)), ("DFS", (5, 5)))
        for mode in available_mode:
            button = ctk.CTkRadioButton(solving_frame, variable=self.alghoritm, text=mode[0], border_width_unchecked=2, radiobutton_width=18,
                                        radiobutton_height=18)
            button.grid(row=available_mode.index(mode) + 1, column=0, pady=mode[1])

        tkButton = ctk.CTkButton(solving_frame, fg_color="gray25", border_width=1, text="Solve", state="disabled")
        tkButton.grid(row=3, column=0, padx=(25, 25), pady=(10, 5), sticky="nwse")

    def _creation_frame(self):

        creation_frame = ctk.CTkFrame(self, border_width=2)
        creation_frame.grid(row=6, column=0, padx=(20, 20), pady=(15, 0), sticky="nwse")
        creation_frame.grid_columnconfigure(index=0, weight=1)

        textbox = ctk.CTkLabel(creation_frame, fg_color="gray25", corner_radius=5, text="Maze Creation Box")
        textbox.grid(row=0, column=0, sticky="nsew", columnspan=2)

        self.slider = ctk.CTkSlider(creation_frame, from_=10, to=25, number_of_steps=15, command=lambda value: self._update_size(int(value)), width=80)
        self.slider.grid(row=6, column=0, pady=(10, 0), sticky="nsew", padx=(10, 0))
        self.slider.set(10)
        self.size_text = ctk.CTkLabel(creation_frame, fg_color="gray15", corner_radius=5, text="10x10", height=10)
        self.size_text.grid(row=6, column=1, sticky="nsew", padx=(0, 10), pady=(6, 0))

        available_mode = (("Wall", (10, 2)), ("StartPoint", (3, 3)), ("EndPoint", (2, 5)))
        self.button_brick_type = list()

        for mode in available_mode:
            button = ctk.CTkRadioButton(creation_frame, variable=self.brick_type, value=mode[0], text=mode[0], border_width_unchecked=2, radiobutton_width=18,
                                        radiobutton_height=18)
            button.grid(row=available_mode.index(mode) + 7, column=0, pady=mode[1], columnspan=2)
            self.button_brick_type.append(button)

        tkButton = ctk.CTkButton(creation_frame, fg_color="gray25", border_width=1, text="Clear", command=lambda: self._update_size(int(self.slider.get())))
        tkButton.grid(row=11, column=0, padx=(25, 25), pady=(10, 10), sticky="nwse", columnspan=2)

    def _update_size(self, size: int) -> None:
        self.size_text.configure(text=f"{size}x{size}")
        self.master.update(size)

    def get_brick_type(self):
        return self.brick_type

    def disable_brick(self, brick_type: str):
        for button in self.button_brick_type:
            if button.cget("text") == brick_type and brick_type != "Wall":
                button.configure(state="disabled")
                self.brick_type.set("Wall")
