"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\personal
Fecha: 2025-11-05 10:21:18
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\personal\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: apto_medico.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\personal\apto_medico.py
# ================================================================================

from datetime import date

class AptoMedico:
    """
    Entidad que representa la certificación médica de un trabajador.
    Contiene solo el estado (datos) del apto médico.

    REFACTORIZADO: Extraída de clase interna de Trabajador a clase independiente.
    """

    def __init__(self, apto: bool, fecha_emision: date, observaciones: str):
        """
        Constructor completo para crear un apto médico.

        :param apto: Estado de aptitud (True = apto, False = no apto)
        :param fecha_emision: Fecha de emisión del certificado médico
        :param observaciones: Observaciones médicas del certificado
        """
        self.apto = apto
        self.fecha_emision = fecha_emision
        self.observaciones = observaciones

    # --- Métodos de acceso (Getters y Setters) ---
    def esta_apto(self) -> bool:
        """Verifica si el trabajador está apto médicamente."""
        return self.apto

    def set_apto(self, apto: bool) -> None:
        """Define el estado de aptitud médica."""
        self.apto = apto

    def get_fecha_emision(self) -> date:
        """Devuelve la fecha de emisión del certificado."""
        return self.fecha_emision

    def set_fecha_emision(self, fecha_emision: date) -> None:
        """Modifica la fecha de emisión del certificado."""
        self.fecha_emision = fecha_emision

    def get_observaciones(self) -> str:
        """Devuelve las observaciones médicas."""
        return self.observaciones

    def set_observaciones(self, observaciones: str) -> None:
        """Modifica las observaciones médicas."""
        self.observaciones = observaciones

    def get_resumen(self) -> str:
        """Genera un resumen legible del apto médico."""
        return f"Apto: {self.apto} | Fecha: {self.fecha_emision} | Obs: {self.observaciones}"


# ================================================================================
# ARCHIVO 3/5: herramienta.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\personal\herramienta.py
# ================================================================================

class Herramienta:
    def __init__(self, id: int, nombre: str, certificado_hys: bool):
        self._id = id
        self.nombre = nombre
        self.certificado_hys = certificado_hys

    @property
    def id(self):
        return self._id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_certificado(self):
        return self.certificado_hys

    def set_certificado(self, certificado_hys: bool):
        self.certificado_hys = certificado_hys


# ================================================================================
# ARCHIVO 4/5: tarea.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\personal\tarea.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/5: trabajador.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\personal\trabajador.py
# ================================================================================

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


