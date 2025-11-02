from abc import ABC, abstractmethod

class Cultivo(ABC):
    EDAD_MAXIMA = 20

    @abstractmethod
    def get_superficie(self) -> float:
        pass

    @abstractmethod
    def get_agua(self) -> float:
        pass

    @abstractmethod
    def set_agua(self, agua: float):
        pass

    # Método absorber_agua para riego
    def absorber_agua(self, cantidad: float):
        # Suma la cantidad de agua disponible
        self.set_agua(self.get_agua() + cantidad)


class Hortaliza(Cultivo):
    def __init__(self, agua: float, superficie: float, requiere_invernadero: bool):
        self._agua = agua
        self._superficie = superficie
        self._requiere_invernadero = requiere_invernadero
        self._altura = 0.1  # Altura por defecto para compatibilidad con mostrar_datos

    # Getters y Setters
    def get_agua(self) -> float:
        return self._agua

    def set_agua(self, agua: float):
        self._agua = agua

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float):
        self._superficie = superficie

    def get_requiere_invernadero(self) -> bool:
        return self._requiere_invernadero

    def get_altura(self) -> float:
        # Para compatibilidad con mostrar_datos
        return self._altura

