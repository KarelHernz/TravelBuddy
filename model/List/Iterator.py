from abc import ABC, abstractmethod
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def rewind(self):
        pass