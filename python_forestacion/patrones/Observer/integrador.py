"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Observer
Fecha: 2025-11-05 10:21:18
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Observer\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observador_plantacion.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Observer\observador_plantacion.py
# ================================================================================

class ObservadorPlantacion:
    """Observador que reacciona ante cambios en la plantación."""
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"[{self.nombre}] recibió notificación: {mensaje}")


# ================================================================================
# ARCHIVO 3/3: sujeto_plantacion.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Observer\sujeto_plantacion.py
# ================================================================================

class SujetoPlantacion:
    """Sujeto que notifica a observadores cuando cambia el estado de la plantación."""
    def __init__(self):
        self._observadores = []

    def agregar_observador(self, observador):
        self._observadores.append(observador)

    def eliminar_observador(self, observador):
        self._observadores.remove(observador)

    def notificar(self, mensaje):
        for observador in self._observadores:
            observador.actualizar(mensaje)


