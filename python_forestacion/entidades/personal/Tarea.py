from datetime import date

class Tarea:
    def __init__(self, id: int, fecha: date, descripcion: str):
        self._id = id
        self._fecha = fecha
        self._descripcion = descripcion
        self._estado = False  # Inicialmente false como en Java

    # Getters y Setters
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def fecha(self) -> date:
        return self._fecha

    @fecha.setter
    def fecha(self, value: date):
        self._fecha = value

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value: str):
        self._descripcion = value

    @property
    def estado(self) -> bool:
        return self._estado

    @estado.setter
    def estado(self, value: bool):
        self._estado = value
