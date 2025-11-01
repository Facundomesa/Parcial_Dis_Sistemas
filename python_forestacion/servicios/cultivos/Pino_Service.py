from datetime import datetime
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.servicios.cultivos.arbol_service import ArbolService

class PinoService(ArbolService):
    """
    Servicio para operaciones específicas del Pino.
    Implementa la lógica de negocio estacional del pino.
    """

    def secretar_resina(self, pino: Pino):
        print("Estoy secretando resina")

    def florecer(self, pino: Pino) -> bool:
        mes = datetime.now().month
        return 9 <= mes <= 12

    def absorver_agua(self, pino: Pino) -> int:
        mes = datetime.now().month
        agua_absorvida = 2 if mes in [1,2,3,4,9,10,11,12] else 0
        pino.set_agua(pino.get_agua() + agua_absorvida)
        return agua_absorvida

    def consumir_agua(self, pino: Pino) -> int:
        mes = datetime.now().month
        if mes in [1,2,3,4,9,10,11,12]:
            agua_consumida = 2
            self.crecer(pino, 0.10)
        elif mes in [5,6,7,8]:
            agua_consumida = 1
        else:
            agua_consumida = 0

        pino.set_agua(pino.get_agua() - agua_consumida)
        return agua_consumida

    def mostrar_datos(self, pino: Pino):
        print(f"Cultivo {type(pino).__name__}")
        print(f"Variedad: {pino.get_variedad()}")
        print(f"Altura: {pino.get_altura()}")
