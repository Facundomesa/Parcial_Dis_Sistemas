from threading import Lock
from .cultivo import Cultivo

class Arbol(Cultivo):
    _cant_arboles = 0
    _lock = Lock()  # Para incrementar de forma segura en entornos concurrentes

    def __init__(self, agua: int, altura: float, superficie: float):
        with Arbol._lock:
            Arbol._cant_arboles += 1
            self._id = Arbol._cant_arboles

        self._agua = agua
        self._altura = altura
        self._superficie = superficie

    # Getters y Setters
    @property
    def id(self) -> int:
        return self._id

    def get_agua(self) -> int:
        return self._agua

    def set_agua(self, agua: int):
        self._agua = agua

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, valor: float):
        self._altura = valor

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float):
        self._superficie = superficie

    @classmethod
    def get_cant_arboles(cls) -> int:
        return cls._cant_arboles
