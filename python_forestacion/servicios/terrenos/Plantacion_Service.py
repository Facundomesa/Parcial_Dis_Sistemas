from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.excepciones.agua_agotada_excepcion import AguaAgotadaException
from python_forestacion.excepciones.superficie_insuficiente_excepcion import SuperficieInsuficienteException


class PlantacionService:
    """
    Servicio para operaciones sobre Plantación.
    Contiene toda la lógica de negocio de plantar, regar y cosechar.
    """

    def __init__(self, cultivo_service_registry):
        self.cultivo_service_registry = cultivo_service_registry

    def plantar(self, plantacion, especie: str, cantidad: int) -> bool:
        superficie_ocupada = sum(c.get_superficie() for c in plantacion.get_cultivos_interno())
        sup_disponible = plantacion.situada_en.superficie - superficie_ocupada

        for _ in range(cantidad):
            cultivo = self.crear_cultivo(especie)
            if cultivo is None:
                raise ValueError(f"Especie de cultivo no reconocida: {especie}")

            superficie_requerida = cultivo.get_superficie()
            sup_disponible -= superficie_requerida

            if sup_disponible >= 0:
                plantacion.get_cultivos_interno().append(cultivo)
                print(f"Se plantó un/a: {cultivo.__class__.__name__}")
            else:
                raise SuperficieInsuficienteException(
                    cultivo.__class__.__name__,
                    superficie_requerida,
                    sup_disponible + superficie_requerida
                )

        return True

    def crear_cultivo(self, especie: str):
        if especie == "Pino":
            return Pino("cedro")
        elif especie == "Olivo":
            return Olivo(TipoAceituna.NEGRA)
        elif especie == "Lechuga":
            return Lechuga("Mantecosa")
        elif especie == "Zanahoria":
            return Zanahoria(True)
        else:
            return None

    def regar(self, plantacion) -> bool:
        print(f"Regando finca: {plantacion.nombre}")
        AGUA_MINIMA = 10

        for cultivo in plantacion.get_cultivos_interno():
            agua_actual = plantacion.agua_disponible
            if agua_actual > AGUA_MINIMA:
                agua_absorvida = self.absorver_agua_cultivo(cultivo)
                plantacion.agua_disponible = agua_actual - agua_absorvida
            else:
                raise AguaAgotadaException(agua_actual, AGUA_MINIMA)

        return True

    def absorver_agua_cultivo(self, cultivo) -> int:
        return self.cultivo_service_registry.absorber_agua(cultivo)

    def consumir(self, plantacion, tipo_cultivo):
        # Iterar en reversa para poder eliminar mientras iteramos
        for i in range(len(plantacion.get_cultivos_interno()) - 1, -1, -1):
            cult = plantacion.get_cultivos_interno()[i]
            if isinstance(cult, tipo_cultivo):
                del plantacion.get_cultivos_interno()[i]
        return True
