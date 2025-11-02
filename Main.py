# Main.py
from datetime import date

# Servicios
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService

# Servicios de cultivos
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

# Entidades
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal


def main():
    print("=" * 80)
    print("SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")
    print("=" * 80)
    
    # 1. PATRON SINGLETON - CultivoServiceRegistry
    print("\n[1] Patron SINGLETON - Creando servicios...")
    pino_service = PinoService()
    olivo_service = OlivoService()
    lechuga_service = LechugaService()
    zanahoria_service = ZanahoriaService()
    
    registry = CultivoServiceRegistry(
        pino_service, olivo_service, lechuga_service, zanahoria_service
    )
    print("    Registry creado exitosamente")
    
    # 2. Crear tierra con plantación
    print("\n[2] Creando tierra con plantacion...")
    tierra_service = TierraService()
    tierra = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=1,
        superficie=10000.0,
        domicilio="Agrelo, Mendoza",
        nombre_plantacion="Finca del Madero"
    )
    
    plantacion = tierra.finca
    print(f"    Plantacion creada: {plantacion.nombre}")
    print(f"    Superficie disponible: {tierra.superficie} m2")
    
    # 3. PATRON FACTORY - Plantar cultivos
    print("\n[3] PATRON FACTORY - Plantando cultivos...")
    plantacion_service = PlantacionService(registry)
    
    try:
        plantacion_service.plantar(plantacion, "Pino", 5)
        plantacion_service.plantar(plantacion, "Olivo", 5)
        plantacion_service.plantar(plantacion, "Lechuga", 5)
        plantacion_service.plantar(plantacion, "Zanahoria", 5)
        print(f"    Total cultivos plantados: {len(plantacion.cultivos)}")
    except Exception as e:
        print(f"    Error al plantar: {e}")
    
    # 4. PATRON STRATEGY - Regar (usa estrategias de absorción)
    print("\n[4] PATRON STRATEGY - Regando plantacion...")
    try:
        plantacion_service.regar(plantacion)
        print("    Riego completado exitosamente")
        print(f"    Agua restante: {plantacion.agua_disponible} L")
    except Exception as e:
        print(f"    Error al regar: {e}")
    
    # 5. PATRON REGISTRY - Mostrar datos
    print("\n[5] PATRON REGISTRY - Mostrando datos de cultivos...")
    print(f"    Total de cultivos: {len(plantacion.cultivos)}")
    for i, cultivo in enumerate(plantacion.cultivos[:3], 1):
        print(f"    Cultivo {i}: {type(cultivo).__name__}")
    
    # 6. Gestión de trabajadores
    print("\n[6] Gestion de trabajadores...")
    trabajador_service = TrabajadorService()
    
    tareas = [
        Tarea(1, date.today(), "Podar arboles"),
        Tarea(2, date.today(), "Cosechar olivos")
    ]
    
    trabajador = Trabajador(43888734, "Juan Perez", tareas)
    
    trabajador_service.asignar_apto_medico(
        trabajador,
        apto=True,
        fecha_emision=date.today(),
        observaciones="Apto sin restricciones"
    )
    
    herramienta = Herramienta(1, "Motosierra", True)
    resultado = trabajador_service.trabajar(trabajador, date.today(), herramienta)
    print(f"    Tareas ejecutadas: {resultado}")
    
    # 7. Crear registro forestal
    print("\n[7] Creando registro forestal...")
    registro = RegistroForestal(
        id_padron=1,
        tierra=tierra,
        plantacion=plantacion,
        propietario="Juan Perez",
        avaluo=50309233.55
    )
    print(f"    Registro creado para: {registro.propietario}")
    
    # 8. Persistencia
    print("\n[8] Persistiendo datos...")
    registro_service = RegistroForestalService(registry)
    try:
        registro_service.persistir(registro)
        print("    Datos persistidos exitosamente en data/Juan Perez.pkl")
    except Exception as e:
        print(f"    Error al persistir: {e}")
    
    # 9. Mostrar datos del registro
    print("\n[9] Datos del registro forestal:")
    print("-" * 80)
    registro_service.mostrar_datos(registro)
    
    print("\n" + "=" * 80)
    print("PATRONES IMPLEMENTADOS:")
    print("  [OK] SINGLETON   - CultivoServiceRegistry")
    print("  [OK] FACTORY     - Creacion de cultivos")
    print("  [OK] STRATEGY    - Absorcion de agua")
    print("  [OK] REGISTRY    - Dispatch polimorfico")
    print("=" * 80)
    print("SISTEMA EJECUTADO EXITOSAMENTE")
    print("=" * 80)


if __name__ == "__main__":
    main()
