from .arbol import Arbol

class Pino(Arbol):
    def __init__(self, variedad: str):
        # Llama al constructor de Arbol con valores fijos:
        # agua = 2, altura = 1, superficie = 2
        super().__init__(agua=2, altura=1.0, superficie=2.0)
        self._variedad = variedad

    # Getter de la variedad
    def get_variedad(self) -> str:
        return self._variedad

    # Getter de altura para mostrar datos
    def get_altura(self) -> float:
        return self._altura

    # Getter de agua (opcional, si tu servicio lo usa)
    def get_agua(self) -> float:
        return self._agua
