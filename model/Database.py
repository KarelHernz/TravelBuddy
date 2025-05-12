import mysql.connector

class Database:
    def __init__(self):
        self.__host = "localhost"
        self.__user = "root"
        self.__password = "root"  
        self.__db = mysql.connector.connect( host=self.__host, user=self.__user, password=self.__password)
        self.__cursor = self.__db.cursor()
        
    def criar_bd(self):
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS clientes;")
        self.__cursor.execute("USE clientes;")
        
    def criar_tabela_clientes(self):
        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL);""")

    def inserir_cliente(self, nome, password):
        sql = "INSERT INTO clientes (nome, password) VALUES (%s, %s)"
        values = (nome, password)
        self.__cursor.execute(sql, values)
        self.__db.commit()

    def retornar_cliente_por_nome(self, nome):
        sql = "SELECT * FROM clientes WHERE nome = %s"
        self.__cursor.execute(sql, (nome,))
        return self.__cursor.fetchone()

    def retornar_todos_clientes(self):
        self.__cursor.execute("SELECT * FROM clientes")
        return self.__cursor.fetchall()
