"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\excepciones
Fecha: 2025-11-05 10:21:18
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\excepciones\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: agua_agotada_excepcion.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\excepciones\agua_agotada_excepcion.py
# ================================================================================

from python_forestacion.excepciones.forestacion_excepcion import ForestacionException
from python_forestacion.excepciones.mensajes_excepcion import MensajesException


class AguaAgotadaException(ForestacionException):
    """
    Excepción lanzada cuando el agua disponible en la plantación
    es insuficiente para riego.
    """

    def __init__(self, agua_disponible: float = 0, agua_minima: float = 10):
        # Llamada al constructor de la excepción base con mensajes
        mensaje_detallado = MensajesException.get_agua_agotada_detallado_message(
            agua_disponible, agua_minima
        )
        super().__init__(
            MensajesException.ERROR_CODE_01,
            MensajesException.ERROR_01_AGUA_AGOTADA,
            mensaje_detallado
        )
        self._agua_disponible = agua_disponible
        self._agua_minima = agua_minima

    @property
    def agua_disponible(self) -> float:
        return self._agua_disponible

    @property
    def agua_minima(self) -> float:
        return self._agua_minima


# ================================================================================
# ARCHIVO 3/6: forestacion_excepcion.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\excepciones\forestacion_excepcion.py
# ================================================================================

class ForestacionException(Exception):
    """
    Excepción base para todas las excepciones del sistema de forestación.
    Proporciona una jerarquía común y códigos de error estandarizados.
    """

    def __init__(self, error_code: str, message: str, user_message: str = None, cause: Exception = None):
        """
        Constructor con mensaje técnico y opcional mensaje para usuario y causa raíz.
        """
        super().__init__(message)
        self._error_code = error_code
        self._user_message = user_message if user_message is not None else message
        self.__cause__ = cause  # Para mantener la causa original si existe

    @property
    def error_code(self) -> str:
        return self._error_code

    @property
    def user_message(self) -> str:
        return self._user_message

    def get_full_message(self) -> str:
        """
        Retorna el mensaje completo formateado: código + mensaje.
        """
        base_msg = f"{self._error_code} - {self._user_message}"
        if self.__cause__:
            base_msg += f" | Causa: {str(self.__cause__)}"
        return base_msg

    def __str__(self):
        return self.get_full_message()


# ================================================================================
# ARCHIVO 4/6: mensajes_excepcion.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\excepciones\mensajes_excepcion.py
# ================================================================================

class MensajesException:
    # ============================================
    # CÓDIGOS DE ERROR
    # ============================================
    ERROR_CODE_00 = "ERROR 00"
    ERROR_CODE_01 = "ERROR 01"
    ERROR_CODE_02 = "ERROR 02"
    ERROR_CODE_03 = "ERROR 03"
    ERROR_CODE_04 = "ERROR 04"
    ERROR_CODE_05 = "ERROR 05"
    ERROR_CODE_06 = "ERROR 06"
    ERROR_CODE_07 = "ERROR 07"

    # ============================================
    # ERRORES GENERALES
    # ============================================
    ERROR_00_NO_IDENTIFICADO = "Se produjo un error no identificado en el sistema"

    # ============================================
    # ERRORES DE RIEGO Y AGUA
    # ============================================
    ERROR_01_AGUA_AGOTADA = "Se agotó el agua disponible en la finca"
    ERROR_01_AGUA_AGOTADA_USER_MESSAGE = (
        "No hay suficiente agua disponible para continuar el riego. Nivel de agua crítico."
    )

    @staticmethod
    def get_agua_agotada_detallado_message(agua_disponible: float, agua_minima: float) -> str:
        return f"Agua insuficiente para riego. Disponible: {agua_disponible:.2f} L, Mínimo requerido: {agua_minima:.2f} L"

    # ============================================
    # ERRORES DE SUPERFICIE Y PLANTACIÓN
    # ============================================
    ERROR_02_SUPERFICIE_INSUFICIENTE_PREFIX = "No se pudo plantar: "
    ERROR_02_SUPERFICIE_INSUFICIENTE_SUFFIX = " porque no queda superficie disponible en la finca"

    @staticmethod
    def get_superficie_insuficiente_message(cultivo: str) -> str:
        return MensajesException.ERROR_02_SUPERFICIE_INSUFICIENTE_PREFIX + cultivo + \
               MensajesException.ERROR_02_SUPERFICIE_INSUFICIENTE_SUFFIX

    @staticmethod
    def get_superficie_insuficiente_user_message(cultivo: str) -> str:
        return f"No hay suficiente espacio en la plantación para cultivar {cultivo}"

    @staticmethod
    def get_superficie_insuficiente_detallado_message(cultivo: str, superficie_requerida: float, superficie_disponible: float) -> str:
        return f"No se puede plantar {cultivo}. Requiere: {superficie_requerida:.2f} m², Disponible: {superficie_disponible:.2f} m²"

    # ============================================
    # ERRORES DE PERSISTENCIA
    # ============================================
    ERROR_03_ARCHIVO_NO_ENCONTRADO_ESCRITURA = "No se encontró la ruta del archivo para escritura"
    ERROR_04_IO_ESCRITURA = "Se produjo un error de entrada/salida durante la escritura"
    ERROR_05_ARCHIVO_NO_ENCONTRADO_LECTURA = "No se encontró el archivo para lectura"
    ERROR_06_IO_LECTURA = "Se produjo un error de entrada/salida durante la lectura"
    ERROR_07_CLASS_NOT_FOUND = "Error de conversión de clase durante la deserialización"

    @staticmethod
    def get_archivo_no_encontrado_message(nombre_archivo: str) -> str:
        return f"No se encontró el archivo: {nombre_archivo}"

    @staticmethod
    def get_io_error_message(nombre_archivo: str) -> str:
        return f"Error de entrada/salida al procesar el archivo: {nombre_archivo}"

    @staticmethod
    def get_class_not_found_message(nombre_archivo: str) -> str:
        return f"Error de deserialización. Verifique la versión de las clases en: {nombre_archivo}"

    # ============================================
    # MENSAJES DE OPERACIONES EXITOSAS
    # ============================================
    @staticmethod
    def get_persistencia_exitosa_message(propietario: str) -> str:
        return f"Registro persistido exitosamente: {propietario}"

    @staticmethod
    def get_lectura_exitosa_message(propietario: str) -> str:
        return f"Registro leído exitosamente: {propietario}"


# ================================================================================
# ARCHIVO 5/6: persistencia_excepcion.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\excepciones\persistencia_excepcion.py
# ================================================================================

from enum import Enum
from .forestacion_excepcion import ForestacionException
from .mensajes_excepcion import MensajesException


class PersistenciaException(ForestacionException):
    class TipoOperacion(Enum):
        ESCRITURA = "ESCRITURA"
        LECTURA = "LECTURA"

    def __init__(self, error_code: str, message: str, user_message: str, tipo_operacion: 'PersistenciaException.TipoOperacion', cause: Exception = None):
        super().__init__(error_code, message, user_message)
        self.tipo_operacion = tipo_operacion
        self.__cause__ = cause  # Para mantener la referencia de la causa original

    @classmethod
    def archivo_no_encontrado(cls, tipo_operacion: 'PersistenciaException.TipoOperacion', nombre_archivo: str, cause: Exception = None):
        if tipo_operacion == cls.TipoOperacion.ESCRITURA:
            return cls(
                MensajesException.ERROR_CODE_03,
                MensajesException.ERROR_03_ARCHIVO_NO_ENCONTRADO_ESCRITURA,
                MensajesException.get_archivo_no_encontrado_message(nombre_archivo),
                tipo_operacion,
                cause
            )
        else:
            return cls(
                MensajesException.ERROR_CODE_05,
                MensajesException.ERROR_05_ARCHIVO_NO_ENCONTRADO_LECTURA,
                MensajesException.get_archivo_no_encontrado_message(nombre_archivo),
                tipo_operacion,
                cause
            )

    @classmethod
    def from_io_error(cls, tipo_operacion: 'PersistenciaException.TipoOperacion', nombre_archivo: str, io_exception: Exception):
        if tipo_operacion == cls.TipoOperacion.ESCRITURA:
            return cls(
                MensajesException.ERROR_CODE_04,
                MensajesException.ERROR_04_IO_ESCRITURA,
                MensajesException.get_io_error_message(nombre_archivo),
                tipo_operacion,
                io_exception
            )
        else:
            return cls(
                MensajesException.ERROR_CODE_06,
                MensajesException.ERROR_06_IO_LECTURA,
                MensajesException.get_io_error_message(nombre_archivo),
                tipo_operacion,
                io_exception
            )

    @classmethod
    def from_class_not_found(cls, nombre_archivo: str, cause: Exception):
        return cls(
            MensajesException.ERROR_CODE_07,
            MensajesException.ERROR_07_CLASS_NOT_FOUND,
            MensajesException.get_class_not_found_message(nombre_archivo),
            cls.TipoOperacion.LECTURA,
            cause
        )


# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_excepcion.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\excepciones\superficie_insuficiente_excepcion.py
# ================================================================================

from python_forestacion.excepciones.forestacion_excepcion import ForestacionException
from python_forestacion.excepciones.mensajes_excepcion import MensajesException




class SuperficieInsuficienteException(ForestacionException):
    def __init__(self, tipo_cultivo: str, superficie_requerida: float = 0, superficie_disponible: float = 0):
        if superficie_requerida == 0 and superficie_disponible == 0:
            user_message = MensajesException.getSuperficieInsuficienteUserMessage(tipo_cultivo)
        else:
            user_message = MensajesException.getSuperficieInsuficienteDetalladoMessage(
                tipo_cultivo, superficie_requerida, superficie_disponible
            )

        super().__init__(
            MensajesException.ERROR_CODE_02,
            MensajesException.getSuperficieInsuficienteMessage(tipo_cultivo),
            user_message
        )

        self._tipo_cultivo = tipo_cultivo
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

    # Propiedades de solo lectura
    @property
    def tipo_cultivo(self) -> str:
        return self._tipo_cultivo

    @property
    def superficie_requerida(self) -> float:
        return self._superficie_requerida

    @property
    def superficie_disponible(self) -> float:
        return self._superficie_disponible


