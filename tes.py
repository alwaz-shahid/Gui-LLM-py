import tkinter as tk
import customtkinter
from widgets.molecules import ScrollFrame, MessageFrame, Frame

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.chat_frame = None
        self.entry = None
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")
        self.configure_grid_layout()

        self.create_sidebar_frame()
        self.create_input_section()
        self.create_chat_frame()

    def configure_grid_layout(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3, 4, 5), weight=0)
        self.grid_rowconfigure((0, 1, 2, 4, 5, 6, 7), weight=1)

    def create_sidebar_frame(self):
        sidebar_frame = ScrollFrame(self, width=300)
        sidebar_frame.grid(row=0, column=0, rowspan=9, sticky="nsew", padx=(5, 5), pady=(5, 5))
        sidebar_frame.grid_rowconfigure(4, weight=1)

    def create_input_section(self):
        input_frame = Frame(self)
        input_frame.grid(row=8, column=1, columnspan=5, padx=(10, 0), pady=(10, 10), sticky="nsew")
        # Configure input_frame to expand with the grid cell
        input_frame.grid_rowconfigure(0, weight=1)

        input_frame.grid_columnconfigure((0,1,2,3,4), weight=1)

        # Create the input entry
        self.entry = customtkinter.CTkEntry(input_frame, placeholder_text="Enter Your Prompt Here")
        self.entry.grid(row=0, column=0, columnspan=4, padx=(5, 0), pady=(5, 5), sticky="nsew")

        # Create the Submit button
        entry_button = customtkinter.CTkButton(input_frame, fg_color="#15288a",width=5,
                                               text_color=("gray10", "#DCE4EE"), text="Submit",
                                               command=self.send_message)
        entry_button.grid(row=0, column=4, padx=(0, 10), pady=(10, 10), sticky="nsew")

        # # Create the Audio button
        # audio_button = customtkinter.CTkButton(input_frame, fg_color="#1e38bd", border_width=2,width=5,
        #                                        text_color=("blue10", "#DCE4EE"), text="Audio", )
        # audio_button.grid(row=1, column=4, padx=(0, 10), pady=(10, 10), sticky="nsew")

    def create_chat_frame(self):
        self.chat_frame = ScrollFrame(self, width=600, border_width=2, border_color="gray50")
        self.chat_frame.grid(row=0, column=1, rowspan=8, columnspan=4, sticky="nsew", padx=(5, 0), pady=(5, 5))
        self.chat_frame.grid_rowconfigure(4, weight=1)

        # Create a list to keep track of message frames
        self.message_frames = []

    def add_message(self, text, sender):
        # Create a message frame for the message
        message_frame = MessageFrame(self.chat_frame, text, sender)

        message_frame.grid(row=len(self.message_frames), column=0, sticky="w", columnspan=4, padx=(5, 0), pady=(5, 5))

        # Add the message frame to the chat frame
        self.message_frames.append(message_frame)

        # Clear the entry after sending
        self.entry.delete(0, tk.END)

    def handle_bot_response(self, user_message):
        # Simulate a bot response (you can replace this with actual bot logic)
        bot_response = "Hello, I'm a bot!"
        self.add_message(bot_response, "Bot")

    def send_message(self):
        user_message = self.entry.get()

        if user_message:
            # Add the user message
            self.add_message(user_message, "User")

            # Handle bot response
            self.handle_bot_response(user_message)


if __name__ == "__main__":
    app = App()
    app.mainloop()
