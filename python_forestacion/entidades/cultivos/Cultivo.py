from abc import ABC, abstractmethod

class Cultivo(ABC):
    EDAD_MAXIMA = 20  # Constante de clase

    @abstractmethod
    def get_superficie(self) -> float:
        pass

    @abstractmethod
    def get_agua(self) -> int:
        pass

    @abstractmethod
    def set_agua(self, agua: int):
        pass
