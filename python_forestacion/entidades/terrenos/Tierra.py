from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from typing import Optional
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
        self._finca: Optional[Plantacion] = None

    # Getters y Setters (Pythonic con propiedades)
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
    def finca(self) -> Optional[Plantacion]:
        return self._finca

    @finca.setter
    def finca(self, value: Plantacion):
        self._finca = value