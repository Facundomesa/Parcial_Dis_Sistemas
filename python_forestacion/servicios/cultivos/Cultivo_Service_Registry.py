from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class CultivoServiceRegistry:
    """
    Registry para despachar automáticamente servicios según el tipo de cultivo.
    """

    def __init__(self, pino_service, olivo_service, lechuga_service, zanahoria_service):
        self.pino_service = pino_service
        self.olivo_service = olivo_service
        self.lechuga_service = lechuga_service
        self.zanahoria_service = zanahoria_service

        # Mapeos para métodos de crecimiento/absorción de agua
        self._handlers_crecer = {
            Pino: lambda c: self.pino_service.absorver_agua(c),
            Olivo: lambda c: self.olivo_service.absorver_agua(c),
            Lechuga: lambda c: self.lechuga_service.absorver_agua(c),
            Zanahoria: lambda c: self.zanahoria_service.absorver_agua(c)
        }

        # Mapeos para mostrar datos
        self._handlers_mostrar = {
            Pino: lambda c: self.pino_service.mostrar_datos(c),
            Olivo: lambda c: self.olivo_service.mostrar_datos(c),
            Lechuga: lambda c: self.lechuga_service.mostrar_datos(c),
            Zanahoria: lambda c: self.zanahoria_service.mostrar_datos(c)
        }

    def crecer(self, cultivo):
        handler = self._handlers_crecer.get(type(cultivo))
        if handler is None:
            raise ValueError(f"No hay servicio registrado para: {type(cultivo).__name__}")
        return handler(cultivo)

    def mostrar_datos(self, cultivo):
        handler = self._handlers_mostrar.get(type(cultivo))
        if handler is None:
            raise ValueError(f"No hay servicio registrado para: {type(cultivo).__name__}")
        return handler(cultivo)
