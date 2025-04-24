import tkinter as tk
from PIL import Image, ImageTk

class View:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("900x500")
        self.master.resizable(False, False)
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.imagem_fundo = Image.open("source\img\ceu-vermelho.jpg")
        self.imagem_fundo = self.imagem_fundo.resize((900, 500), Image.LANCZOS)
        self.imagem_fundo = ImageTk.PhotoImage(self.imagem_fundo)
        
        self.canva = tk.Canvas(self.frame, width=900, height=500)
        self.canva.pack(fill="both", expand=True)
        self.canva.create_image(0, 0, anchor = "nw", image = self.imagem_fundo)
