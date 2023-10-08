import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)


class AnotherFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # Create an instance of MyFrame within this frame
        my_frame = MyFrame(self, width=300, height=200)
        my_frame.grid(row=0, column=0, padx=20, pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = AnotherFrame(root)
    app.pack()
    root.mainloop()

# def create_window(tk,title):
#     window = tk.Toplevel()
#     window.title(title)
#
# def create_frame(tk,root, side="left"):
#     frame = tk.Frame(root, padx=20, pady=20)
#     frame.pack(side=side)
#     return frame
#
# def create_button(tk,parent, text, command):
#     button = tk.Button(parent, text=text, command=command)
#     button.pack()
#     return button