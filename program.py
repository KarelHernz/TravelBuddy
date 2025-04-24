import tkinter as tk
from model.Controller import *
from view import *

if __name__ == "__main__":
    root = tk.Tk()
    app = Controller(root)
    root.title("Login")
    root.mainloop()