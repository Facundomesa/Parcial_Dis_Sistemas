"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\personal
Fecha: 2025-11-05 10:21:19
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\personal\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: trabajador_service.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\personal\trabajador_service.py
# ================================================================================

from datetime import date

class TrabajadorService:
    """
    Servicio para operaciones sobre Trabajador.
    Contiene lógica de ejecución de tareas.
    """

    def trabajar(self, trabajador, fecha: date, herramienta):
        """
        Ejecuta las tareas asignadas al trabajador para una fecha específica.
        Solo ejecuta si el trabajador tiene apto médico válido.
        """
        if not trabajador.apto_medico.esta_apto():
            print(f"El trabajador {trabajador.nombre} no puede trabajar - apto médico inválido")
            return False

        # Crear copia mutable de la lista antes de ordenar
        tareas_ordenadas = list(trabajador.tareas)

        # Ordenar tareas por ID descendente
        tareas_ordenadas.sort(key=lambda t: t.id, reverse=True)

        tarea_ejecutada = False
        for t in tareas_ordenadas:
            if t.fecha == fecha:
                print(f"El trabajador {trabajador.nombre} realizó la tarea {t.id} {t.descripcion} "
                      f"con herramienta: {herramienta.nombre}")
                t.estado = True
                tarea_ejecutada = True

        return tarea_ejecutada

    def asignar_apto_medico(self, trabajador, apto: bool, fecha_emision: date, observaciones: str):
        """
        Asigna o actualiza el apto médico de un trabajador.
        """
        trabajador.asignar_apto_medico(apto, fecha_emision, observaciones)
        print(f"Apto médico actualizado para: {trabajador.nombre}")


