from python_forestacion.entidades.cultivos.cultivo import Cultivo

class CultivoService:
    """Servicio base para operaciones comunes de cultivos."""

    def mostrar_datos(self, cultivo: Cultivo):
        print(f"Cultivo: {cultivo.__class__.__name__}")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")
