
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
