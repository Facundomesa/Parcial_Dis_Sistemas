class ObservadorPlantacion:
    """Observador que reacciona ante cambios en la plantación."""
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"[{self.nombre}] recibió notificación: {mensaje}")
