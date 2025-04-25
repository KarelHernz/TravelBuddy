import tkinter as tk
from PIL import Image, ImageTk

class View:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("900x500")
        self.master.resizable(False, False)
        self.frame_login = tk.Frame(self.master)
        self.frame_login.pack(fill="both", expand=True)

        self.imagem_fundo = Image.open("source\img\img_atardecer.jpg")
        self.imagem_fundo = self.imagem_fundo.resize((900, 500), Image.LANCZOS)
        self.imagem_fundo = ImageTk.PhotoImage(self.imagem_fundo)
        
        self.label_fundo = tk.Label(self.frame_login, image=self.imagem_fundo)
        self.label_fundo.place(relwidth=1, relheight=1)

        self.label_bemvindo = tk.Label(self.frame_login, text="Bem-vindo ao TravelBuddy!", font=("Arial", 18))
        self.label_bemvindo.pack()

        self.label1 = tk.Label(self.frame_login, text="Email", font=("Arial", 13))
        self.label1.pack()

        self.entry_Email = tk.Entry(self.frame_login, font=("Arial", 13))
        self.entry_Email.pack()

        self.label2 = tk.Label(self.frame_login, text="Palavra-passe", font=("Arial", 13))
        self.label2.pack()

        self.entry_Palavra_Passe = tk.Entry(self.frame_login, show="*", font=("Arial", 13))
        self.entry_Palavra_Passe.pack()

        self.button_Login = tk.Button(self.frame_login, 
                                      text="Inisiar sessão", 
                                      background="silver", 
                                      font=("Arial", 13))
        self.button_Login.pack()

        self.button_Registar = tk.Button(self.frame_login, 
                                         text="Registar conta", 
                                         background="silver", 
                                         font=("Arial", 13), 
                                         command=self.abrir_janela_registar)
        self.button_Registar.pack()

    def abrir_janela_registar(self):
        self.janela_registar()

    def janela_registar(self):
        top_level = tk.Toplevel(self.master)
        top_level.resizable(False, False)
        top_level.geometry("650x475")
        image = tk.PhotoImage(file = "source\img\TravelBuddy_logo.png")
        top_level.iconphoto(False, image)
        frame_registar = tk.Frame(top_level)
        frame_registar.pack(fill="both", expand=True)

        imagem_fundo = Image.open("source\img\img_amanecer.jfif")
        imagem_fundo = imagem_fundo.resize((650, 475), Image.LANCZOS)
        imagem_fundo = ImageTk.PhotoImage(imagem_fundo)
        
        label_fundo = tk.Label(frame_registar, image=imagem_fundo)
        label_fundo.place(relwidth=1, relheight=1)

        label1 = tk.Label(frame_registar, text="Registar conta", font=("Arial", 18))
        label1.grid(row=0, column=0, columnspan=2)

        label2 = tk.Label(frame_registar, text="Nome", font=("Arial", 13))
        label2.grid(row=1, columnspan=2)

        entry_nome = tk.Entry(frame_registar, font=("Arial", 13))
        entry_nome.grid(row=2, columnspan=2)

        label3 = tk.Label(frame_registar, text="Email", font=("Arial", 13))
        label3.grid(row=3, columnspan=2)

        entry_email = tk.Entry(frame_registar, font=("Arial", 13))
        entry_email.grid(row=4, columnspan=2)

        label4 = tk.Label(frame_registar, text="Palavra-passe", font=("Arial", 13))
        label4.grid(row=5, column=0)

        entry_palavra_passe = tk.Entry(frame_registar, font=("Arial", 13))
        entry_palavra_passe.grid(row=6, column=0)

        button_mostrar1 = tk.Button(frame_registar, text="mostrar")
        button_mostrar1.grid(row=6, column=1)

        label5 = tk.Label(frame_registar, text="Confirmar palavra-passe", font=("Arial", 13))
        label5.grid(row=7, column=0)

        entry_confirmar = tk.Entry(frame_registar, font=("Arial", 13))
        entry_confirmar.grid(row=8, column=0)

        button_mostrar2 = tk.Button(frame_registar, text="mostrar")
        button_mostrar2.grid(row=8, column=1)

        button_registar = tk.Button(frame_registar, 
                                    text="Registar", 
                                    background="silver", 
                                    font=("Arial", 13))
        button_registar.grid(row=9, columnspan=2)

        button_voltar = tk.Button(frame_registar,
                                  text="Voltar",
                                  background="silver",
                                  font=("Arial", 13),
                                  command = top_level.destroy)
        button_voltar.grid(row=10, columnspan=2)