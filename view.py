import tkinter as tk
from PIL import Image, ImageTk

class View:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("700x500")
        self.master.resizable(False, False)
        self.frame_login = tk.Frame(self.master)
        self.frame_login.pack(fill="both", expand=True)

        self.imagem_fundo = Image.open("source\img\img_atardecer.jpg").resize((700, 500), Image.LANCZOS)
        self.imagem_fundo = ImageTk.PhotoImage(self.imagem_fundo)
        
        self.label_fundo = tk.Label(self.frame_login, image=self.imagem_fundo)
        self.label_fundo.place(relwidth=1, relheight=1)

        self.label_bemvindo = tk.Label(self.frame_login, 
                                       text="Bem-vindo ao TravelBuddy!", 
                                       bg="#483634", 
                                       foreground="white",
                                       font=("Arial", 18))
        self.label_bemvindo.pack(pady=70)

        self.label1 = tk.Label(self.frame_login, 
                               text="Email", 
                               bg="#483634", 
                               foreground="white", 
                               font=("Arial", 13))
        self.label1.place(x=203, y=153)

        self.entry_Email = tk.Entry(self.frame_login, font=("Arial", 13), width=32)
        self.entry_Email.pack(pady=(10, 0))

        self.label2 = tk.Label(self.frame_login, 
                               text="Palavra-passe",  
                               bg="#483634", 
                               foreground="white", 
                               font=("Arial", 13))
        self.label2.place(x=203, y=225)

        self.entry_Palavra_Passe = tk.Entry(self.frame_login, show="*", font=("Arial", 13), width=32)
        self.entry_Palavra_Passe.pack(pady=(50, 0))

        imagem_olho = Image.open("source\img\mostrar.png").resize((20, 20), Image.LANCZOS)
        imagem_olho = ImageTk.PhotoImage(imagem_olho)
        self.button_mostrar = tk.Button(self.frame_login, image = imagem_olho, command=self.mostrar)
        self.button_mostrar.place(x = 250, y = 328)

        self.button_Login = tk.Button(self.frame_login, 
                                      text="Iniciar sessão", 
                                      background="silver", 
                                      font=("Arial", 13),
                                      width=22)
        self.button_Login.pack(pady=(85, 10))

        self.button_Registar = tk.Button(self.frame_login, 
                                         text="Registar conta", 
                                         background="silver", 
                                         font=("Arial", 13),
                                         width=22,
                                         command=self.abrir_janela_registar)
        self.button_Registar.pack()

    def abrir_janela_registar(self):
        self.janela_registar()

    def mostrar(self):
        self.mostrar_palavra_passe(self.button_mostrar, self.entry_Palavra_Passe)

    def janela_registar(self):
        top_level = tk.Toplevel(self.master)
        top_level.resizable(False, False)
        top_level.geometry("800x615")
        image = tk.PhotoImage(file = "source\img\TravelBuddy_logo.png")
        top_level.iconphoto(False, image)
        frame_registar = tk.Frame(top_level)
        frame_registar.pack(fill="both", expand=True)

        imagem_fundo = Image.open("source\img\img_amanecer.jpg").resize((800, 615), Image.LANCZOS)
        imagem_fundo = ImageTk.PhotoImage(imagem_fundo)
        
        label_fundo = tk.Label(frame_registar, image=imagem_fundo)
        label_fundo.place(relwidth=1, relheight=1)

        label1 = tk.Label(frame_registar, text="Registar conta", bg="#524B79", foreground="white", font=("Arial", 18))
        label1.pack(pady=70)

        label2 = tk.Label(frame_registar, text="Nome", bg="#635682", foreground="white", font=("Arial", 13))
        label2.place(x=254, y=153)

        entry_nome = tk.Entry(frame_registar, font=("Arial", 13), width=32)
        entry_nome.pack(pady=(10, 0))

        label3 = tk.Label(frame_registar, text="Email", bg="#484678", foreground="white", font=("Arial", 13))
        label3.place(x=254, y=225)

        entry_email = tk.Entry(frame_registar, font=("Arial", 13), width=32)
        entry_email.pack(pady=(50, 0))

        label4 = tk.Label(frame_registar, text="Palavra-passe", bg="#484678", foreground="white", font=("Arial", 13))
        label4.place(x=254, y=297)

        entry_palavra_passe = tk.Entry(frame_registar, show="*", font=("Arial", 13), width=23)
        entry_palavra_passe.pack(pady=(50, 0), padx=(0, 80))

        imagem_olho1 =  Image.open("source\img\mostrar.png").resize((20, 20), Image.LANCZOS)
        imagem_olho1 = ImageTk.PhotoImage(imagem_olho1)
        button_mostrar1 = tk.Button(frame_registar, image = imagem_olho1, command=lambda: mostrar_palavra_passe(button_mostrar1, entry_palavra_passe))
        button_mostrar1.place(x = 495, y = 328)

        label5 = tk.Label(frame_registar, text="Confirmar palavra-passe", bg="#484678", foreground="white", font=("Arial", 13))
        label5.place(x=254, y=369)

        entry_confirmar = tk.Entry(frame_registar, show="*", font=("Arial", 13), width=23)
        entry_confirmar.pack(pady=(50, 0), padx=(0, 80))

        imagem_olho2 =  Image.open("source\img\mostrar.png").resize((20, 20), Image.LANCZOS)
        imagem_olho2 = ImageTk.PhotoImage(imagem_olho2)
        button_mostrar2 = tk.Button(frame_registar, image = imagem_olho2, command=lambda: mostrar_palavra_passe(button_mostrar2, entry_confirmar))
        button_mostrar2.place(x = 495, y = 402)

        button_registar = tk.Button(frame_registar, 
                                    text="Registar", 
                                    background="silver", 
                                    width=22,
                                    font=("Arial", 13))
        button_registar.pack(pady=(50, 10))

        button_voltar = tk.Button(frame_registar,
                                  text="Voltar",
                                  background="silver",
                                  font=("Arial", 13),
                                  width=22,
                                  command = top_level.destroy)
        button_voltar.pack()

        def mostrar_palavra_passe(botao, entry):
            if entry["show"] == "*":
                imagem_olho = Image.open("source\img\img_nao_mostrar.png").resize((20, 20), Image.LANCZOS)
                entry.configure(show="")
            else:
                imagem_olho = Image.open("source\img\mostrar.png").resize((20, 20), Image.LANCZOS)
                entry.configure(show="*")

            imagem_olho = ImageTk.PhotoImage(imagem_olho)
            botao.configure(image=imagem_olho)
            