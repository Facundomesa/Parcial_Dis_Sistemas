from .Hortaliza import Hortaliza

class Lechuga(Hortaliza):
    def __init__(self, variedad: str):
        # Llama al constructor de Hortaliza con los valores fijos:
        # agua = 1, superficie = 0.10, requiere_invernadero = True
        super().__init__(agua=1, superficie=0.10, requiere_invernadero=True)
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad
