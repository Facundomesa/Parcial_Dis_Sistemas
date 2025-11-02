from .hortaliza import Hortaliza

class Lechuga(Hortaliza):
    def __init__(self, variedad: str):
        # Llama al constructor de Hortaliza con valores fijos
        # agua = 1, superficie = 0.10, requiere_invernadero = True
        super().__init__(agua=1, superficie=0.10, requiere_invernadero=True)
        self._variedad = variedad

    # Getter de la variedad
    def get_variedad(self) -> str:
        return self._variedad

    # Getter de altura (aunque sea opcional para hortalizas)
    def get_altura(self) -> float:
        # Podés devolver un valor fijo o un atributo si Hortaliza lo tiene
        return getattr(self, "_altura", 0.1)

    # Getter de agua para riego
    def get_agua(self) -> float:
        return getattr(self, "_agua", 1.0)

    # Método absorber_agua para compatibilidad con servicios de riego
    def absorber_agua(self, cantidad: float):
        # Sumar agua disponible
        self._agua = getattr(self, "_agua", 1.0) + cantidad
