from .arbol import Arbol
from .tipo_aceituna import TipoAceituna  

class Olivo(Arbol):
    def __init__(self, tipo: TipoAceituna):
        # Llama al constructor de Arbol con valores fijos
        # agua = 5, altura = 0.5, superficie = 3
        super().__init__(agua=5, altura=0.5, superficie=3.0)
        self._fruto = tipo

    # Getter del fruto
    def get_fruto(self) -> TipoAceituna:
        return self._fruto

    # Getter de altura para compatibilidad con mostrar_datos
    def get_altura(self) -> float:
        return self._altura

    # Getter de agua
    def get_agua(self) -> float:
        return self._agua

    # Método absorber_agua para riego
    def absorber_agua(self, cantidad: float):
        self._agua += cantidad

