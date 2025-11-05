"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Factory
Fecha: 2025-11-05 10:21:18
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Factory\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: cultivo_Factory.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Factory\cultivo_Factory.py
# ================================================================================

from entidades.cultivos.pino import Pino
from entidades.cultivos.olivo import Olivo, TipoAceituna
from entidades.cultivos.lechuga import Lechuga
from entidades.cultivos.zanahoria import Zanahoria

class CultivoFactory:
    """
    Factory Pattern para crear cultivos según el tipo.
    Evita el uso de múltiples if/switch en el código principal.
    """

    @staticmethod
    def crear_cultivo(tipo: str):
        tipo = tipo.lower()
        if tipo == "pino":
            return Pino("cedro")
        elif tipo == "olivo":
            return Olivo(TipoAceituna.NEGRA)
        elif tipo == "lechuga":
            return Lechuga("Mantecosa")
        elif tipo == "zanahoria":
            return Zanahoria(True)
        else:
            raise ValueError(f"Tipo de cultivo no reconocido: {tipo}")



