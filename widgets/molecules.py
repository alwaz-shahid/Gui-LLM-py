import customtkinter


class ScrollFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, label_text=None, **kwargs):
        super().__init__(master, **kwargs)

        # Create the label if label_text is provided
        if label_text is not None:
            self.label = customtkinter.CTkLabel(self, text=label_text)
            self.label.grid(row=0, column=0, padx=20)

class Frame(customtkinter.CTkFrame):
    def __init__(self, master, label_text=None, **kwargs):
        super().__init__(master, **kwargs)

        # Create the label if label_text is provided
        if label_text is not None:
            self.label = customtkinter.CTkLabel(self, text=label_text)
            self.label.grid(row=0, column=0, padx=10)


class MessageFrame(Frame):
    def __init__(self, master, text, sender):
        super().__init__(master, border_width=2, border_color="gray50")
        self.label = customtkinter.CTkLabel(self, text=f"{sender}: {text}")

        if sender == "User":
            # Align user messages to the right
            self.label.grid(row=0, column=0, sticky="e")
        else:
            # Align bot messages to the left
            self.label.grid(row=0, column=0, sticky="w")

# class MessageFrame(Frame):
#     def __init__(self, master, text, sender):
#         super().__init__(master, border_width=2, border_color="gray50")
#         self.label = customtkinter.CTkLabel(self, text=f"{sender}: {text}")
#         self.label.grid(row=0, column=0, sticky="w")


# class MessageFrame(Frame):
#     def __init__(self, master, text, sender):
#         super().__init__(master)
#         self.label = customtkinter.CTkLabel(self, text=f"{sender}: {text}")
#         self.label.grid(row=0, column=0, sticky="w")