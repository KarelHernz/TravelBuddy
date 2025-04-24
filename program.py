import tkinter as tk
from PIL.ImageTk import PhotoImage
from controller import *

if __name__ == "__main__":
    root = tk.Tk()
    app = Controller(root)
    imagem = PhotoImage(file = "source\img\TravelBuddy_logo.png")
    root.iconphoto(False, imagem)
    root.mainloop()