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
