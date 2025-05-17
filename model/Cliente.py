class Cliente:
    def __init__(self, id_cliente, nome, email, palavra_passe):
        self.__id_cliente = id_cliente
        self.__nome = nome
        self.__email = email
        self.__palavra_passe = palavra_passe

    def get_id_cliente(self):
        return self.__id_cliente

    def set_id_cliente(self, novo_id_cliente):
        self.__id_cliente = novo_id_cliente

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_email(self):
        return self.__email

    def set_email(self, novo_email):
        self.__email = novo_email

    def get_palavra_passe(self):
        return self.__palavra_passe

    def set_palavra_passe(self, nova_palavra_passe):
        self.__palavra_passe = nova_palavra_passe