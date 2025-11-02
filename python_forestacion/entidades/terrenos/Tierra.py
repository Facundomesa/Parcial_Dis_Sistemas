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
