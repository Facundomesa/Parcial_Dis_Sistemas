"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\terrenos
Fecha: 2025-11-05 10:21:18
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\terrenos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\terrenos\plantacion.py
# ================================================================================

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador

class Plantacion:
    """
    Clase que representa una plantación o finca.
    Contiene solo el estado (datos) de la plantación.
    La lógica de plantar, regar, etc. está en PlantacionService.
    """

    def __init__(self, id_: int, nombre: str, agua: int, tierra: "Tierra"):
        # Import dentro del método para romper circular import
        from python_forestacion.entidades.terrenos.tierra import Tierra
        self._id = id_
        self._nombre = nombre
        self._agua_disponible = agua
        self._situada_en: Tierra = tierra
        self._cultivos: List["Cultivo"] = []
        self._trabajadores: List["Trabajador"] = []

    # --- Getters y Setters ---
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        self._nombre = value

    @property
    def agua_disponible(self) -> int:
        return self._agua_disponible

    @agua_disponible.setter
    def agua_disponible(self, value: int):
        self._agua_disponible = value

    @property
    def situada_en(self) -> "Tierra":
        # Import dentro del getter para romper circular import
        from python_forestacion.entidades.terrenos.tierra import Tierra
        return self._situada_en

    @situada_en.setter
    def situada_en(self, value: "Tierra"):
        from python_forestacion.entidades.terrenos.tierra import Tierra
        self._situada_en = value

    # --- Manejo de listas ---
    @property
    def cultivos(self) -> List["Cultivo"]:
        return list(self._cultivos)

    @cultivos.setter
    def cultivos(self, value: List["Cultivo"]):
        self._cultivos = list(value)

    @property
    def trabajadores(self) -> List["Trabajador"]:
        return list(self._trabajadores)

    @trabajadores.setter
    def trabajadores(self, value: List["Trabajador"]):
        self._trabajadores = list(value)

    # --- Métodos internos ---
    def get_cultivos_interno(self) -> List["Cultivo"]:
        return self._cultivos

    def get_trabajadores_interno(self) -> List["Trabajador"]:
        return self._trabajadores


# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\terrenos\registro_forestal.py
# ================================================================================

from dataclasses import dataclass
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion


@dataclass
class RegistroForestal:
    """
    Entidad que representa un registro forestal catastral.
    Contiene solo el estado (datos) del registro.
    La lógica de persistencia está en RegistroForestalService.
    """

    id_padron: int
    tierra: Tierra
    plantacion: Plantacion
    propietario: str
    avaluo: float

    def __init__(self, id_padron: int, tierra: Tierra, plantacion: Plantacion,
                 propietario: str, avaluo: float):
        self.id_padron = id_padron
        self.tierra = tierra
        self.plantacion = plantacion
        self.propietario = propietario
        self.avaluo = avaluo

    # Getters y Setters
    def get_plantacion(self) -> Plantacion:
        return self.plantacion

    def get_id_padron(self) -> int:
        return self.id_padron

    def set_id_padron(self, id_padron: int):
        self.id_padron = id_padron

    def get_tierra(self) -> Tierra:
        return self.tierra

    def get_propietario(self) -> str:
        return self.propietario

    def set_propietario(self, propietario: str):
        self.propietario = propietario

    def get_avaluo(self) -> float:
        return self.avaluo

    def set_avaluo(self, avaluo: float):
        self.avaluo = avaluo


# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\terrenos\tierra.py
# ================================================================================

from typing import Optional, TYPE_CHECKING

# Solo para anotaciones de tipo estáticas
if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion

class Tierra:
    """
    Clase que representa una tierra o parcela.
    Contiene solo el estado (datos) de la tierra.
    La lógica de negocio se maneja en los servicios correspondientes.
    """

    def __init__(self, id_padron_catastral: int, superficie: float, domicilio: str):
        self._id = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca: Optional["Plantacion"] = None  

    
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def superficie(self) -> float:
        return self._superficie

    @superficie.setter
    def superficie(self, value: float):
        self._superficie = value

    @property
    def domicilio(self) -> str:
        return self._domicilio

    @domicilio.setter
    def domicilio(self, value: str):
        self._domicilio = value

    @property
    def finca(self) -> Optional["Plantacion"]:
        from python_forestacion.entidades.terrenos.plantacion import Plantacion
        return self._finca

    @finca.setter
    def finca(self, value: "Plantacion"):
        from python_forestacion.entidades.terrenos.plantacion import Plantacion
        self._finca = value


