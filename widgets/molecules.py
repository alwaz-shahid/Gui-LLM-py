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

class Chat_Label(Frame):
    def __init__(self, master, label_text=None, **kwargs):
        super().__init__(master, **kwargs)

        # Add a border to the frame
        self.configure(border_width=2, border_color="gray50")

        # Create the label if label_text is provided
        if label_text is not None:
            self.label = customtkinter.CTkLabel(self, text=label_text)
            self.label.grid(row=0, column=0, padx=10)

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, tab_names, tab_widgets, **kwargs):
        super().__init__(master, **kwargs)

        self.tabs = {}  # Dictionary to store the tab frames

        # create tabs
        for name in tab_names:
            self.add(name)
            self.tabs[name] = self.tab(name)  # Store the tab frames in the dictionary

        # add widgets on tabs
        for i, widget in enumerate(tab_widgets):
            widget.master = self.tabs[tab_names[i]]  # Use the stored tab frames
            widget.grid(row=0, column=0, padx=20, pady=10)
# class MyTabView(customtkinter.CTkTabview):
#     def __init__(self, master, tab_names, tab_widgets, **kwargs):
#         super().__init__(master, **kwargs)
#
#         self.tabs = {}  # Dictionary to store the tab frames
#
#         # create tabs
#         for name in tab_names:
#             self.add(name)
#             self.tabs[name] = self.tab(name)  # Store the tab frames in the dictionary
#
#         # add widgets on tabs
#         for i, widget in enumerate(tab_widgets):
#             widget.master = self.tabs[tab_names[i]]  # Use the stored tab frames
#             widget.grid(row=0, column=0, padx=20, pady=10)

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





# class MyTabView(customtkinter.CTkTabview):
#     def __init__(self, master, tab_names, tab_widgets, **kwargs):
#         super().__init__(master, **kwargs)
#
#         # create tabs
#         for name in tab_names:
#             self.add(name)
#
#         # add widgets on tabs
#         for i, widget in enumerate(tab_widgets):
#             widget.master = self.tab(tab_names[i])
#             widget.grid(row=0, column=0, padx=20, pady=10)


# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()
#
#         tab_names = ["Tab 1", "Tab 2"]
#         tab_widgets = [customtkinter.CTkLabel(), customtkinter.CTkButton(text="Click me!")]
#         self.tab_view = MyTabView(master=self, tab_names=tab_names, tab_widgets=tab_widgets)
#         self.tab_view.grid(row=0, column=0, padx=20, pady=20)
#
#
# app = App()
# app.mainloop()