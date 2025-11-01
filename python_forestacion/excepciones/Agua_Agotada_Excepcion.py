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
