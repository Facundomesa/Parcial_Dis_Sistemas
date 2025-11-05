"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Singleton
Fecha: 2025-11-05 10:21:18
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Singleton\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: registro_forestal_service.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Singleton\registro_forestal_service.py
# ================================================================================

from entidades.terrenos.tierra import Tierra

class RegistroForestalService:
    """
    Patrón Singleton.
    Asegura una única instancia global del servicio de registro forestal.
    """

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._registro = []
        return cls._instancia

    def registrar_tierra(self, tierra: Tierra):
        self._registro.append(tierra)
        print(f"🌳 Tierra registrada: {tierra.domicilio}")

    def obtener_registro(self):
        return self._registro


