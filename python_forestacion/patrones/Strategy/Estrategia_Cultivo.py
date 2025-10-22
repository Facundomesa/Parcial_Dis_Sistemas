from abc import ABC, abstractmethod

class EstrategiaCultivo(ABC):
    """Interfaz base para estrategias de cultivo."""
    @abstractmethod
    def ejecutar(self, cultivo):
        pass
