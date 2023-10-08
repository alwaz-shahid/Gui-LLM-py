import tkinter as tk
import customtkinter
from widgets.molecules import ScrollFrame,Frame

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")
        self.configure_grid_layout()

        self.create_sidebar_frame()
        self.create_entry_and_button()
        self.create_chat_frame()

    def configure_grid_layout(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 4), weight=1)

    def create_sidebar_frame(self):
        sidebar_frame = ScrollFrame(self, width=300)
        sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew", padx=(5, 5), pady=(5, 5))
        sidebar_frame.grid_rowconfigure(4, weight=1)

    def create_entry_and_button(self):
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=5, column=1, columnspan=4, padx=(5, 0), pady=(5, 5), sticky="nsew")
        # Create the button
        entry_button = customtkinter.CTkButton(master=self, fg_color="#1e38bd", border_width=2,
                                               text_color=("gray10", "#DCE4EE"), text="Submit",
                                               command=self.send_message)
        entry_button.grid(row=5, column=3, padx=(0, 5), pady=(5, 5), sticky="nsew")

    def create_chat_frame(self):
        chat_frame = ScrollFrame(self, width=600,border_width=2, border_color="gray50")
        chat_frame.grid(row=0, column=1, rowspan=5, columnspan=4,sticky="nsew", padx=(5, 0), pady=(5, 5))
        chat_frame.grid_rowconfigure(4, weight=1)

        # Create a list to keep track of message frames
        self.message_frames = []

    def send_message(self):
        user_message = self.entry.get()

        if user_message:
            # Create a message frame for the user message
            user_message_frame = Frame(self)
            user_message_label = customtkinter.CTkLabel(user_message_frame, text=f"User: {user_message}")
            user_message_label.pack()
            user_message_frame.grid(row=len(self.message_frames), column=0, sticky="w")

            # Add the message frame to the chat frame
            self.message_frames.append(user_message_frame)

            # Clear the entry after sending
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    app = App()
    app.mainloop()
