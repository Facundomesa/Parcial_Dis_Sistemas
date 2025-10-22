from .Arbol import Arbol

class Pino(Arbol):
    def __init__(self, variedad: str):
        # Llama al constructor de Arbol con valores fijos:
        # agua = 2, altura = 1, superficie = 2
        super().__init__(agua=2, altura=1.0, superficie=2.0)
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad
