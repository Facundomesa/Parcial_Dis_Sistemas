from entidades.cultivos.Lechuga import Lechuga

class LechugaService:
    """
    Servicio para operaciones específicas de la Lechuga.
    """

    def desarrollar_semilla(self, lechuga: Lechuga):
        print("Desarrollando semilla de lechuga")

    def absorver_agua(self, lechuga: Lechuga) -> int:
        lechuga.set_agua(lechuga.get_agua() + 1)
        return 1

    def consumir_agua(self, lechuga: Lechuga) -> int:
        lechuga.set_agua(lechuga.get_agua() - 1)
        return 1

    def mostrar_datos(self, lechuga: Lechuga):
        print(f"Cultivo: {type(lechuga).__name__}")
        print(f"Variedad: {lechuga.variedad}")
