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
