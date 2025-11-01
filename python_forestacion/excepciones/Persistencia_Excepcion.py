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
