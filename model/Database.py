import mysql.connector

class Database:
    def __init__(self):
        self.__host = "localhost"
        self.__user = "root"
        self.__password = "root"  
        self.__db = mysql.connector.connect(host=self.__host, user=self.__user, password=self.__password)
        self.__cursor = self.__db.cursor()
        
    def criar_bd(self):
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS TravelBuddy;")
        self.__cursor.execute("USE TravelBuddy;")
        
    def criar_tabela_clientes(self):
        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS Cliente(
            id_cliente INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(150) NOT NULL,
            email VARCHAR(200) NOT NULL,
            password VARCHAR(12) NOT NULL);""")

    def inserir_cliente(self, nome, email, password):
        sql = "INSERT INTO Cliente (nome, email, password) VALUES (%s, %s, %s)"
        values = (nome, email, password)
        self.__cursor.execute(sql, values)
        self.__db.commit()

    def retornar_clientes(self):
        self.__cursor.execute("SELECT * FROM Cliente")
        return self.__cursor.fetchall()