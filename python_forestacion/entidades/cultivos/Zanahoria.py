from .hortaliza import Hortaliza

class Zanahoria(Hortaliza):
    """
    Entidad Zanahoria - solo contiene datos/estado.
    La lógica de comportamiento está en ZanahoriaService.
    """

    def __init__(self, is_baby: bool):
        super().__init__(agua=0, sup=0.15, invernadero=False)
        self.is_baby_carrot = is_baby

    def is_baby_carrot(self) -> bool:
        return self.is_baby_carrot

    def set_baby_carrot(self, baby_carrot: bool):
        self.is_baby_carrot = baby_carrot
