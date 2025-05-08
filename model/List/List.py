from abc import ABC, abstractmethod
class List(ABC):
    @abstractmethod
    def is_empty(self):
        pass
    
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def get_first(self):
        pass

    @abstractmethod
    def get_last(self):
        pass

    @abstractmethod
    def get(self, posicao):
        pass

    @abstractmethod
    def find(self, elemento):
        pass

    @abstractmethod
    def insert_first(self, elemento):
        pass

    @abstractmethod
    def insert_last(self, elemento):
        pass

    @abstractmethod
    def insert(self, elemento, posicao):
        pass

    @abstractmethod
    def remove_first(self):
        pass

    @abstractmethod
    def remove_last(self):
        pass

    @abstractmethod
    def remove(self, posicao):
        pass

    @abstractmethod
    def make_empty(self):
        pass

    @abstractmethod
    def iterator(self):
        pass