from .Arbol import Arbol
from .Tipo_Aceituna import TipoAceituna  

class Olivo(Arbol):
    def __init__(self, tipo: TipoAceituna):
        # Llama al constructor de Arbol con los valores fijos:
        # agua = 5, altura = 0.5, superficie = 3
        super().__init__(agua=5, altura=0.5, superficie=3.0)
        self._fruto = tipo

    def get_fruto(self) -> TipoAceituna:
        return self._fruto
