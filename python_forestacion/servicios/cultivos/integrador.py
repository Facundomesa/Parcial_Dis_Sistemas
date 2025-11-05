"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\cultivos
Fecha: 2025-11-05 10:21:19
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\cultivos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\cultivos\arbol_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\cultivos\cultivo_service.py
# ================================================================================

from python_forestacion.entidades.cultivos.cultivo import Cultivo

class CultivoService:
    """Servicio base para operaciones comunes de cultivos."""

    def mostrar_datos(self, cultivo: Cultivo):
        print(f"Cultivo: {cultivo.__class__.__name__}")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")


# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\cultivos\cultivo_service_registry.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\cultivos\lechuga_service.py
# ================================================================================

from python_forestacion.entidades.cultivos.lechuga import Lechuga

class LechugaService:
    """
    Servicio para operaciones específicas de la Lechuga.
    """

    def desarrollar_semilla(self, lechuga: Lechuga):
        print("Desarrollando semilla de lechuga")

    def absorber_agua(self, lechuga: Lechuga) -> int:
        """Corrige typo y usa el método absorber_agua de la clase"""
        lechuga.absorber_agua(1)
        return 1

    def consumir_agua(self, lechuga: Lechuga) -> int:
        lechuga.set_agua(lechuga.get_agua() - 1)
        return 1

    def mostrar_datos(self, lechuga: Lechuga):
        print(f"Cultivo: {type(lechuga).__name__}")
        print(f"Variedad: {lechuga.get_variedad()}")


# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\cultivos\olivo_service.py
# ================================================================================

from datetime import datetime
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.servicios.cultivos.arbol_service import ArbolService

class OlivoService(ArbolService):
    """
    Servicio para operaciones específicas del Olivo.
    Implementa la lógica de negocio estacional del olivo.
    """

    def cosechar(self, olivo: Olivo) -> bool:
        mes = datetime.now().month
        if 5 <= mes <= 7:
            print("Se ha cosechado este olivo")
            return True
        return False

    def florecer(self, olivo: Olivo) -> bool:
        mes = datetime.now().month
        return 9 <= mes <= 12

    def absorber_agua(self, olivo: Olivo) -> int:
        """Corrige typo y usa el método absorber_agua del cultivo"""
        mes = datetime.now().month
        agua_absorbida = 1 if mes in [1,2,3,4,9,10,11,12] else 0
        olivo.absorber_agua(agua_absorbida)
        return agua_absorbida

    def consumir_agua(self, olivo: Olivo) -> int:
        mes = datetime.now().month
        if mes in [1,2,3,4,9,10,11,12]:
            agua_consumida = 2
            self.crecer(olivo, 0.01)
        elif mes in [5,6,7,8]:
            agua_consumida = 1
        else:
            agua_consumida = 0

        olivo.set_agua(olivo.get_agua() - agua_consumida)
        return agua_consumida

    def mostrar_datos(self, olivo: Olivo):
        print(f"Cultivo {type(olivo).__name__}")
        print(f"Fruto: {olivo.get_fruto().name}")
        print(f"Altura: {olivo.get_altura()}")


# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\cultivos\pino_service.py
# ================================================================================

from datetime import datetime
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.servicios.cultivos.arbol_service import ArbolService

class PinoService(ArbolService):
    """
    Servicio para operaciones específicas del Pino.
    Implementa la lógica de negocio estacional del pino.
    """

    def secretar_resina(self, pino: Pino):
        print("Estoy secretando resina")

    def florecer(self, pino: Pino) -> bool:
        mes = datetime.now().month
        return 9 <= mes <= 12

    def absorber_agua(self, pino: Pino) -> int:
        """Corrige typo y usa el método absorber_agua del cultivo"""
        mes = datetime.now().month
        agua_absorbida = 2 if mes in [1,2,3,4,9,10,11,12] else 0
        pino.absorber_agua(agua_absorbida)
        return agua_absorbida

    def consumir_agua(self, pino: Pino) -> int:
        mes = datetime.now().month
        if mes in [1,2,3,4,9,10,11,12]:
            agua_consumida = 2
            self.crecer(pino, 0.10)
        elif mes in [5,6,7,8]:
            agua_consumida = 1
        else:
            agua_consumida = 0

        pino.set_agua(pino.get_agua() - agua_consumida)
        return agua_consumida

    def mostrar_datos(self, pino: Pino):
        print(f"Cultivo {type(pino).__name__}")
        print(f"Variedad: {pino.get_variedad()}")
        print(f"Altura: {pino.get_altura()}")


# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\cultivos\zanahoria_service.py
# ================================================================================

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


