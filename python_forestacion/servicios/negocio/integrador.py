"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\negocio
Fecha: 2025-11-05 10:21:19
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\negocio\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: box.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\negocio\box.py
# ================================================================================

from typing import Generic, TypeVar, List
from entidades.cultivos.cultivo import Cultivo

T = TypeVar("T", bound=Cultivo)

class Box(Generic[T]):
    """
    Contenedor genérico tipo-seguro para cultivos cosechados.
    Funciona como DTO (Data Transfer Object).
    """

    def __init__(self):
        self.id: int | None = None
        self.productos: List[T] = []

    def add_item(self, producto: T):
        """Agrega un cultivo a la caja."""
        self.productos.append(producto)

    def get_items(self) -> List[T]:
        """Devuelve todos los cultivos en la caja."""
        return self.productos

    def mostrar_contenido_caja(self):
        """Muestra por consola el contenido de la caja."""
        print("CONTENIDO DE LA CAJA")
        print("____________________")
        for c in self.get_items():
            print(f"Cultivo: {c.__class__.__name__}")


# ================================================================================
# ARCHIVO 3/3: fincas_service.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\negocio\fincas_service.py
# ================================================================================

import time
from typing import Type, TypeVar, Generic
from concurrent.futures import ThreadPoolExecutor
from entidades.terrenos.registro_forestal import RegistroForestal
from entidades.cultivos.cultivo import Cultivo
from servicios.negocio.box import Box
from servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from servicios.terrenos.plantacion_service import PlantacionService
from riego.control.control_riego_task import ControlRiegoTask
from riego.sensores.humedad_reader_task import HumedadReaderTask
from riego.sensores.temperatura_reader_task import TemperaturaReaderTask

T = TypeVar("T", bound=Cultivo)

class FincasService:
    """
    Servicio de orquestación para gestión de múltiples fincas.
    Coordina operaciones entre diferentes dominios (cultivos, riego, plantaciones).
    """

    def __init__(self, plantacion_service: PlantacionService, cultivo_service_registry: CultivoServiceRegistry):
        self.fincas: list[RegistroForestal] = []
        self.plantacion_service = plantacion_service
        self.cultivo_service_registry = cultivo_service_registry

    def add_finca(self, finca: RegistroForestal):
        self.fincas.append(finca)

    def remover_finca(self, finca: RegistroForestal):
        self.fincas.remove(finca)

    def fumigar(self, id_finca: int, insecticida: str):
        for finca in self.fincas:
            if finca.plantacion.id == id_finca:
                for c in finca.plantacion.cultivos:
                    print("Se está fumigando el cultivo:")
                    self.mostrar_datos_cultivo(c)
                    print(f"Con el insecticida: {insecticida}")

    def regar(self, duracion_segundos: int = 20):
        """
        Activa el sistema de riego automatizado para todas las fincas.
        """
        for finca in self.fincas:
            tarea_temp = TemperaturaReaderTask()
            tarea_hum = HumedadReaderTask()
            tarea_control = ControlRiegoTask(tarea_temp, tarea_hum, finca.plantacion, self.plantacion_service)

            threads = [
                ThreadPoolExecutor(max_workers=1).submit(tarea_temp.run),
                ThreadPoolExecutor(max_workers=1).submit(tarea_hum.run),
                ThreadPoolExecutor(max_workers=1).submit(tarea_control.run)
            ]

            time.sleep(duracion_segundos)

            # Detener tareas
            tarea_temp.detener()
            tarea_hum.detener()
            tarea_control.detener()

    def cosechar_y_empaquetar(self, tipo_cultivo: Type[T]) -> Box[T]:
        caja = Box[T]()

        for finca in self.fincas:
            for cult in finca.plantacion.cultivos:
                if isinstance(cult, tipo_cultivo):
                    caja.add_item(cult)
            self.plantacion_service.consumir(finca.plantacion, tipo_cultivo)
            print(f"Se cosecharon los/las {tipo_cultivo.__name__}s de la finca {finca.plantacion.nombre}")

        return caja

    def mostrar_datos_cultivo(self, cultivo: Cultivo):
        """Delegar mostrar datos al servicio específico del cultivo."""
        self.cultivo_service_registry.mostrar_datos(cultivo)


