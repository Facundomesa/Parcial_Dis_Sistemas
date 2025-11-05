"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Strategy
Fecha: 2025-11-05 10:21:18
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Strategy\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: contexto_cultivo.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Strategy\contexto_cultivo.py
# ================================================================================

class ContextoCultivo:
    """Contexto que permite cambiar de estrategia según el tipo de cultivo."""
    def __init__(self, estrategia):
        self._estrategia = estrategia

    def set_estrategia(self, nueva_estrategia):
        self._estrategia = nueva_estrategia

    def ejecutar_estrategia(self, cultivo):
        self._estrategia.ejecutar(cultivo)

# ================================================================================
# ARCHIVO 3/5: estrategia_cultivo.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Strategy\estrategia_cultivo.py
# ================================================================================

from abc import ABC, abstractmethod

class EstrategiaCultivo(ABC):
    """Interfaz base para estrategias de cultivo."""
    @abstractmethod
    def ejecutar(self, cultivo):
        pass


# ================================================================================
# ARCHIVO 4/5: estrategia_fertilizacion_manual.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Strategy\estrategia_fertilizacion_manual.py
# ================================================================================

from .estrategia_cultivo import EstrategiaCultivo

class EstrategiaFertilizacionManual(EstrategiaCultivo):
    def ejecutar(self, cultivo):
        print(f"Fertilización manual aplicada al cultivo {cultivo.nombre}.")


# ================================================================================
# ARCHIVO 5/5: estrategia_riego_automatizado.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Strategy\estrategia_riego_automatizado.py
# ================================================================================

from .estrategia_cultivo import EstrategiaCultivo

class EstrategiaRiegoAutomatizado(EstrategiaCultivo):
    def ejecutar(self, cultivo):
        print(f"Riego automatizado ejecutado para el cultivo {cultivo.nombre}.")


