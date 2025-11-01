from .estrategia_cultivo import EstrategiaCultivo

class EstrategiaRiegoAutomatizado(EstrategiaCultivo):
    def ejecutar(self, cultivo):
        print(f"Riego automatizado ejecutado para el cultivo {cultivo.nombre}.")
