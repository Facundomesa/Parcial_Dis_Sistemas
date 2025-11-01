import time
from excepciones.agua_agotada_excepcion import AguaAgotadaException


class ControlRiegoTask:
    """
    Tarea de control de riego automatizado.
    Monitorea sensores de temperatura y humedad para decidir cuándo regar.

    REFACTORIZADO: Usa inyección de dependencias.
    """

    def __init__(self, temp_task, hum_task, finca, plantacion_service):
        """
        Constructor con inyección de dependencias.

        :param temp_task: instancia de TemperaturaReaderTask
        :param hum_task: instancia de HumedadReaderTask
        :param finca: objeto Plantacion
        :param plantacion_service: instancia de PlantacionService
        """
        self.temp_task = temp_task
        self.hum_task = hum_task
        self.finca = finca
        self.plantacion_service = plantacion_service
        self.ejecutando = True

    def run(self):
        """Ejecuta el bucle principal de control de riego."""
        while self.ejecutando:
            try:
                temp = self.temp_task.get_ultima_temperatura()
                hum = self.hum_task.get_ultima_humedad()

                if temp is not None and hum is not None:
                    if 8 <= temp <= 15 and hum < 50:
                        self.plantacion_service.regar(self.finca)

                time.sleep(2.5)  # frecuencia de control

            except AguaAgotadaException as e:
                print(e.get_full_message())
                print("Sistema de riego detenido automáticamente por falta de agua.")
                self.ejecutando = False
                break

            except KeyboardInterrupt:
                print("Interrupción manual: deteniendo el sistema de riego.")
                self.ejecutando = False
                break

    def detener(self):
        """Detiene el sistema de control."""
        self.ejecutando = False
