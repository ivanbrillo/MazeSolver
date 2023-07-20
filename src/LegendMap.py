import customtkinter as ctk


class LegendMap(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, border_width=2)
        textbox = ctk.CTkLabel(self, fg_color="gray25", corner_radius=5, text="Legend", width=100)
        textbox.grid(row=0, column=0, sticky="nsew", rowspan=2, padx=(0, 120))
        options = (("black", "black", "Wall"), ("green", "black", "Start"), ("red", "black", "End"), ("orange", "black", "Path"), ("gray60", "blue", "Visited"))

        for option in options:
            canvas1 = ctk.CTkCanvas(self, width=50, height=50, highlightthickness=0, bg=self.cget("fg_color")[1])
            canvas1.grid(row=0, column=1 + options.index(option), sticky="nwse", padx=(20, 20), pady=(10, 5))
            canvas1.create_rectangle(0, 0, 50, 50, fill=option[0], outline=option[1])

            text1 = ctk.CTkLabel(self, fg_color="gray15", corner_radius=5, text=option[2], height=10)
            text1.grid(row=1, column=1 + options.index(option), sticky="nsew", padx=(18, 20), pady=(2, 10))

        text1 = ctk.CTkLabel(self, fg_color="gray15", corner_radius=5, text="- Left click to add a brick\n- Right click to delete a brick")
        text1.grid(row=0, column=6, sticky="nsew", padx=(18, 20), pady=(10, 10), rowspan=2, ipadx=20)
