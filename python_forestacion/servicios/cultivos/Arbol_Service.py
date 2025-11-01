from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService:
    """
    Servicio para operaciones específicas de árboles.
    Contiene la lógica de negocio de crecimiento y floración.
    """

    def crecer(self, arbol: Arbol, incremento: float) -> bool:
        """
        Hace crecer un árbol incrementando su altura.
        :param arbol: El árbol a crecer
        :param incremento: El incremento de altura (debe ser >0 y <1)
        :return: True si creció exitosamente, False si no
        """
        if 0 < incremento < 1:
            arbol.altura += incremento
            # Consumir agua al crecer
            self.consumir_agua_por_crecimiento(arbol)
            return True
        return False

    def consumir_agua_por_crecimiento(self, arbol: Arbol):
        """
        Consume agua del árbol por el proceso de crecimiento.
        Este método puede ser sobrescrito por servicios específicos.
        """
        if arbol.agua > 0:
            arbol.agua -= 1
