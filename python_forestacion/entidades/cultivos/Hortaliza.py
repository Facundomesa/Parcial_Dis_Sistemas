from abc import ABC, abstractmethod
from .cultivo import Cultivo

class Cultivo(ABC):
    EDAD_MAXIMA = 20

    @abstractmethod
    def get_superficie(self) -> float:
        pass

    @abstractmethod
    def get_agua(self) -> int:
        pass

    @abstractmethod
    def set_agua(self, agua: int):
        pass


class Hortaliza(Cultivo):
    def __init__(self, agua: int, superficie: float, requiere_invernadero: bool):
        self._agua = agua
        self._superficie = superficie
        self._requiere_invernadero = requiere_invernadero

    # Getters y Setters
    def get_agua(self) -> int:
        return self._agua

    def set_agua(self, agua: int):
        self._agua = agua

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float):
        self._superficie = superficie

    def get_requiere_invernadero(self) -> bool:
        return self._requiere_invernadero
