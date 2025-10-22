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
