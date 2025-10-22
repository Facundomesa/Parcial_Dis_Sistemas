from datetime import date
from concurrent.futures import ThreadPoolExecutor

from datetime import date

# --- Servicios principales ---
from python_forestacion.servicios.terrenos.Tierra_Service import TierraService
from python_forestacion.servicios.Personal.Trabajador_Service import TrabajadorService
from python_forestacion.servicios.negocio.Fincas_Service import FincaService
from python_forestacion.servicios.negocio.Box import Box
from python_forestacion.servicios.registro.Registro_Forestal_Service import RegistroForestalService

# --- Servicios de cultivos ---
from python_forestacion.servicios.cultivos.Pino_Service import PinoService
from python_forestacion.servicios.cultivos.Olivo_Service import OlivoService
from python_forestacion.servicios.cultivos.Lechuga_Service import LechugaService
from python_forestacion.servicios.cultivos.Zanahoria_Service import ZanahoriaService

# --- Entidades ---
from python_forestacion.entidades.personal.Trabajador import Trabajador
from python_forestacion.entidades.personal.Herramienta import Herramienta
from python_forestacion.entidades.personal.Tarea import Tarea


def main():
    print("=== SISTEMA DE GESTIÓN AGROFORESTAL ===")

    # --- Tierra y plantación ---
    tierra_service = TierraService()
    tierra = tierra_service.crear_tierra_con_plantacion(
        id_padronCatastral=1001,
        superficie=12000.0,
        domicilio="Ruta 40 Km 23",
        nombrePlantacion="Finca Los Pinos"
    )

    # --- Cultivos ---
    pino_service = PinoService()
    olivo_service = OlivoService()
    lechuga_service = LechugaService()
    zanahoria_service = ZanahoriaService()

    print("\n=== Plantando cultivos ===")
    pino_service.plantar_pino(tierra)
    olivo_service.plantar_olivo(tierra)
    lechuga_service.plantar_lechuga(tierra)
    zanahoria_service.plantar_zanahoria(tierra)

    # --- Finca y Box ---
    finca_service = FincaService()
    finca = finca_service.crear_finca("Finca Los Pinos", tierra)

    box_service = Box()
    box_service.crear_box(finca, "Box de Herramientas 1")

    # --- Trabajadores ---
    trabajador_service = TrabajadorService()
    trabajador = Trabajador(id=1, nombre="Carlos López")

    trabajador_service.asignarAptoMedico(
        trabajador,
        apto=True,
        fechaEmision=date.today(),
        observaciones="Apto sin restricciones"
    )

    herramienta = Herramienta(nombre="Motosierra")
    tarea1 = Tarea(id=1, descripcion="Podar árboles", fecha=date.today())
    tarea2 = Tarea(id=2, descripcion="Cosechar olivos", fecha=date.today())

    trabajador.agregar_tarea(tarea1)
    trabajador.agregar_tarea(tarea2)

    print("\n=== Tareas Asignadas ===")
    trabajador_service.trabajar(trabajador, date.today(), herramienta)

    # --- Registro Forestal ---
    registro_service = RegistroForestalService()
    registro_service.registrar_actividad(
        trabajador=trabajador,
        tarea=tarea1,
        fecha=date.today(),
        observacion="Podas realizadas con éxito"
    )

    print("\n=== Finalización del Programa ===")
    print("Gestión completada correctamente")


if __name__ == "__main__":
    main()
