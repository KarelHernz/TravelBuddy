class Companhia:
    def __init__(self, id_companhia, iata_code, nome):
        self.__id_companhia = id_companhia
        self.__iata_code = iata_code
        self.__nome = nome

    def get_id_companhia(self):
        return self.__id_companhia

    def set_id_companhia(self, novo_id_companhia):
        self.__id_companhia = novo_id_companhia

    def get_iata_code(self):
        return self.__iata_code

    def set_iata_code(self, iata_code):
        self.__iata_code = iata_code

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome