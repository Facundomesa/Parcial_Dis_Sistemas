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
