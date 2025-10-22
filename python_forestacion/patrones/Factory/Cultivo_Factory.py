from entidades.cultivos.Pino import Pino
from entidades.cultivos.Olivo import Olivo, TipoAceituna
from entidades.cultivos.Lechuga import Lechuga
from entidades.cultivos.Zanahoria import Zanahoria

class CultivoFactory:
    """
    Factory Pattern para crear cultivos según el tipo.
    Evita el uso de múltiples if/switch en el código principal.
    """

    @staticmethod
    def crear_cultivo(tipo: str):
        tipo = tipo.lower()
        if tipo == "pino":
            return Pino("cedro")
        elif tipo == "olivo":
            return Olivo(TipoAceituna.NEGRA)
        elif tipo == "lechuga":
            return Lechuga("Mantecosa")
        elif tipo == "zanahoria":
            return Zanahoria(True)
        else:
            raise ValueError(f"Tipo de cultivo no reconocido: {tipo}")

