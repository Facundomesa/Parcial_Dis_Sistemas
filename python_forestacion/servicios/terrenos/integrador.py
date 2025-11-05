"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\terrenos
Fecha: 2025-11-05 10:21:19
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\terrenos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\terrenos\plantacion_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\terrenos\registro_forestal_service.py
# ================================================================================

from typing import Optional, List, Dict, Any
import os
import pickle
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.excepciones.persistencia_excepcion import PersistenciaException
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry


class RegistroForestalService:
    """
    Servicio para operaciones sobre RegistroForestal.
    Contiene lógica de persistencia y visualización de datos.
    """

    def __init__(self, cultivo_service_registry: CultivoServiceRegistry):
        self.cultivo_service_registry = cultivo_service_registry

    def mostrar_datos(self, registro: RegistroForestal):
        print("REGISTRO FORESTAL")
        print("=================")
        print(f"Padrón:      {registro.id_padron}")
        print(f"Propietario: {registro.propietario}")
        print(f"Avalúo:      {registro.avaluo}")
        print(f"Domicilio:   {registro.tierra.domicilio}")
        print(f"Superficie:  {registro.tierra.superficie}")
        print(f"Cantidad de cultivos plantados: {len(registro.plantacion.cultivos)}")
        print("Listado de Cultivos plantados")
        print("____________________________")

        for cultivo in registro.plantacion.cultivos:
            self._mostrar_datos_cultivo(cultivo)

    def _mostrar_datos_cultivo(self, cultivo: Cultivo):
        """Delega mostrar datos al servicio específico del cultivo usando el registry."""
        self.cultivo_service_registry.mostrar_datos(cultivo)

    def persistir(self, registro: RegistroForestal):
        """Persiste el registro forestal en disco usando pickle."""
        nombre_archivo = f"data/{registro.propietario}.pkl"

        try:
            os.makedirs("data", exist_ok=True)
            with open(nombre_archivo, "wb") as f:
                pickle.dump(registro, f)

            print(f"Persistencia exitosa para: {registro.propietario}")

        except Exception as e:
            raise PersistenciaException(f"Error al persistir {nombre_archivo}: {e}") from e

    @staticmethod
    def leer_registro(propietario: str) -> RegistroForestal:
        """Lee un registro forestal desde disco usando pickle."""
        if not propietario or propietario.strip() == "":
            raise ValueError("El nombre del propietario no puede ser nulo o vacío")

        nombre_archivo = f"data/{propietario}.pkl"

        try:
            with open(nombre_archivo, "rb") as f:
                registro = pickle.load(f)

            print(f"Lectura exitosa para: {propietario}")
            return registro

        except FileNotFoundError as ex:
            raise PersistenciaException(f"Archivo no encontrado: {nombre_archivo}") from ex
        except Exception as ex:
            raise PersistenciaException(f"Error al leer {nombre_archivo}: {ex}") from ex

# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\terrenos\tierra_service.py
# ================================================================================

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion


class TierraService:
    """
    Servicio para operaciones sobre Tierra.
    Incluye lógica de creación e inicialización.
    """

    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str
    ) -> Tierra:
        """
        Crea una nueva Tierra e inicializa automáticamente su plantación.
        Factory method que encapsula la creación completa.
        """
        tierra = Tierra(id_padron_catastral, superficie, domicilio)

        # Crear plantación asociada automáticamente
        plantacion = Plantacion(1, nombre_plantacion, 100000, tierra)
        tierra.finca = plantacion

        print(f"Tierra creada: {domicilio} con plantación: {nombre_plantacion}")
        return tierra


