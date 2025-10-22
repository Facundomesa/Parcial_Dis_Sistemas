class ContextoCultivo:
    """Contexto que permite cambiar de estrategia según el tipo de cultivo."""
    def __init__(self, estrategia):
        self._estrategia = estrategia

    def set_estrategia(self, nueva_estrategia):
        self._estrategia = nueva_estrategia

    def ejecutar_estrategia(self, cultivo):
        self._estrategia.ejecutar(cultivo)