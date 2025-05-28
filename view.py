import datetime
from decimal import *

from model.Database import *
from model.Cliente import *
from model.ClientLinkedList import *

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
from PIL import Image, ImageTk
from fpdf import FPDF

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
        try:
            clientes = self.database.retornar_clientes()
            for i in clientes:
                self.clientes.insert_last(Cliente(i[0], i[1], i[2], i[3]))
        except Exception as error:
            messagebox.showerror("Error", error)

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
        try:
            self.obter_clientes()
            if email and password:
                posicao = self.clientes.find_cliente(email, password)
                if posicao == -1:
                    messagebox.showerror("Erro", "Email ou password incorretos")
                else:
                    self.menu()
            else:
                messagebox.showinfo("Atenção", "Insira os dados dentro dos campos de texto")
        except Exception as error:
            messagebox.showerror("Error", error)

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
        self.lista_voos = []

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

        combobox_destino = ttk.Combobox(frame_viagens, width = 28, font=("Arial", 13))
        combobox_destino.place(x=414, y = 67)
        combobox_destino.bind('<KeyRelease>', self.retornar_paises)

        label_companhia_aerea = tk.Label(frame_viagens, text="Companhia Aérea", font=("Arial", 13))
        label_companhia_aerea.place(x=716, y = 37)

        combobox_companhia_aerea = ttk.Combobox(frame_viagens, width = 28, font=("Arial", 13))
        combobox_companhia_aerea.place(x=720, y = 67)
        combobox_companhia_aerea.bind('<KeyRelease>', self.retornar_companhias)

        label_nadultos = tk.Label(frame_viagens, text="Nº adultos", font=("Arial", 13))
        label_nadultos.place(x=40, y = 107)

        spin_nadultos = tk.Spinbox(frame_viagens, width=12, from_=1, to=50, state="readonly", font=("Arial", 13))
        spin_nadultos.place(x=43, y = 137)

        label_data = tk.Label(frame_viagens, text="Data saída", font=("Arial", 13))
        label_data.place(x=410, y = 107)
                         
        hoje = datetime.date.today()
        amanha = hoje + datetime.timedelta(days=1)
        data_saida = DateEntry(frame_viagens, 
                              selectmode="day", 
                              year=hoje.year, 
                              month=hoje.month, 
                              day=hoje.day,
                              firstweekday = "sunday",
                              mindate = amanha,
                              date_pattern = "dd/mm/yyyy",
                              font=("Arial", 13))
        data_saida.place(x=414, y = 137)

        label_preco = tk.Label(frame_viagens, text="Preço", font=("Arial", 13))
        label_preco.place(x=716, y = 107)

        spin_preco = tk.Spinbox(frame_viagens, 
                                from_=0, 
                                to=99999, 
                                validate="key", 
                                validatecommand=(self.master.register(self.validar_preco), "%P"), 
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
                                        combobox_destino.get(),
                                        data_saida.get_date(),
                                        spin_nadultos.get(),
                                        combobox_companhia_aerea.get(),
                                        spin_preco.get()))
        button_procurar.place(x=1000, y = 200)

        button_exportar = tk.Button(frame_viagens, text="Exportar", font=("Arial", 13), command=self.generar_pdf_voos)
        button_exportar.place(x=1105, y = 200)

        button_voltar = tk.Button(frame_viagens, text="Voltar", font=("Arial", 13), command=self.abrir_menu_desde_viagens)
        button_voltar.place(x=1205, y = 200)

        scrollbar = tk.Scrollbar(frame_viagens, orient=tk.HORIZONTAL)
        scrollbar.pack(side = tk.BOTTOM, fill=tk.X)
        
        self.tree_view_viagens = ttk.Treeview(frame_viagens, 
                                         columns=("Companhia", "Duração", "Classe", "Data", "Preço"), 
                                         show="headings",
                                         xscrollcommand = scrollbar.set)
    	
        self.tree_view_viagens.heading("Companhia", text="Companhia")
        self.tree_view_viagens.heading("Duração", text="Duração")
        self.tree_view_viagens.heading("Classe", text="Classe")
        self.tree_view_viagens.heading("Data", text="Data")
        self.tree_view_viagens.heading("Preço", text="Preço (EUR)")

        self.tree_view_viagens.pack(padx=40, pady=(250, 10), fill="both", expand=True)

        scrollbar.config(command = self.tree_view_viagens.xview)

    def validar_preco(self, texto):
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
        
    def procurar_voos(self, origem_voo, destino_voo, data_saida, nadultos, companhia, preco_maximo):
        if origem_voo and destino_voo:
            self.lista_voos = []
            data_saida = data_saida.strftime("%Y-%m-%d")
            origem = origem_voo.split(" -", 1)[0]
            destino = destino_voo.split(" -", 1)[0]
            iataCode_Companhia = companhia.split(" - ")[0]
            preco_maximo = Decimal(preco_maximo)
            preco_voo = 0
            try:
                response_voos = self.amadeus.shopping.flight_offers_search.get(
                    originLocationCode=origem,
                    destinationLocationCode=destino,
                    departureDate=data_saida,
                    adults=nadultos)  
                
                texto = destino_voo.split(" - ")[1]
                pais = texto.split(", ", 1)[0]
                cidade = texto.split(", ", 1)[1]
                
                if len(response_voos.data) == 0:
                    messagebox.showinfo("Informação", f"Não há voos disponiveis para {pais}, {cidade}")

                j = 0
                for i in response_voos.data:
                    if j == 25:
                        break

                    preco_voo = Decimal(i["price"]["total"])
                    if preco_maximo != 0:
                        if preco_voo > preco_maximo:
                            continue

                    if companhia:
                        iataCode = i["itineraries"][0]["segments"][0]["carrierCode"]
                        if iataCode != iataCode_Companhia:
                            continue

                    codigo_voo = i['itineraries'][0]["segments"][0]['carrierCode']
                    duracao = i["itineraries"][0]["duration"].split("PT")[1]
                    classe = i["travelerPricings"][0]["fareDetailsBySegment"][0]["cabin"]
                    data_voo = i["itineraries"][0]["segments"][0]["departure"]["at"]
                    data_voo = f"{data_voo.split("T")[0]} {data_voo.split("T")[1]}H"
                    self.lista_voos.append((codigo_voo, 
                                    duracao,
                                    classe,
                                    data_voo, 
                                    preco_voo))
                    j += 1
                
                for items in self.tree_view_viagens.get_children():
                    self.tree_view_viagens.delete(items)

                for voo in self.lista_voos:
                    self.tree_view_viagens.insert("", "end", values=voo)
                   
            except ResponseError as error:
                messagebox.showerror("Erro", error)
            except Exception as error:
                messagebox.showerror("Erro", error)
        else:
            messagebox.showerror("Error", "Há campos que não estão preenchidos")

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
                cod_iata = i["iataCode"]
                nome = i["businessName"]
                lista_companhias.append(f"{cod_iata} - {nome}")

            combobox["values"] = lista_companhias
            combobox.event_generate("<Down>") 
        except ResponseError as error:
            messagebox.showerror("Erro", error)
        except Exception as error:
            messagebox.showerror("Erro", error)

    def generar_pdf_voos(self):
        if not len(self.lista_voos):
            messagebox.showinfo("Informação", "Não há dados para exportar")
            return
        
        try:
            pdf = FPDF(orientation="L")
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            pdf.cell(0, 7, txt="Lista de voos", align="C", ln=True)
            lista_cabecalho = ["Companhia", "Duração", "Classe", "Data", "Preço (EUR)"]

            for coluna in lista_cabecalho:
                    pdf.cell(55, 10, coluna, border=1, align="C")
            pdf.ln(10)
                
            for linha in self.lista_voos:
                for coluna in linha:
                    pdf.cell(55, 10, str(coluna), border=1, align="L")
                pdf.ln(10)
            
            pdf.output("lista_voos.pdf")
            messagebox.showinfo("Informação", "O seu pdf foi gerado com sucesso")
        except Exception as error:
            messagebox.showerror("Error", error)

    def janela_lugares_turisticos(self):
        self.lista_atividades = []
        self.lista_atividades_traduzidas = {"Passeios turísticos": "SIGHTSEEING",
                                            "Cultura": "CULTURE",
                                            "Comida": "FOOD",
                                            "Bebidas": "DRINK",
                                            "Compras": "SHOPPING",
                                            "Vida noturna": "NIGHTLIFE",
                                            "Atividades ao ar livre": "OUTDOORS",
                                            "Excursões": "TOURS",
                                            "Parques temáticos": "THEME_PARKS",
                                            "Entretenimento": "ENTERTAINMENT"}
        
        self.top_level_lturistico = tk.Toplevel(self.master)
        image = tk.PhotoImage(file = "source\img\TravelBuddy_logo.png")
        self.top_level_lturistico.geometry("1300x750")
        self.top_level_lturistico.resizable(False, False)
        self.top_level_lturistico.iconphoto(False, image)
        self.top_level_lturistico.title("Lugares Turísticos")
        
        frame_turismo = tk.Frame(self.top_level_lturistico, width=700, height=550)
        frame_turismo.pack(expand=True, fill="both")

        label_cidade = tk.Label(frame_turismo, text="Cidade", font=("Arial", 13))
        label_cidade.place(x=40, y = 37)

        label_obrigatorio = tk.Label(frame_turismo, text="*", foreground="red", font=("Arial", 13))
        label_obrigatorio.place(x=95, y = 37)

        entry_cidade = ttk.Entry(frame_turismo, width = 28, font=("Arial", 13))
        entry_cidade.place(x=43, y = 67)

        label_atividades = tk.Label(frame_turismo, text="Atividades", font=("Arial", 13))
        label_atividades.place(x=408, y = 37)

        combobox_atividades = ttk.Combobox(frame_turismo, width = 28, font=("Arial", 13))
        combobox_atividades.place(x=410, y = 67)
        combobox_atividades["values"] = self.retornar_atividades()

        label_preco = tk.Label(frame_turismo, text="Preço", font=("Arial", 13))
        label_preco.place(x=40, y = 107)

        spin_preco = tk.Spinbox(frame_turismo, 
                                from_=0, 
                                to=99999, 
                                validate="key", 
                                validatecommand=(self.master.register(self.validar_preco), "%P"), 
                                font=("Arial", 13))
        spin_preco.place(x=43, y = 137)
        spin_preco.bind("<Key>", self.apagar_cero)

        label_ordenar = tk.Label(frame_turismo, text="Ordenar preço", font=("Arial", 13))
        label_ordenar.place(x=410, y = 107)

        combo_ordenar = ttk.Combobox(frame_turismo, state="readonly", font=("Arial", 13))
        combo_ordenar.place(x=408, y = 137)  
        combo_ordenar["values"] = ["Ascendente", "Descendente"]
       
        label_resultados = tk.Label(frame_turismo, text="Resultados: 0", font=("Arial", 13))
        label_resultados.place(x=40, y = 215)

        button_procurar = tk.Button(frame_turismo, 
                                    text="Procurar", 
                                    font=("Arial", 13),
                                    command=lambda:self.procurar_lugares_turisticos(
                                        entry_cidade.get(),
                                        combobox_atividades.get(),
                                        spin_preco.get(),
                                        combo_ordenar.get()))
        button_procurar.place(x=1000, y = 200)

        button_exportar = tk.Button(frame_turismo, 
                                    text="Exportar", 
                                    font=("Arial", 13))
        button_exportar.place(x=1105, y = 200)

        button_voltar = tk.Button(frame_turismo, text="Voltar", font=("Arial", 13), command=self.abrir_menu_desde_turisticos)
        button_voltar.place(x=1205, y = 200)

        scrollbar = tk.Scrollbar(frame_turismo, orient=tk.HORIZONTAL)
        scrollbar.pack(side = tk.BOTTOM, fill=tk.X)
        
        self.tree_view_atividades = ttk.Treeview(frame_turismo, 
                                         columns=("Nome", "Descrição", "Preço", "Moeda", "Imagem"), 
                                         show="headings",
                                         xscrollcommand = scrollbar.set)
    	
        self.tree_view_atividades.heading("Nome", text="Nome")
        self.tree_view_atividades.heading("Descrição", text="Descrição")
        self.tree_view_atividades.heading("Preço", text="Preço")
        self.tree_view_atividades.heading("Moeda", text="Moeda")
        self.tree_view_atividades.heading("Imagem", text="Imagem")

        self.tree_view_atividades.pack(padx=40, pady=(250, 10), fill="both", expand=True)

        scrollbar.config(command = self.tree_view_atividades.xview)

    def procurar_lugares_turisticos(self, cidade, tipo_atividade, preco_maximo, ordenacao):
        if cidade:
            self.lista_atividades = []
            latitude, longitude = self.retornar_coordenadas(cidade)
            preco_maximo = Decimal(preco_maximo)
            preco_atividade = 0
            try:
                if tipo_atividade:
                    atividade = self.lista_atividades_traduzidas[tipo_atividade]
                    response_lugares = self.amadeus.shopping.activities.get(latitude=latitude, longitude=longitude, category = atividade, radius=15)
                else:
                    response_lugares = self.amadeus.shopping.activities.get(latitude=latitude, longitude=longitude, radius=15)

                if len(response_lugares.data) == 0:
                    messagebox.showinfo("Informação", f"Não há lugares turísticos na localização inserida")

                j = 0
                for i in response_lugares.data:
                    if j == 20:
                        break
                        
                    preco_atividade = i.get("price", {}).get("amount")

                    if preco_atividade is None:
                        preco_atividade = "Preço indisponível"
                    else:
                        preco_atividade = Decimal(preco_atividade)
                        if preco_atividade == 0:
                            preco_atividade = "Grátis"

                        if preco_maximo != 0 and preco_atividade != "Grátis":
                            if preco_atividade > preco_maximo:
                                continue

                    nome = i["name"]
                    descricao = i.get("description", "Sem descrição")
                    moeda = i.get("price", {}).get("currencyCode")
                    if moeda is None:
                        moeda = "Moeda indisponível"
                        
                    url_foto = i.get("pictures", [])
                    if len(url_foto) == 0:
                        url_foto = "Sem imagem"
                    else:
                        url_foto = url_foto[0]
                    

                    self.lista_atividades.append((nome, descricao, preco_atividade, moeda, url_foto))
                    j += 1
                
                if ordenacao:
                    if ordenacao == "Ascendente":
                        pass
                    else:
                        pass

                for items in self.tree_view_atividades.get_children():
                    self.tree_view_atividades.delete(items)

                for atividade in self.lista_atividades:
                    self.tree_view_atividades.insert("", "end", values=atividade)

            except ResponseError as error:
                messagebox.showerror("Erro", error)
            except Exception as error:
                messagebox.showerror("Erro", error)

    def retornar_coordenadas(self, cidade):
        try:
            response_localizacoes = self.amadeus.reference_data.locations.get(keyword=cidade, subType="CITY")
            for i in response_localizacoes.data:
                latidude =  i['geoCode']['latitude']
                longitude = i['geoCode']['longitude']
                break
            return latidude, longitude
        except ResponseError as error:
            messagebox.showerror("Erro", error)
        except Exception as error:
            messagebox.showerror("Erro", error)

    def retornar_atividades(self):
        lista_atividades = []
        for i in self.lista_atividades_traduzidas:
            lista_atividades.append(i)
        return lista_atividades

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
                              validatecommand=(self.master.register(self.validar_preco), "%P"),
                              font=("Arial", 13))
        spin_voo.pack(pady=8)
        spin_voo.bind("<Key>", self.apagar_cero)

        label_alojamento = tk.Label(frame_calculadora, text="Alojamento", font=("Arial", 13))
        label_alojamento.pack(pady=8, padx=(0, 125))

        spin_alojamento = tk.Spinbox(frame_calculadora, 
                                     from_=0.00, 
                                     to=99999.99,
                                     validate="key", 
                                     validatecommand=(self.master.register(self.validar_preco), "%P"),
                                     font=("Arial", 13))
        spin_alojamento.pack(pady=8)
        spin_alojamento.bind("<Key>", self.apagar_cero)

        label_atividades = tk.Label(frame_calculadora, text="Atividades", font=("Arial", 13))
        label_atividades.pack(pady=8, padx=(0, 125))
        
        spin_atividade = tk.Spinbox(frame_calculadora, 
                                    from_=0.00, 
                                    to=99999.99,
                                    validate="key", 
                                    validatecommand=(self.master.register(self.validar_preco), "%P"),
                                    font=("Arial", 13))
        spin_atividade.pack(pady=8)
        spin_atividade.bind("<Key>", self.apagar_cero)

        label_outros = tk.Label(frame_calculadora, text="Outros", font=("Arial", 13))
        label_outros.pack(pady=8, padx=(0, 150))

        spin_outros = tk.Spinbox(frame_calculadora, 
                                 from_=0.00, 
                                 to=99999.99,
                                 validate="key", 
                                 validatecommand=(self.master.register(self.validar_preco), "%P"),
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

        button_exportar = tk.Button(frame_calculadora, 
                                    text="Exportar", 
                                    font=("Arial", 13),
                                    command=lambda:self.generar_pdf_calculadora(spin_voo.get(),
                                                                spin_alojamento.get(),
                                                                spin_atividade.get(),
                                                                spin_outros.get()))
        button_exportar.pack(pady=8)

        button_voltar = tk.Button(frame_calculadora, text="Voltar", font=("Arial", 13), command=self.abrir_menu_desde_calculadora)
        button_voltar.pack(pady=8)

    def calcular_valores(self, valor_voo, valor_alojamento, valor_atividades, valor_outros, label_resultado):
        resultado = self.calcular_total(valor_voo, valor_alojamento, valor_atividades, valor_outros)
        label_resultado["text"] = resultado

    def generar_pdf_calculadora(self, valor_voo, valor_alojamento, valor_atividades, valor_outros):
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=13)

            pdf.cell(0, 7, txt="TravellBuddy", align="C", ln=True)

            resultado = self.calcular_total(valor_voo, valor_alojamento, valor_atividades, valor_outros)
            pdf.multi_cell(w=10000, h=10, txt=f"Valor Voo: {valor_voo}")
            pdf.multi_cell(w=10000, h=10, txt=f"Valor Alojamento: {valor_alojamento}")
            pdf.multi_cell(w=10000, h=10, txt=f"Valor Atividades: {valor_atividades}")
            pdf.multi_cell(w=10000, h=10, txt=f"Valor Outros: {valor_outros}")
            pdf.multi_cell(w=10000, h=10, txt=resultado)
            
            pdf.output("calculos_viagem.pdf")
            messagebox.showinfo("Informação", "O seu pdf foi gerado com sucesso")
        except Exception as error:
            messagebox.showerror("Error", error)

    def calcular_total(self, valor_voo, valor_alojamento, valor_atividades, valor_outros):
        if valor_voo == "":
            valor_voo = 0.00

        if valor_alojamento == "":
            valor_alojamento = 0.00

        if valor_atividades == "":
            valor_atividades = 0.00

        if valor_outros == "":
            valor_outros = 0.00

        resultado = Decimal(valor_voo) + Decimal(valor_alojamento) + Decimal(valor_atividades) + Decimal(valor_outros)
        return f"Total: {resultado}"