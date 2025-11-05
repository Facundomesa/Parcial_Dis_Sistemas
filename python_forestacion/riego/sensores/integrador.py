"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\riego\sensores
Fecha: 2025-11-05 10:21:19
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\riego\sensores\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: humedad_reader_task.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\riego\sensores\humedad_reader_task.py
# ================================================================================

import threading
import time
import random


class HumedadReaderTask(threading.Thread):
    """
    Hilo que simula la lectura de un sensor de humedad.
    Actualiza periódicamente el valor de humedad en porcentaje.
    """

    def __init__(self):
        super().__init__()
        self._ultima_humedad = float("nan")
        self._ejecutando = True

    def run(self):
        """Bucle principal de lectura de humedad."""
        while self._ejecutando:
            try:
                self._ultima_humedad = self._leer_sensor()
                print(f"[Humedad] {self._ultima_humedad:.2f} %")
                time.sleep(3)  # simula el muestreo cada 3 segundos
            except KeyboardInterrupt:
                break

    def _leer_sensor(self) -> float:
        """Simula la lectura del sensor de humedad (0% a 100%)."""
        return random.random() * 100

    def get_ultima_humedad(self) -> float:
        """Devuelve la última lectura registrada."""
        return self._ultima_humedad

    def detener(self):
        """Detiene la lectura del sensor."""
        self._ejecutando = False


# ================================================================================
# ARCHIVO 3/3: temperatura_reader_task.py
# Ruta: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\riego\sensores\temperatura_reader_task.py
# ================================================================================

import threading
import time
import random


class TemperaturaReaderTask(threading.Thread):
    """
    Hilo que simula la lectura de un sensor de temperatura.
    Actualiza periódicamente el valor de temperatura en grados Celsius.
    """

    def __init__(self):
        super().__init__()
        self._ultima_temperatura = float("nan")
        self._ejecutando = True

    def run(self):
        """Bucle principal de lectura de temperatura."""
        while self._ejecutando:
            try:
                self._ultima_temperatura = self._leer_sensor()
                print(f"[Temperatura] {self._ultima_temperatura:.2f} °C")
                time.sleep(2)  # simula muestreo cada 2 segundos
            except KeyboardInterrupt:
                break

    def _leer_sensor(self) -> float:
        """Simula la lectura del sensor de temperatura (-25 a 50 °C)."""
        return -25 + random.random() * 75

    def get_ultima_temperatura(self) -> float:
        """Devuelve la última lectura registrada."""
        return self._ultima_temperatura

    def detener(self):
        """Detiene la lectura del sensor."""
        self._ejecutando = False


