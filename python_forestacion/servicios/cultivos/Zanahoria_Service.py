from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class ZanahoriaService:
    """
    Servicio para operaciones específicas de la Zanahoria.
    """

    def desarrollar_semilla(self, zanahoria: Zanahoria):
        print("Desarrollando semilla de zanahoria")

    def absorver_agua(self, zanahoria: Zanahoria) -> int:
        zanahoria.set_agua(zanahoria.get_agua() + 2)
        return 2

    def consumir_agua(self, zanahoria: Zanahoria) -> int:
        zanahoria.set_agua(zanahoria.get_agua() - 1)
        return 1

    def mostrar_datos(self, zanahoria: Zanahoria):
        print(f"Cultivo: {type(zanahoria).__name__}")
        if zanahoria.is_baby_carrot():
            print("Es baby carrot")
