from datetime import datetime
from decimal import *

from model.Database import *
from model.Cliente import *
from model.ClientLinkedList import *

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
from PIL import Image, ImageTk

from amadeus import *

class View:
    def __init__(self, master):
        self.master = master

        self.database = Database()
        self.database.criar_bd()
        self.database.criar_tabela_clientes()
        
        self.clientes = ClientLinkedList()
    
        self.master.title("Login")
        self.master.geometry("700x500")
        self.master.resizable(False, False)
        self.frame_login = tk.Frame(self.master)
        self.frame_login.pack(fill="both", expand=True)

        self.imagem_fundo = self.gerar_imagem("source\img\img_atardecer.jpg", 700, 500)
        
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

        self.entry_Palavra_Passe = tk.Entry(self.frame_login, show="*", font=("Arial", 13), width=23)
        self.entry_Palavra_Passe.pack(pady=(50, 0), padx=(0, 80))

        self.imagem_olho = self.gerar_imagem("source\img\mostrar.png", 20, 20)

        self.button_mostrar = tk.Button(self.frame_login, width=32, image = self.imagem_olho, command=self.mostrar)
        self.button_mostrar.place(x = 446, y = 255)

        self.button_Login = tk.Button(self.frame_login, 
                                      text="Iniciar sessão", 
                                      background="silver", 
                                      font=("Arial", 13),
                                      width=22,
                                      command=lambda: self.login(self.entry_Email.get(), self.entry_Palavra_Passe.get()))
        self.button_Login.pack(pady=(85, 10))

        self.button_Registar = tk.Button(self.frame_login, 
                                         text="Registar conta", 
                                         background="silver", 
                                         font=("Arial", 13),
                                         width=22,
                                         command=self.abrir_janela_registar)
        self.button_Registar.pack()

    def gerar_imagem(self, imagem, ancho, altura):
        imagem_fundo = Image.open(imagem).resize((ancho, altura), Image.LANCZOS)
        return ImageTk.PhotoImage(imagem_fundo)

    def mostrar(self):
        self.mostrar_palavra_passe(self.entry_Palavra_Passe)
    
    def obter_clientes(self):
        clientes = self.database.retornar_clientes()
        for i in clientes:
            self.clientes.insert_last(Cliente(i[0], i[1], i[2], i[3]))

    def abrir_janela_registar(self):
        self.janela_registar()

    def janela_registar(self):
        top_level = tk.Toplevel(self.master)
        top_level.resizable(False, False)
        top_level.geometry("800x615")
        image = tk.PhotoImage(file = "source\img\TravelBuddy_logo.png")
        top_level.iconphoto(False, image)
        top_level.title("Registro")
        frame_registar = tk.Frame(top_level)
        frame_registar.pack(fill="both", expand=True)

        imagem_fundo = self.gerar_imagem("source\img\img_amanecer.jpg", 800, 615)
        
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

        imagem_olho1 =  self.gerar_imagem("source\img\mostrar.png", 20, 20)
    
        button_mostrar1 = tk.Button(frame_registar, width=32, image = imagem_olho1, command=lambda: self.mostrar_palavra_passe(entry_palavra_passe))
        button_mostrar1.place(x = 495, y = 328)

        label5 = tk.Label(frame_registar, text="Confirmar palavra-passe", bg="#484678", foreground="white", font=("Arial", 13))
        label5.place(x=254, y=369)

        entry_confirmar = tk.Entry(frame_registar, show="*", font=("Arial", 13), width=23)
        entry_confirmar.pack(pady=(50, 0), padx=(0, 80))

        imagem_olho2 =  self.gerar_imagem("source\img\mostrar.png", 20, 20)
        
        button_mostrar2 = tk.Button(frame_registar, width=32, image = imagem_olho2, command=lambda: self.mostrar_palavra_passe(entry_confirmar))
        button_mostrar2.place(x = 495, y = 402)

        button_registar = tk.Button(frame_registar, 
                                    text = "Registar", 
                                    background = "silver", 
                                    width = 22,
                                    font = ("Arial", 13),
                                    command = lambda:self.registar_cliente(entry_nome.get(), 
                                                                           entry_email.get(), 
                                                                           entry_palavra_passe.get(), 
                                                                           entry_confirmar.get()))
        button_registar.pack(pady=(50, 10))

        button_voltar = tk.Button(frame_registar,
                                  text="Voltar",
                                  background="silver",
                                  font=("Arial", 13),
                                  width=22,
                                  command = top_level.destroy)
        button_voltar.pack()

    def mostrar_palavra_passe(self, entry):
        if entry["show"] == "*":
            entry.configure(show="")
        else:
            entry.configure(show="*") 

    def login(self, email, password):
        self.obter_clientes()
        if email and password:
            posicao = self.clientes.find_cliente(email, password)
            if posicao == -1:
                messagebox.showerror("Erro", "Email ou password incorretos")
            else:
                self.menu()
        else:
             messagebox.showinfo("Atenção", "Insira os dados dentro dos campos de texto")

    def registar_cliente(self, nome, email, password, password_repetida):
        self.obter_clientes()
        if email and password:
            posicao = self.clientes.find_email(email)
            if posicao != -1: 
                messagebox.showerror("Erro", "Email existente")
            else:
                if password != password_repetida:
                    messagebox.showerror("Erro", "As palavras-passe não coincidem")
                else:
                    self.database.inserir_cliente(nome, email, password)
                    self.clientes.insert_last(Cliente(nome, email, password))
                    messagebox.showinfo("Sucesso", f"{nome}, foi registado com sucesso!")
    
    def menu(self):
        self.amadeus = Client(
            client_id='bIowr7VJfkAORoRA4Hl5KhBfGiiogEmq',
            client_secret='UzFP1EGwkUfu82aE'
        )

        self.top_level_menu = tk.Toplevel(self.master)
        self.top_level_menu.resizable(False, False)
        self.top_level_menu.geometry("700x550")
        image = tk.PhotoImage(file = "source\img\TravelBuddy_logo.png")
        self.top_level_menu.iconphoto(False, image)
        self.top_level_menu.title("Menu")
        
        frame_menu = tk.Frame(self.top_level_menu, width=700, height=550)
        frame_menu.pack(fill="both",expand=True)

        imagem_fundo = self.gerar_imagem("source\img\img_dia.jpg", 700, 550)
        
        label_fundo = tk.Label(frame_menu, image=imagem_fundo)
        label_fundo.place(relwidth=1, relheight=1)

        imagem_viagem = self.gerar_imagem("source\img\img_viagens.png", 130, 85)
        button_viagens = tk.Button(frame_menu, 
                                   image=imagem_viagem, 
                                   font=("Arial", 13),
                                   command=self.abrir_viagens)
        button_viagens.pack(fill="both", 
                            expand=True, 
                            padx=80, 
                            pady=(80, 0))

        imagem_turismo = self.gerar_imagem("source\img\img_turismo.png", 220, 85)
        button_lugares_turisticos = tk.Button(frame_menu, 
                                              image=imagem_turismo, 
                                              font=("Arial", 13),
                                              command=self.abrir_lugares_turisticos)
        button_lugares_turisticos.pack(fill="both", 
                                       expand=True, 
                                       padx=80, 
                                       pady=(40,0))

        imagem_calculadora = self.gerar_imagem("source\img\img_calculadora.png", 135, 85)
        button_caluladora = tk.Button(frame_menu, 
                                      image=imagem_calculadora,
                                      font=("Arial", 13),
                                      command=self.abrir_calculadora)
        
        button_caluladora.pack(fill="both", 
                               expand=True,
                               padx=80, 
                               pady=(40, 80))
        
    def abrir_viagens(self):
        self.janela_viagens()
        self.top_level_menu.destroy()

    def abrir_lugares_turisticos(self):
        self.janela_lugares_turisticos()
        self.top_level_menu.destroy()

    def abrir_calculadora(self):
        self.janela_calculadora()
        self.top_level_menu.destroy()

    def abrir_menu_desde_viagens(self):
        self.top_level_viagens.destroy()
        self.menu()

    def abrir_menu_desde_turisticos(self):
        self.top_level_lturistico.destroy()
        self.menu()

    def abrir_menu_desde_calculadora(self):
        self.top_level_calculadora.destroy()
        self.menu()

    def janela_viagens(self):
        self.top_level_viagens = tk.Toplevel(self.master)
        image = tk.PhotoImage(file = "source\img\TravelBuddy_logo.png")
        self.top_level_viagens.geometry("1300x750")
        self.top_level_viagens.resizable(False, False)
        self.top_level_viagens.iconphoto(False, image)
        self.top_level_viagens.title("Viagens")
        
        frame_viagens = tk.Frame(self.top_level_viagens)
        frame_viagens.pack(expand=True, fill="both")

        label_origem = tk.Label(frame_viagens, text="Origem", font=("Arial", 13))
        label_origem.place(x=40, y = 37)

        label_obrigatorio1 = tk.Label(frame_viagens, text="*", foreground="red", font=("Arial", 13))
        label_obrigatorio1.place(x=100, y = 37)

        combobox_origem = ttk.Combobox(frame_viagens, width = 28, font=("Arial", 13))
        combobox_origem.place(x=43, y = 67)
        combobox_origem.bind('<KeyRelease>', self.retornar_paises)

        label_destino = tk.Label(frame_viagens, text="Destino", font=("Arial", 13))
        label_destino.place(x=410, y = 37)

        label_obrigatorio2 = tk.Label(frame_viagens, text="*", foreground="red", font=("Arial", 13))
        label_obrigatorio2.place(x=470, y = 37)

        self.combobox_destino = ttk.Combobox(frame_viagens, width = 28, font=("Arial", 13))
        self.combobox_destino.place(x=414, y = 67)
        self.combobox_destino.bind('<KeyRelease>', self.retornar_paises)

        label_companhia_aerea = tk.Label(frame_viagens, text="Companhia Aérea", font=("Arial", 13))
        label_companhia_aerea.place(x=716, y = 37)

        combobox_companhia_aerea = ttk.Combobox(frame_viagens, width = 28, font=("Arial", 13))
        combobox_companhia_aerea.place(x=720, y = 67)
        combobox_companhia_aerea.bind('<KeyRelease>', self.retornar_companhias)

        label_nadultos = tk.Label(frame_viagens, text="Nº adultos", font=("Arial", 13))
        label_nadultos.place(x=40, y = 107)

        label_obrigatorio3 = tk.Label(frame_viagens, text="*", foreground="red", font=("Arial", 13))
        label_obrigatorio3.place(x=120, y = 107)

        spin_nadultos = tk.Spinbox(frame_viagens, width=12, from_=0, to=50, state="readonly", font=("Arial", 13))
        spin_nadultos.place(x=43, y = 137)

        label_data = tk.Label(frame_viagens, text="Data saída", font=("Arial", 13))
        label_data.place(x=410, y = 107)
                         
        data = datetime.now()
        data_saida = DateEntry(frame_viagens, 
                              selectmode="day", 
                              year=data.year, 
                              month=data.month, 
                              day=data.day,
                              firstweekday = "sunday",
                              mindate = datetime.today(),
                              date_pattern = "dd/mm/yyyy",
                              font=("Arial", 13))
        data_saida.place(x=414, y = 137)

        label_preco = tk.Label(frame_viagens, text="Preço", font=("Arial", 13))
        label_preco.place(x=716, y = 107)

        spin_preco = tk.Spinbox(frame_viagens, 
                                from_=0, 
                                to=99999, 
                                validate="key", 
                                validatecommand=(self.master.register(self.validar), "%P"), 
                                font=("Arial", 13))
        spin_preco.place(x=720, y = 137)
        spin_preco.bind("<Key>", self.apagar_cero)

        label_resultados = tk.Label(frame_viagens, text="Resultados: 0", font=("Arial", 13))
        label_resultados.place(x=40, y = 215)

        button_procurar = tk.Button(frame_viagens, 
                                    text="Procurar", 
                                    font=("Arial", 13), 
                                    command=lambda:self.procurar_voos(
                                        combobox_origem.get(),
                                        self.combobox_destino.get(),
                                        data_saida.get_date(),
                                        spin_nadultos.get(),
                                        combobox_companhia_aerea.get(),
                                        spin_preco.get()))
        button_procurar.place(x=1000, y = 200)

        button_exportar = tk.Button(frame_viagens, text="Exportar", font=("Arial", 13))
        button_exportar.place(x=1105, y = 200)

        button_voltar = tk.Button(frame_viagens, text="Voltar", font=("Arial", 13), command=self.abrir_menu_desde_viagens)
        button_voltar.place(x=1205, y = 200)

        scrollbar = tk.Scrollbar(frame_viagens, orient=tk.HORIZONTAL)
        scrollbar.pack(side = tk.BOTTOM, fill=tk.X)
        
        self.tree_view_viagens = ttk.Treeview(frame_viagens, 
                                         columns=("Voo", "Companhia", "Pais", "Cidade", "Duração", "Classe", "Data", "Preço"), 
                                         show="headings",
                                         xscrollcommand = scrollbar.set)
    	
        self.tree_view_viagens.heading("Voo", text="Voo")
        self.tree_view_viagens.heading("Companhia", text="Companhia")
        self.tree_view_viagens.heading("Pais", text="Pais")
        self.tree_view_viagens.heading("Cidade", text="Cidade")
        self.tree_view_viagens.heading("Duração", text="Duração")
        self.tree_view_viagens.heading("Classe", text="Classe")
        self.tree_view_viagens.heading("Data", text="Data")
        self.tree_view_viagens.heading("Preço", text="Preço")
        self.tree_view_viagens.pack(padx=40, pady=(250, 10), fill="both", expand=True)

        scrollbar.config(command = self.tree_view_viagens.xview)

    def validar(self, texto):
        if not texto:
            return True

        try:
            numero = float(texto)
        except ValueError:
            return False

        if '.' in texto:
            partes = texto.split('.', 1)
            parte_decimal = partes[1]
            if len(parte_decimal) > 2:
                return False
        
        if numero > 99999:
            return False

        return True
    
    def apagar_cero(self, event):
        spin = event.widget
        texto = spin.get()

        if texto == "0":
            spin.delete(0, tk.END)
        
    def procurar_voos(self, origem, destino, data_saida, nadultos, companhia, preco):
        lista_voos = []
        data_saida = data_saida.strftime("%Y-%m-%d")
        origem = origem.split(" -", 1)[0]
        destino = destino.split(" -", 1)[0]
        preco = self.set_decimal(preco)
        try:
            response_voos = self.amadeus.shopping.flight_offers_search.get(
                originLocationCode=origem,
                destinationLocationCode=destino,
                departureDate=data_saida,
                adults=nadultos)  
            
            texto = self.combobox_destino.get().split(" - ")[1]
            pais = texto.split(", ", 1)[0]
            cidade = texto.split(", ", 1)[1]
            
            for i in response_voos.data:
                print(i ['itineraries'][0]['segments'][0]['departure']['iataCode'])
                break
                #for j in i["validatingAirlineCodes"]:
                iataCode = i['']
                companhia = self.retornar_comanhia_por_iataCode(iataCode)

                lista_voos.append((i["carrierCode"], 
                                  companhia,
                                  pais,
                                  cidade, 
                                  i["itineraries"][0]["duration"].split("PT"),
                                  i["fareDetailsBySegment"][0]["cabin"],
                                  i["itineraries"][0]["duration"].split("PT"), 
                                  i["price"]["total"] + "€"))
                
            self.tree_view_viagens["values"] = lista_voos
                   
        except ResponseError as error:
            messagebox.showerror("Erro", error)
        except Exception as error:
            messagebox.showerror("Erro", error)

    def retornar_paises(self, event):
        combobox = event.widget
        texto = combobox.get()

        if len(texto) < 3:
            return
        
        try:
            lista_paises = []
            response_cidade = self.amadeus.reference_data.locations.get(keyword=texto, subType="CITY")
            for i in response_cidade.data:
                cod_iata = i["iataCode"]
                pais = i["address"]["countryName"]
                cidade = i["name"]
                lista_paises.append(f"{cod_iata} - {pais}, {cidade}")

            combobox["values"] = lista_paises
            combobox.event_generate("<Down>") 
        except ResponseError as error:
            messagebox.showerror("Erro", error)
        except Exception as error:
            messagebox.showerror("Erro", error)

    def retornar_companhias(self, event):
        combobox = event.widget
        texto = combobox.get()
    
        if len(texto) < 2:
            return
        
        try:
            lista_companhias = []
            response_companhias = self.amadeus.reference_data.airlines.get(airlineCodes = texto)
            for i in response_companhias.data:
                cod_iata = i["icaoCode"]
                nome = i["businessName"]
                lista_companhias.append(f"{cod_iata} - {nome}")

            combobox["values"] = lista_companhias
            combobox.event_generate("<Down>") 
        except ResponseError as error:
            messagebox.showerror("Erro", error)
        except Exception as error:
            messagebox.showerror("Erro", error)

    def retornar_comanhia_por_iataCode(self, iataCode):
        try:
            response_companhias = self.amadeus.reference_data.airlines.get(airlineCodes = iataCode)
            for i in response_companhias.data:
                return i["businessName"]
        except ResponseError as error:
            messagebox.showerror("Erro", error)
        except Exception as error:
            messagebox.showerror("Erro", error)

    def janela_lugares_turisticos(self):
        self.top_level_lturistico = tk.Toplevel(self.master)
        image = tk.PhotoImage(file = "source\img\TravelBuddy_logo.png")
        self.top_level_lturistico.iconphoto(False, image)
        self.top_level_lturistico.title("Lugares Turísticos")
        
        frame_turismo = tk.Frame(self.top_level_lturistico, width=700, height=550)
        frame_turismo.pack()

    def janela_calculadora(self):
        self.top_level_calculadora = tk.Toplevel(self.master)
        image = tk.PhotoImage(file = "source\img\TravelBuddy_logo.png")
        self.top_level_calculadora.geometry("700x600")
        self.top_level_calculadora.resizable(False, False)
        self.top_level_calculadora.iconphoto(False, image)
        self.top_level_calculadora.title("Calculadora")
        
        frame_calculadora = tk.Frame(self.top_level_calculadora, width=700, height=550)
        frame_calculadora.pack()

        label_voo = tk.Label(frame_calculadora, text="Voo", font=("Arial", 13))
        label_voo.pack(pady=(35, 8), padx=(0, 175))

        spin_voo = tk.Spinbox(frame_calculadora, 
                              from_=0.00, 
                              to=99999.99,
                              validate="key", 
                              validatecommand=(self.master.register(self.validar), "%P"),
                              font=("Arial", 13))
        spin_voo.pack(pady=8)
        spin_voo.bind("<Key>", self.apagar_cero)

        label_alojamento = tk.Label(frame_calculadora, text="Alojamento", font=("Arial", 13))
        label_alojamento.pack(pady=8, padx=(0, 125))

        spin_alojamento = tk.Spinbox(frame_calculadora, 
                                     from_=0.00, 
                                     to=99999.99,
                                     validate="key", 
                                     validatecommand=(self.master.register(self.validar), "%P"),
                                     font=("Arial", 13))
        spin_alojamento.pack(pady=8)
        spin_alojamento.bind("<Key>", self.apagar_cero)

        label_atividades = tk.Label(frame_calculadora, text="Atividades", font=("Arial", 13))
        label_atividades.pack(pady=8, padx=(0, 125))
        
        spin_atividade = tk.Spinbox(frame_calculadora, 
                                    from_=0.00, 
                                    to=99999.99,
                                    validate="key", 
                                    validatecommand=(self.master.register(self.validar), "%P"),
                                    font=("Arial", 13))
        spin_atividade.pack(pady=8)
        spin_atividade.bind("<Key>", self.apagar_cero)

        label_outros = tk.Label(frame_calculadora, text="Outros", font=("Arial", 13))
        label_outros.pack(pady=8, padx=(0, 150))

        spin_outros = tk.Spinbox(frame_calculadora, 
                                 from_=0.00, 
                                 to=99999.99,
                                 validate="key", 
                                 validatecommand=(self.master.register(self.validar), "%P"),
                                 font=("Arial", 13))
        spin_outros.pack(pady=8)
        spin_outros.bind("<Key>", self.apagar_cero)

        label_resultado = tk.Label(frame_calculadora, text="Total: 0.00€", font=("Arial", 13))
        label_resultado.pack(pady=8)

        button_calcular = tk.Button(frame_calculadora, 
                                    text="Calcular",
                                    font=("Arial", 13),
                                    command=lambda:self.calcular_valores(spin_voo.get(),
                                                                spin_alojamento.get(),
                                                                spin_atividade.get(),
                                                                spin_outros.get(),
                                                                label_resultado))
        button_calcular.pack(pady=8)

        button_exportar = tk.Button(frame_calculadora, text="Exportar", font=("Arial", 13))
        button_exportar.pack(pady=8)

        button_voltar = tk.Button(frame_calculadora, text="Voltar", font=("Arial", 13), command=self.abrir_menu_desde_calculadora)
        button_voltar.pack(pady=8)

    def calcular_valores(self, valor_voo,
                         valor_alojamento,
                         valor_atividades,
                         valor_outros,
                         label_resultado):
        
        valor_voo = self.set_decimal(valor_voo)
        valor_alojamento = self.set_decimal(valor_alojamento)
        valor_atividades = self.set_decimal(valor_atividades)
        valor_outros = self.set_decimal(valor_outros)

        resultado = Decimal(valor_voo) + Decimal(valor_alojamento) + Decimal(valor_atividades) + Decimal(valor_outros)
        label_resultado["text"] = f"Total: {resultado}€"

    def set_decimal(self, numero):
        if numero == "":
            return 0.00
        return numero