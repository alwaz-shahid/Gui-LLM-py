import customtkinter
from widgets.molecules import Frame

class Chat_Label(Frame):
    def __init__(self, master, label_text=None, **kwargs):
        super().__init__(master, **kwargs)

        # Add a border to the frame
        self.configure(border_width=2, border_color="gray50")

        # Create the label if label_text is provided
        if label_text is not None:
            self.label = customtkinter.CTkLabel(self, text=label_text)
            self.label.grid(row=0, column=0, padx=10)
