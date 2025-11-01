from .estrategia_cultivo import EstrategiaCultivo

class EstrategiaFertilizacionManual(EstrategiaCultivo):
    def ejecutar(self, cultivo):
        print(f"Fertilización manual aplicada al cultivo {cultivo.nombre}.")
