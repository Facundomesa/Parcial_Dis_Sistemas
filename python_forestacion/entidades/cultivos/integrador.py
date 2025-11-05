"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos
Fecha: 2025-11-05 10:21:18
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\arbol.py
# ================================================================================

from threading import Lock
from .cultivo import Cultivo

class Arbol(Cultivo):
    _cant_arboles = 0
    _lock = Lock()  # Para incrementar de forma segura en entornos concurrentes

    def __init__(self, agua: int, altura: float, superficie: float):
        with Arbol._lock:
            Arbol._cant_arboles += 1
            self._id = Arbol._cant_arboles

        self._agua = agua
        self._altura = altura
        self._superficie = superficie

    # Getters y Setters
    @property
    def id(self) -> int:
        return self._id

    def get_agua(self) -> int:
        return self._agua

    def set_agua(self, agua: int):
        self._agua = agua

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, valor: float):
        self._altura = valor

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float):
        self._superficie = superficie

    @classmethod
    def get_cant_arboles(cls) -> int:
        return cls._cant_arboles


# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\cultivo.py
# ================================================================================

from abc import ABC, abstractmethod

class Cultivo(ABC):
    EDAD_MAXIMA = 20  # Constante de clase

    @abstractmethod
    def get_superficie(self) -> float:
        pass

    @abstractmethod
    def get_agua(self) -> int:
        pass

    @abstractmethod
    def set_agua(self, agua: int):
        pass


# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\hortaliza.py
# ================================================================================

from abc import ABC, abstractmethod

class Cultivo(ABC):
    EDAD_MAXIMA = 20

    @abstractmethod
    def get_superficie(self) -> float:
        pass

    @abstractmethod
    def get_agua(self) -> float:
        pass

    @abstractmethod
    def set_agua(self, agua: float):
        pass

    # Método absorber_agua para riego
    def absorber_agua(self, cantidad: float):
        # Suma la cantidad de agua disponible
        self.set_agua(self.get_agua() + cantidad)


class Hortaliza(Cultivo):
    def __init__(self, agua: float, superficie: float, requiere_invernadero: bool):
        self._agua = agua
        self._superficie = superficie
        self._requiere_invernadero = requiere_invernadero
        self._altura = 0.1  # Altura por defecto para compatibilidad con mostrar_datos

    # Getters y Setters
    def get_agua(self) -> float:
        return self._agua

    def set_agua(self, agua: float):
        self._agua = agua

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float):
        self._superficie = superficie

    def get_requiere_invernadero(self) -> bool:
        return self._requiere_invernadero

    def get_altura(self) -> float:
        # Para compatibilidad con mostrar_datos
        return self._altura



# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\lechuga.py
# ================================================================================

from .hortaliza import Hortaliza

class Lechuga(Hortaliza):
    def __init__(self, variedad: str):
        # Llama al constructor de Hortaliza con valores fijos
        # agua = 1, superficie = 0.10, requiere_invernadero = True
        super().__init__(agua=1, superficie=0.10, requiere_invernadero=True)
        self._variedad = variedad

    # Getter de la variedad
    def get_variedad(self) -> str:
        return self._variedad

    # Getter de altura (aunque sea opcional para hortalizas)
    def get_altura(self) -> float:
        # Podés devolver un valor fijo o un atributo si Hortaliza lo tiene
        return getattr(self, "_altura", 0.1)

    # Getter de agua para riego
    def get_agua(self) -> float:
        return getattr(self, "_agua", 1.0)

    # Método absorber_agua para compatibilidad con servicios de riego
    def absorber_agua(self, cantidad: float):
        # Sumar agua disponible
        self._agua = getattr(self, "_agua", 1.0) + cantidad


# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\olivo.py
# ================================================================================

from .arbol import Arbol
from .tipo_aceituna import TipoAceituna  

class Olivo(Arbol):
    def __init__(self, tipo: TipoAceituna):
        # Llama al constructor de Arbol con valores fijos
        # agua = 5, altura = 0.5, superficie = 3
        super().__init__(agua=5, altura=0.5, superficie=3.0)
        self._fruto = tipo

    # Getter del fruto
    def get_fruto(self) -> TipoAceituna:
        return self._fruto

    # Getter de altura para compatibilidad con mostrar_datos
    def get_altura(self) -> float:
        return self._altura

    # Getter de agua
    def get_agua(self) -> float:
        return self._agua

    # Método absorber_agua para riego
    def absorber_agua(self, cantidad: float):
        self._agua += cantidad



# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\pino.py
# ================================================================================

from .arbol import Arbol

class Pino(Arbol):
    def __init__(self, variedad: str):
        # Llama al constructor de Arbol con valores fijos:
        # agua = 2, altura = 1, superficie = 2
        super().__init__(agua=2, altura=1.0, superficie=2.0)
        self._variedad = variedad

    # Getter de la variedad
    def get_variedad(self) -> str:
        return self._variedad

    # Getter de altura para mostrar datos
    def get_altura(self) -> float:
        return self._altura

    # Getter de agua (opcional, si tu servicio lo usa)
    def get_agua(self) -> float:
        return self._agua


# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\tipo_aceituna.py
# ================================================================================

from enum import Enum

class TipoAceituna(Enum):
    NEGRA = "NEGRA"
    VERDE = "VERDE"
    ROJA = "ROJA"


# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\zanahoria.py
# ================================================================================

from .hortaliza import Hortaliza

class Zanahoria(Hortaliza):
    """
    Entidad Zanahoria - solo contiene datos/estado.
    La lógica de comportamiento está en ZanahoriaService.
    """

    def __init__(self, is_baby: bool):
        super().__init__(agua=0, sup=0.15, invernadero=False)
        self.is_baby_carrot = is_baby

    def is_baby_carrot(self) -> bool:
        return self.is_baby_carrot

    def set_baby_carrot(self, baby_carrot: bool):
        self.is_baby_carrot = baby_carrot


