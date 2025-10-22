from dataclasses import dataclass
from typing import Optional
from .Tierra import Tierra
from .Plantacion import Plantacion

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
