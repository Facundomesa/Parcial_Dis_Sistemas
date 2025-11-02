from datetime import datetime
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.servicios.cultivos.arbol_service import ArbolService

class OlivoService(ArbolService):
    """
    Servicio para operaciones específicas del Olivo.
    Implementa la lógica de negocio estacional del olivo.
    """

    def cosechar(self, olivo: Olivo) -> bool:
        mes = datetime.now().month
        if 5 <= mes <= 7:
            print("Se ha cosechado este olivo")
            return True
        return False

    def florecer(self, olivo: Olivo) -> bool:
        mes = datetime.now().month
        return 9 <= mes <= 12

    def absorber_agua(self, olivo: Olivo) -> int:
        """Corrige typo y usa el método absorber_agua del cultivo"""
        mes = datetime.now().month
        agua_absorbida = 1 if mes in [1,2,3,4,9,10,11,12] else 0
        olivo.absorber_agua(agua_absorbida)
        return agua_absorbida

    def consumir_agua(self, olivo: Olivo) -> int:
        mes = datetime.now().month
        if mes in [1,2,3,4,9,10,11,12]:
            agua_consumida = 2
            self.crecer(olivo, 0.01)
        elif mes in [5,6,7,8]:
            agua_consumida = 1
        else:
            agua_consumida = 0

        olivo.set_agua(olivo.get_agua() - agua_consumida)
        return agua_consumida

    def mostrar_datos(self, olivo: Olivo):
        print(f"Cultivo {type(olivo).__name__}")
        print(f"Fruto: {olivo.get_fruto().name}")
        print(f"Altura: {olivo.get_altura()}")
