from datetime import date
from typing import List
from .apto_medico import AptoMedico  
from .tarea import Tarea  

class Trabajador:
    def __init__(self, dni: int, nombre: str, tareas: List[Tarea]):
        self.dni = dni
        self._nombre = nombre
        self._tareas = list(tareas)  # Copia defensiva
        # Inicializar apto médico por defecto
        self._apto_medico = AptoMedico(True, date.today(), "Estado de salud: bueno")

    # Getters y Setters
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        self._nombre = value

    @property
    def apto_medico(self) -> AptoMedico:
        return self._apto_medico

    @apto_medico.setter
    def apto_medico(self, value: AptoMedico):
        self._apto_medico = value

    @property
    def tareas(self) -> List[Tarea]:
        # Retorna copia para proteger estado interno (similar a Collections.unmodifiableList)
        return list(self._tareas)

    @tareas.setter
    def tareas(self, value: List[Tarea]):
        self._tareas = list(value)  # Copia defensiva

    # Método de conveniencia para asignar apto médico
    def asignar_apto_medico(self, apto: bool, fecha_emision: date, observaciones: str):
        self._apto_medico = AptoMedico(apto, fecha_emision, observaciones)
