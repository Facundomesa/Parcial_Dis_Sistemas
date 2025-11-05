"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas
Fecha de generacion: 2025-11-05 10:21:19
Total de archivos integrados: 66
Total de directorios procesados: 20
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. buscar_paquete.py
#   3. main.py
#
# DIRECTORIO: python_forestacion
#   4. __init__.py
#
# DIRECTORIO: python_forestacion\entidades
#   5. __init__.py
#
# DIRECTORIO: python_forestacion\entidades\cultivos
#   6. __init__.py
#   7. arbol.py
#   8. cultivo.py
#   9. hortaliza.py
#   10. lechuga.py
#   11. olivo.py
#   12. pino.py
#   13. tipo_aceituna.py
#   14. zanahoria.py
#
# DIRECTORIO: python_forestacion\entidades\personal
#   15. __init__.py
#   16. apto_medico.py
#   17. herramienta.py
#   18. tarea.py
#   19. trabajador.py
#
# DIRECTORIO: python_forestacion\entidades\terrenos
#   20. __init__.py
#   21. plantacion.py
#   22. registro_forestal.py
#   23. tierra.py
#
# DIRECTORIO: python_forestacion\excepciones
#   24. __init__.py
#   25. agua_agotada_excepcion.py
#   26. forestacion_excepcion.py
#   27. mensajes_excepcion.py
#   28. persistencia_excepcion.py
#   29. superficie_insuficiente_excepcion.py
#
# DIRECTORIO: python_forestacion\patrones
#   30. __init__.py
#
# DIRECTORIO: python_forestacion\patrones\Factory
#   31. __init__.py
#   32. cultivo_Factory.py
#
# DIRECTORIO: python_forestacion\patrones\Observer
#   33. __init__.py
#   34. observador_plantacion.py
#   35. sujeto_plantacion.py
#
# DIRECTORIO: python_forestacion\patrones\Singleton
#   36. __init__.py
#   37. registro_forestal_service.py
#
# DIRECTORIO: python_forestacion\patrones\Strategy
#   38. __init__.py
#   39. contexto_cultivo.py
#   40. estrategia_cultivo.py
#   41. estrategia_fertilizacion_manual.py
#   42. estrategia_riego_automatizado.py
#
# DIRECTORIO: python_forestacion\riego
#   43. __init__.py
#
# DIRECTORIO: python_forestacion\riego\control
#   44. __init__.py
#   45. control_riego_task.py
#
# DIRECTORIO: python_forestacion\riego\sensores
#   46. __init__.py
#   47. humedad_reader_task.py
#   48. temperatura_reader_task.py
#
# DIRECTORIO: python_forestacion\servicios
#   49. __init__.py
#
# DIRECTORIO: python_forestacion\servicios\cultivos
#   50. __init__.py
#   51. arbol_service.py
#   52. cultivo_service.py
#   53. cultivo_service_registry.py
#   54. lechuga_service.py
#   55. olivo_service.py
#   56. pino_service.py
#   57. zanahoria_service.py
#
# DIRECTORIO: python_forestacion\servicios\negocio
#   58. __init__.py
#   59. box.py
#   60. fincas_service.py
#
# DIRECTORIO: python_forestacion\servicios\personal
#   61. __init__.py
#   62. trabajador_service.py
#
# DIRECTORIO: python_forestacion\servicios\terrenos
#   63. __init__.py
#   64. plantacion_service.py
#   65. registro_forestal_service.py
#   66. tierra_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/66: __init__.py
# Directorio: .
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/66: buscar_paquete.py
# Directorio: .
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\buscar_paquete.py
# ==============================================================================

"""
Script para buscar el paquete python_forestacion desde el directorio raiz del proyecto.
Incluye funcionalidad para integrar archivos Python en cada nivel del arbol de directorios.
"""
import os
import sys
from datetime import datetime


def buscar_paquete(directorio_raiz: str, nombre_paquete: str) -> list:
    """
    Busca un paquete Python en el directorio raiz y subdirectorios.

    Args:
        directorio_raiz: Directorio desde donde iniciar la busqueda
        nombre_paquete: Nombre del paquete a buscar

    Returns:
        Lista de rutas donde se encontro el paquete
    """
    paquetes_encontrados = []

    for raiz, directorios, archivos in os.walk(directorio_raiz):
        # Verificar si el directorio actual es el paquete buscado
        nombre_dir = os.path.basename(raiz)

        if nombre_dir == nombre_paquete:
            # Verificar que sea un paquete Python (contiene __init__.py)
            if '__init__.py' in archivos:
                paquetes_encontrados.append(raiz)
                print(f"[+] Paquete encontrado: {raiz}")
            else:
                print(f"[!] Directorio encontrado pero no es un paquete Python: {raiz}")

    return paquetes_encontrados


def obtener_archivos_python(directorio: str) -> list:
    """
    Obtiene todos los archivos Python en un directorio (sin recursion).

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de archivos .py
    """
    archivos_python = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isfile(ruta_completa) and item.endswith('.py'):
                # Excluir archivos integradores para evitar recursion infinita
                if item not in ['integrador.py', 'integradorFinal.py']:
                    archivos_python.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(archivos_python)


def obtener_subdirectorios(directorio: str) -> list:
    """
    Obtiene todos los subdirectorios inmediatos de un directorio.

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de subdirectorios
    """
    subdirectorios = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isdir(ruta_completa):
                # Excluir directorios especiales
                if not item.startswith('.') and item not in ['__pycache__', 'venv', '.venv']:
                    subdirectorios.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(subdirectorios)


def leer_contenido_archivo(ruta_archivo: str) -> str:
    """
    Lee el contenido de un archivo Python.

    Args:
        ruta_archivo: Ruta completa del archivo

    Returns:
        Contenido del archivo como string
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except Exception as error:
        print(f"[!] Error al leer {ruta_archivo}: {error}")
        return f"# Error al leer este archivo: {error}\n"


def crear_archivo_integrador(directorio: str, archivos_python: list) -> bool:
    """
    Crea un archivo integrador.py con el contenido de todos los archivos Python.

    Args:
        directorio: Directorio donde crear el archivo integrador
        archivos_python: Lista de rutas de archivos Python a integrar

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_python:
        return False

    ruta_integrador = os.path.join(directorio, 'integrador.py')

    try:
        with open(ruta_integrador, 'w', encoding='utf-8') as integrador:
            # Encabezado
            integrador.write('"""\n')
            integrador.write(f"Archivo integrador generado automaticamente\n")
            integrador.write(f"Directorio: {directorio}\n")
            integrador.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador.write(f"Total de archivos integrados: {len(archivos_python)}\n")
            integrador.write('"""\n\n')

            # Integrar cada archivo
            for idx, archivo in enumerate(archivos_python, 1):
                nombre_archivo = os.path.basename(archivo)
                integrador.write(f"# {'=' * 80}\n")
                integrador.write(f"# ARCHIVO {idx}/{len(archivos_python)}: {nombre_archivo}\n")
                integrador.write(f"# Ruta: {archivo}\n")
                integrador.write(f"# {'=' * 80}\n\n")

                contenido = leer_contenido_archivo(archivo)
                integrador.write(contenido)
                integrador.write("\n\n")

        print(f"[OK] Integrador creado: {ruta_integrador}")
        print(f"     Archivos integrados: {len(archivos_python)}")
        return True

    except Exception as error:
        print(f"[!] Error al crear integrador en {directorio}: {error}")
        return False


def procesar_directorio_recursivo(directorio: str, nivel: int = 0, archivos_totales: list = None) -> list:
    """
    Procesa un directorio de forma recursiva, creando integradores en cada nivel.
    Utiliza DFS (Depth-First Search) para llegar primero a los niveles mas profundos.

    Args:
        directorio: Directorio a procesar
        nivel: Nivel de profundidad actual (para logging)
        archivos_totales: Lista acumulativa de todos los archivos procesados

    Returns:
        Lista de todos los archivos Python procesados en el arbol
    """
    if archivos_totales is None:
        archivos_totales = []

    indentacion = "  " * nivel
    print(f"{indentacion}[INFO] Procesando nivel {nivel}: {os.path.basename(directorio)}")

    # Obtener subdirectorios
    subdirectorios = obtener_subdirectorios(directorio)

    # Primero, procesar recursivamente todos los subdirectorios (DFS)
    for subdir in subdirectorios:
        procesar_directorio_recursivo(subdir, nivel + 1, archivos_totales)

    # Despues de procesar subdirectorios, procesar archivos del nivel actual
    archivos_python = obtener_archivos_python(directorio)

    if archivos_python:
        print(f"{indentacion}[+] Encontrados {len(archivos_python)} archivo(s) Python")
        crear_archivo_integrador(directorio, archivos_python)
        # Agregar archivos a la lista total
        archivos_totales.extend(archivos_python)
    else:
        print(f"{indentacion}[INFO] No hay archivos Python en este nivel")

    return archivos_totales


def crear_integrador_final(directorio_raiz: str, archivos_totales: list) -> bool:
    """
    Crea un archivo integradorFinal.py con TODO el codigo fuente de todas las ramas.

    Args:
        directorio_raiz: Directorio donde crear el archivo integrador final
        archivos_totales: Lista completa de todos los archivos Python procesados

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_totales:
        print("[!] No hay archivos para crear el integrador final")
        return False

    ruta_integrador_final = os.path.join(directorio_raiz, 'integradorFinal.py')

    # Organizar archivos por directorio para mejor estructura
    archivos_por_directorio = {}
    for archivo in archivos_totales:
        directorio = os.path.dirname(archivo)
        if directorio not in archivos_por_directorio:
            archivos_por_directorio[directorio] = []
        archivos_por_directorio[directorio].append(archivo)

    try:
        with open(ruta_integrador_final, 'w', encoding='utf-8') as integrador_final:
            # Encabezado principal
            integrador_final.write('"""\n')
            integrador_final.write("INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write(f"Directorio raiz: {directorio_raiz}\n")
            integrador_final.write(f"Fecha de generacion: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write(f"Total de archivos integrados: {len(archivos_totales)}\n")
            integrador_final.write(f"Total de directorios procesados: {len(archivos_por_directorio)}\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write('"""\n\n')

            # Tabla de contenidos
            integrador_final.write("# " + "=" * 78 + "\n")
            integrador_final.write("# TABLA DE CONTENIDOS\n")
            integrador_final.write("# " + "=" * 78 + "\n\n")

            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)
                    integrador_final.write(f"#   {contador_global}. {nombre_archivo}\n")
                    contador_global += 1
                integrador_final.write("#\n")

            integrador_final.write("\n\n")

            # Contenido completo organizado por directorio
            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)

                # Separador de directorio
                integrador_final.write("\n" + "#" * 80 + "\n")
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                integrador_final.write("#" * 80 + "\n\n")

                # Procesar cada archivo del directorio
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)

                    integrador_final.write(f"# {'=' * 78}\n")
                    integrador_final.write(f"# ARCHIVO {contador_global}/{len(archivos_totales)}: {nombre_archivo}\n")
                    integrador_final.write(f"# Directorio: {dir_relativo}\n")
                    integrador_final.write(f"# Ruta completa: {archivo}\n")
                    integrador_final.write(f"# {'=' * 78}\n\n")

                    contenido = leer_contenido_archivo(archivo)
                    integrador_final.write(contenido)
                    integrador_final.write("\n\n")

                    contador_global += 1

            # Footer
            integrador_final.write("\n" + "#" * 80 + "\n")
            integrador_final.write("# FIN DEL INTEGRADOR FINAL\n")
            integrador_final.write(f"# Total de archivos: {len(archivos_totales)}\n")
            integrador_final.write(f"# Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write("#" * 80 + "\n")

        print(f"\n[OK] Integrador final creado: {ruta_integrador_final}")
        print(f"     Total de archivos integrados: {len(archivos_totales)}")
        print(f"     Total de directorios procesados: {len(archivos_por_directorio)}")

        # Mostrar tamanio del archivo
        tamanio = os.path.getsize(ruta_integrador_final)
        if tamanio < 1024:
            tamanio_str = f"{tamanio} bytes"
        elif tamanio < 1024 * 1024:
            tamanio_str = f"{tamanio / 1024:.2f} KB"
        else:
            tamanio_str = f"{tamanio / (1024 * 1024):.2f} MB"
        print(f"     Tamanio del archivo: {tamanio_str}")

        return True

    except Exception as error:
        print(f"[!] Error al crear integrador final: {error}")
        return False


def integrar_arbol_directorios(directorio_raiz: str) -> None:
    """
    Inicia el proceso de integracion para todo el arbol de directorios.

    Args:
        directorio_raiz: Directorio raiz desde donde comenzar
    """
    print("\n" + "=" * 80)
    print("INICIANDO INTEGRACION DE ARCHIVOS PYTHON")
    print("=" * 80)
    print(f"Directorio raiz: {directorio_raiz}\n")

    # Procesar directorios y obtener lista de todos los archivos
    archivos_totales = procesar_directorio_recursivo(directorio_raiz)

    print("\n" + "=" * 80)
    print("INTEGRACION POR NIVELES COMPLETADA")
    print("=" * 80)

    # Crear integrador final con todos los archivos
    if archivos_totales:
        print("\n" + "=" * 80)
        print("CREANDO INTEGRADOR FINAL")
        print("=" * 80)
        crear_integrador_final(directorio_raiz, archivos_totales)

    print("\n" + "=" * 80)
    print("PROCESO COMPLETO FINALIZADO")
    print("=" * 80)


def main():
    """Funcion principal del script."""
    # Obtener el directorio raiz del proyecto (donde esta este script)
    directorio_raiz = os.path.dirname(os.path.abspath(__file__))

    # Verificar argumentos de linea de comandos
    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()

        if comando == "integrar":
            # Modo de integracion de archivos
            if len(sys.argv) > 2:
                directorio_objetivo = sys.argv[2]
                if not os.path.isabs(directorio_objetivo):
                    directorio_objetivo = os.path.join(directorio_raiz, directorio_objetivo)
            else:
                directorio_objetivo = directorio_raiz

            if not os.path.isdir(directorio_objetivo):
                print(f"[!] El directorio no existe: {directorio_objetivo}")
                return 1

            integrar_arbol_directorios(directorio_objetivo)
            return 0

        elif comando == "help" or comando == "--help" or comando == "-h":
            print("Uso: python buscar_paquete.py [COMANDO] [OPCIONES]")
            print("")
            print("Comandos disponibles:")
            print("  (sin argumentos)     Busca el paquete python_forestacion")
            print("  integrar [DIR]       Integra archivos Python en el arbol de directorios")
            print("                       DIR: directorio raiz (por defecto: directorio actual)")
            print("  help                 Muestra esta ayuda")
            print("")
            print("Ejemplos:")
            print("  python buscar_paquete.py")
            print("  python buscar_paquete.py integrar")
            print("  python buscar_paquete.py integrar python_forestacion")
            return 0

        else:
            print(f"[!] Comando desconocido: {comando}")
            print("    Use 'python buscar_paquete.py help' para ver los comandos disponibles")
            return 1

    # Modo por defecto: buscar paquete
    print(f"[INFO] Buscando desde: {directorio_raiz}")
    print(f"[INFO] Buscando paquete: python_forestacion")
    print("")

    # Buscar el paquete
    paquetes = buscar_paquete(directorio_raiz, "python_forestacion")

    print("")
    if paquetes:
        print(f"[OK] Se encontraron {len(paquetes)} paquete(s):")
        for paquete in paquetes:
            print(f"  - {paquete}")

            # Mostrar estructura basica del paquete
            print(f"    Contenido:")
            try:
                contenido = os.listdir(paquete)
                for item in sorted(contenido)[:10]:  # Mostrar primeros 10 items
                    ruta_item = os.path.join(paquete, item)
                    if os.path.isdir(ruta_item):
                        print(f"      [DIR]  {item}")
                    else:
                        print(f"      [FILE] {item}")
                if len(contenido) > 10:
                    print(f"      ... y {len(contenido) - 10} items mas")
            except PermissionError:
                print(f"      [!] Sin permisos para leer el directorio")
    else:
        print("[!] No se encontro el paquete python_forestacion")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

# ==============================================================================
# ARCHIVO 3/66: main.py
# Directorio: .
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\main.py
# ==============================================================================

from datetime import date
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
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



################################################################################
# DIRECTORIO: python_forestacion
################################################################################

# ==============================================================================
# ARCHIVO 4/66: __init__.py
# Directorio: python_forestacion
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion\entidades
################################################################################

# ==============================================================================
# ARCHIVO 5/66: __init__.py
# Directorio: python_forestacion\entidades
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\__init__.py
# ==============================================================================

from . import cultivos
from . import personal
from . import terrenos



################################################################################
# DIRECTORIO: python_forestacion\entidades\cultivos
################################################################################

# ==============================================================================
# ARCHIVO 6/66: __init__.py
# Directorio: python_forestacion\entidades\cultivos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 7/66: arbol.py
# Directorio: python_forestacion\entidades\cultivos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\arbol.py
# ==============================================================================

from threading import Lock
from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo):
    _cant_arboles = 0
    _lock = Lock()  # Para incrementar de forma segura en entornos concurrentes

    def __init__(self, agua: int, altura: float, superficie: float):
        with Arbol._lock:
            Arbol._cant_arboles += 1
            self._id = Arbol._cant_arboles

        self._agua = agua
        self._altura = altura
        self._superficie = superficie

    # Getters y Setters
    @property
    def id(self) -> int:
        return self._id

    def get_agua(self) -> int:
        return self._agua

    def set_agua(self, agua: int):
        self._agua = agua

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, valor: float):
        self._altura = valor

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float):
        self._superficie = superficie

    @classmethod
    def get_cant_arboles(cls) -> int:
        return cls._cant_arboles


# ==============================================================================
# ARCHIVO 8/66: cultivo.py
# Directorio: python_forestacion\entidades\cultivos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\cultivo.py
# ==============================================================================

from abc import ABC, abstractmethod

class Cultivo(ABC):
    EDAD_MAXIMA = 20  # Constante de clase

    @abstractmethod
    def get_superficie(self) -> float:
        pass

    @abstractmethod
    def get_agua(self) -> int:
        pass

    @abstractmethod
    def set_agua(self, agua: int):
        pass


# ==============================================================================
# ARCHIVO 9/66: hortaliza.py
# Directorio: python_forestacion\entidades\cultivos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\hortaliza.py
# ==============================================================================

from abc import ABC, abstractmethod

class Cultivo(ABC):
    EDAD_MAXIMA = 20

    @abstractmethod
    def get_superficie(self) -> float:
        pass

    @abstractmethod
    def get_agua(self) -> float:
        pass

    @abstractmethod
    def set_agua(self, agua: float):
        pass

    # Método absorber_agua para riego
    def absorber_agua(self, cantidad: float):
        # Suma la cantidad de agua disponible
        self.set_agua(self.get_agua() + cantidad)


class Hortaliza(Cultivo):
    def __init__(self, agua: float, superficie: float, requiere_invernadero: bool):
        self._agua = agua
        self._superficie = superficie
        self._requiere_invernadero = requiere_invernadero
        self._altura = 0.1  # Altura por defecto para compatibilidad con mostrar_datos

    # Getters y Setters
    def get_agua(self) -> float:
        return self._agua

    def set_agua(self, agua: float):
        self._agua = agua

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float):
        self._superficie = superficie

    def get_requiere_invernadero(self) -> bool:
        return self._requiere_invernadero

    def get_altura(self) -> float:
        # Para compatibilidad con mostrar_datos
        return self._altura



# ==============================================================================
# ARCHIVO 10/66: lechuga.py
# Directorio: python_forestacion\entidades\cultivos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\lechuga.py
# ==============================================================================

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza

class Lechuga(Hortaliza):
    def __init__(self, variedad: str):
        # Llama al constructor de Hortaliza con valores fijos
        # agua = 1, superficie = 0.10, requiere_invernadero = True
        super().__init__(agua=1, superficie=0.10, requiere_invernadero=True)
        self._variedad = variedad

    # Getter de la variedad
    def get_variedad(self) -> str:
        return self._variedad

    # Getter de altura (aunque sea opcional para hortalizas)
    def get_altura(self) -> float:
        # Podés devolver un valor fijo o un atributo si Hortaliza lo tiene
        return getattr(self, "_altura", 0.1)

    # Getter de agua para riego
    def get_agua(self) -> float:
        return getattr(self, "_agua", 1.0)

    # Método absorber_agua para compatibilidad con servicios de riego
    def absorber_agua(self, cantidad: float):
        # Sumar agua disponible
        self._agua = getattr(self, "_agua", 1.0) + cantidad


# ==============================================================================
# ARCHIVO 11/66: olivo.py
# Directorio: python_forestacion\entidades\cultivos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\olivo.py
# ==============================================================================

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna  

class Olivo(Arbol):
    def __init__(self, tipo: TipoAceituna):
        # Llama al constructor de Arbol con valores fijos
        # agua = 5, altura = 0.5, superficie = 3
        super().__init__(agua=5, altura=0.5, superficie=3.0)
        self._fruto = tipo

    # Getter del fruto
    def get_fruto(self) -> TipoAceituna:
        return self._fruto

    # Getter de altura para compatibilidad con mostrar_datos
    def get_altura(self) -> float:
        return self._altura

    # Getter de agua
    def get_agua(self) -> float:
        return self._agua

    # Método absorber_agua para riego
    def absorber_agua(self, cantidad: float):
        self._agua += cantidad



# ==============================================================================
# ARCHIVO 12/66: pino.py
# Directorio: python_forestacion\entidades\cultivos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\pino.py
# ==============================================================================

from python_forestacion.entidades.cultivos.arbol import Arbol

class Pino(Arbol):
    def __init__(self, variedad: str):
        # Llama al constructor de Arbol con valores fijos:
        # agua = 2, altura = 1, superficie = 2
        super().__init__(agua=2, altura=1.0, superficie=2.0)
        self._variedad = variedad

    # Getter de la variedad
    def get_variedad(self) -> str:
        return self._variedad

    # Getter de altura para mostrar datos
    def get_altura(self) -> float:
        return self._altura

    # Getter de agua (opcional, si tu servicio lo usa)
    def get_agua(self) -> float:
        return self._agua


# ==============================================================================
# ARCHIVO 13/66: tipo_aceituna.py
# Directorio: python_forestacion\entidades\cultivos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\tipo_aceituna.py
# ==============================================================================

from enum import Enum

class TipoAceituna(Enum):
    NEGRA = "NEGRA"
    VERDE = "VERDE"
    ROJA = "ROJA"


# ==============================================================================
# ARCHIVO 14/66: zanahoria.py
# Directorio: python_forestacion\entidades\cultivos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\cultivos\zanahoria.py
# ==============================================================================

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza

class Zanahoria(Hortaliza):
    """
    Entidad Zanahoria - solo contiene datos/estado.
    La lógica de comportamiento está en ZanahoriaService.
    """

    def __init__(self, is_baby: bool):
        super().__init__(agua=0, sup=0.15, invernadero=False)
        self.is_baby_carrot = is_baby

    def is_baby_carrot(self) -> bool:
        return self.is_baby_carrot

    def set_baby_carrot(self, baby_carrot: bool):
        self.is_baby_carrot = baby_carrot



################################################################################
# DIRECTORIO: python_forestacion\entidades\personal
################################################################################

# ==============================================================================
# ARCHIVO 15/66: __init__.py
# Directorio: python_forestacion\entidades\personal
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\personal\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 16/66: apto_medico.py
# Directorio: python_forestacion\entidades\personal
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\personal\apto_medico.py
# ==============================================================================

from datetime import date

class AptoMedico:
    """
    Entidad que representa la certificación médica de un trabajador.
    Contiene solo el estado (datos) del apto médico.

    REFACTORIZADO: Extraída de clase interna de Trabajador a clase independiente.
    """

    def __init__(self, apto: bool, fecha_emision: date, observaciones: str):
        """
        Constructor completo para crear un apto médico.

        :param apto: Estado de aptitud (True = apto, False = no apto)
        :param fecha_emision: Fecha de emisión del certificado médico
        :param observaciones: Observaciones médicas del certificado
        """
        self.apto = apto
        self.fecha_emision = fecha_emision
        self.observaciones = observaciones

    # --- Métodos de acceso (Getters y Setters) ---
    def esta_apto(self) -> bool:
        """Verifica si el trabajador está apto médicamente."""
        return self.apto

    def set_apto(self, apto: bool) -> None:
        """Define el estado de aptitud médica."""
        self.apto = apto

    def get_fecha_emision(self) -> date:
        """Devuelve la fecha de emisión del certificado."""
        return self.fecha_emision

    def set_fecha_emision(self, fecha_emision: date) -> None:
        """Modifica la fecha de emisión del certificado."""
        self.fecha_emision = fecha_emision

    def get_observaciones(self) -> str:
        """Devuelve las observaciones médicas."""
        return self.observaciones

    def set_observaciones(self, observaciones: str) -> None:
        """Modifica las observaciones médicas."""
        self.observaciones = observaciones

    def get_resumen(self) -> str:
        """Genera un resumen legible del apto médico."""
        return f"Apto: {self.apto} | Fecha: {self.fecha_emision} | Obs: {self.observaciones}"


# ==============================================================================
# ARCHIVO 17/66: herramienta.py
# Directorio: python_forestacion\entidades\personal
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\personal\herramienta.py
# ==============================================================================

class Herramienta:
    def __init__(self, id: int, nombre: str, certificado_hys: bool):
        self._id = id
        self.nombre = nombre
        self.certificado_hys = certificado_hys

    @property
    def id(self):
        return self._id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_certificado(self):
        return self.certificado_hys

    def set_certificado(self, certificado_hys: bool):
        self.certificado_hys = certificado_hys


# ==============================================================================
# ARCHIVO 18/66: tarea.py
# Directorio: python_forestacion\entidades\personal
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\personal\tarea.py
# ==============================================================================

from datetime import date

class Tarea:
    def __init__(self, id: int, fecha: date, descripcion: str):
        self._id = id
        self._fecha = fecha
        self._descripcion = descripcion
        self._estado = False  # Inicialmente false como en Java

    # Getters y Setters
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def fecha(self) -> date:
        return self._fecha

    @fecha.setter
    def fecha(self, value: date):
        self._fecha = value

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value: str):
        self._descripcion = value

    @property
    def estado(self) -> bool:
        return self._estado

    @estado.setter
    def estado(self, value: bool):
        self._estado = value


# ==============================================================================
# ARCHIVO 19/66: trabajador.py
# Directorio: python_forestacion\entidades\personal
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\personal\trabajador.py
# ==============================================================================

from datetime import date
from typing import List
from python_forestacion.entidades.personal.apto_medico import AptoMedico  
from python_forestacion.entidades.personal.tarea import Tarea  

class Trabajador:
    def __init__(self, dni: int, nombre: str, tareas: List[Tarea]):
        self.dni = dni
        self._nombre = nombre
        self._tareas = list(tareas)  # Copia defensiva
        # Inicializar apto médico por defecto
        self._apto_medico = AptoMedico(True, date.today(), "Estado de salud: bueno")

    # Getters y Setters
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        self._nombre = value

    @property
    def apto_medico(self) -> AptoMedico:
        return self._apto_medico

    @apto_medico.setter
    def apto_medico(self, value: AptoMedico):
        self._apto_medico = value

    @property
    def tareas(self) -> List[Tarea]:
        # Retorna copia para proteger estado interno (similar a Collections.unmodifiableList)
        return list(self._tareas)

    @tareas.setter
    def tareas(self, value: List[Tarea]):
        self._tareas = list(value)  # Copia defensiva

    # Método de conveniencia para asignar apto médico
    def asignar_apto_medico(self, apto: bool, fecha_emision: date, observaciones: str):
        self._apto_medico = AptoMedico(apto, fecha_emision, observaciones)



################################################################################
# DIRECTORIO: python_forestacion\entidades\terrenos
################################################################################

# ==============================================================================
# ARCHIVO 20/66: __init__.py
# Directorio: python_forestacion\entidades\terrenos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\terrenos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 21/66: plantacion.py
# Directorio: python_forestacion\entidades\terrenos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\terrenos\plantacion.py
# ==============================================================================

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador

class Plantacion:
    """
    Clase que representa una plantación o finca.
    Contiene solo el estado (datos) de la plantación.
    La lógica de plantar, regar, etc. está en PlantacionService.
    """

    def __init__(self, id_: int, nombre: str, agua: int, tierra: "Tierra"):
        # Import dentro del método para romper circular import
        from python_forestacion.entidades.terrenos.tierra import Tierra
        self._id = id_
        self._nombre = nombre
        self._agua_disponible = agua
        self._situada_en: Tierra = tierra
        self._cultivos: List["Cultivo"] = []
        self._trabajadores: List["Trabajador"] = []

    # --- Getters y Setters ---
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        self._nombre = value

    @property
    def agua_disponible(self) -> int:
        return self._agua_disponible

    @agua_disponible.setter
    def agua_disponible(self, value: int):
        self._agua_disponible = value

    @property
    def situada_en(self) -> "Tierra":
        # Import dentro del getter para romper circular import
        from python_forestacion.entidades.terrenos.tierra import Tierra
        return self._situada_en

    @situada_en.setter
    def situada_en(self, value: "Tierra"):
        from python_forestacion.entidades.terrenos.tierra import Tierra
        self._situada_en = value

    # --- Manejo de listas ---
    @property
    def cultivos(self) -> List["Cultivo"]:
        return list(self._cultivos)

    @cultivos.setter
    def cultivos(self, value: List["Cultivo"]):
        self._cultivos = list(value)

    @property
    def trabajadores(self) -> List["Trabajador"]:
        return list(self._trabajadores)

    @trabajadores.setter
    def trabajadores(self, value: List["Trabajador"]):
        self._trabajadores = list(value)

    # --- Métodos internos ---
    def get_cultivos_interno(self) -> List["Cultivo"]:
        return self._cultivos

    def get_trabajadores_interno(self) -> List["Trabajador"]:
        return self._trabajadores


# ==============================================================================
# ARCHIVO 22/66: registro_forestal.py
# Directorio: python_forestacion\entidades\terrenos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\terrenos\registro_forestal.py
# ==============================================================================

from dataclasses import dataclass
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion


@dataclass
class RegistroForestal:
    """
    Entidad que representa un registro forestal catastral.
    Contiene solo el estado (datos) del registro.
    La lógica de persistencia está en RegistroForestalService.
    """

    id_padron: int
    tierra: Tierra
    plantacion: Plantacion
    propietario: str
    avaluo: float

    def __init__(self, id_padron: int, tierra: Tierra, plantacion: Plantacion,
                 propietario: str, avaluo: float):
        self.id_padron = id_padron
        self.tierra = tierra
        self.plantacion = plantacion
        self.propietario = propietario
        self.avaluo = avaluo

    # Getters y Setters
    def get_plantacion(self) -> Plantacion:
        return self.plantacion

    def get_id_padron(self) -> int:
        return self.id_padron

    def set_id_padron(self, id_padron: int):
        self.id_padron = id_padron

    def get_tierra(self) -> Tierra:
        return self.tierra

    def get_propietario(self) -> str:
        return self.propietario

    def set_propietario(self, propietario: str):
        self.propietario = propietario

    def get_avaluo(self) -> float:
        return self.avaluo

    def set_avaluo(self, avaluo: float):
        self.avaluo = avaluo


# ==============================================================================
# ARCHIVO 23/66: tierra.py
# Directorio: python_forestacion\entidades\terrenos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\entidades\terrenos\tierra.py
# ==============================================================================

from typing import Optional, TYPE_CHECKING

# Solo para anotaciones de tipo estáticas
if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion

class Tierra:
    """
    Clase que representa una tierra o parcela.
    Contiene solo el estado (datos) de la tierra.
    La lógica de negocio se maneja en los servicios correspondientes.
    """

    def __init__(self, id_padron_catastral: int, superficie: float, domicilio: str):
        self._id = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca: Optional["Plantacion"] = None  

    
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def superficie(self) -> float:
        return self._superficie

    @superficie.setter
    def superficie(self, value: float):
        self._superficie = value

    @property
    def domicilio(self) -> str:
        return self._domicilio

    @domicilio.setter
    def domicilio(self, value: str):
        self._domicilio = value

    @property
    def finca(self) -> Optional["Plantacion"]:
        from python_forestacion.entidades.terrenos.plantacion import Plantacion
        return self._finca

    @finca.setter
    def finca(self, value: "Plantacion"):
        from python_forestacion.entidades.terrenos.plantacion import Plantacion
        self._finca = value



################################################################################
# DIRECTORIO: python_forestacion\excepciones
################################################################################

# ==============================================================================
# ARCHIVO 24/66: __init__.py
# Directorio: python_forestacion\excepciones
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\excepciones\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 25/66: agua_agotada_excepcion.py
# Directorio: python_forestacion\excepciones
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\excepciones\agua_agotada_excepcion.py
# ==============================================================================

from python_forestacion.excepciones.forestacion_excepcion import ForestacionException
from python_forestacion.excepciones.mensajes_excepcion import MensajesException


class AguaAgotadaException(ForestacionException):
    """
    Excepción lanzada cuando el agua disponible en la plantación
    es insuficiente para riego.
    """

    def __init__(self, agua_disponible: float = 0, agua_minima: float = 10):
        # Llamada al constructor de la excepción base con mensajes
        mensaje_detallado = MensajesException.get_agua_agotada_detallado_message(
            agua_disponible, agua_minima
        )
        super().__init__(
            MensajesException.ERROR_CODE_01,
            MensajesException.ERROR_01_AGUA_AGOTADA,
            mensaje_detallado
        )
        self._agua_disponible = agua_disponible
        self._agua_minima = agua_minima

    @property
    def agua_disponible(self) -> float:
        return self._agua_disponible

    @property
    def agua_minima(self) -> float:
        return self._agua_minima


# ==============================================================================
# ARCHIVO 26/66: forestacion_excepcion.py
# Directorio: python_forestacion\excepciones
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\excepciones\forestacion_excepcion.py
# ==============================================================================

class ForestacionException(Exception):
    """
    Excepción base para todas las excepciones del sistema de forestación.
    Proporciona una jerarquía común y códigos de error estandarizados.
    """

    def __init__(self, error_code: str, message: str, user_message: str = None, cause: Exception = None):
        """
        Constructor con mensaje técnico y opcional mensaje para usuario y causa raíz.
        """
        super().__init__(message)
        self._error_code = error_code
        self._user_message = user_message if user_message is not None else message
        self.__cause__ = cause  # Para mantener la causa original si existe

    @property
    def error_code(self) -> str:
        return self._error_code

    @property
    def user_message(self) -> str:
        return self._user_message

    def get_full_message(self) -> str:
        """
        Retorna el mensaje completo formateado: código + mensaje.
        """
        base_msg = f"{self._error_code} - {self._user_message}"
        if self.__cause__:
            base_msg += f" | Causa: {str(self.__cause__)}"
        return base_msg

    def __str__(self):
        return self.get_full_message()


# ==============================================================================
# ARCHIVO 27/66: mensajes_excepcion.py
# Directorio: python_forestacion\excepciones
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\excepciones\mensajes_excepcion.py
# ==============================================================================

class MensajesException:
    # ============================================
    # CÓDIGOS DE ERROR
    # ============================================
    ERROR_CODE_00 = "ERROR 00"
    ERROR_CODE_01 = "ERROR 01"
    ERROR_CODE_02 = "ERROR 02"
    ERROR_CODE_03 = "ERROR 03"
    ERROR_CODE_04 = "ERROR 04"
    ERROR_CODE_05 = "ERROR 05"
    ERROR_CODE_06 = "ERROR 06"
    ERROR_CODE_07 = "ERROR 07"

    # ============================================
    # ERRORES GENERALES
    # ============================================
    ERROR_00_NO_IDENTIFICADO = "Se produjo un error no identificado en el sistema"

    # ============================================
    # ERRORES DE RIEGO Y AGUA
    # ============================================
    ERROR_01_AGUA_AGOTADA = "Se agotó el agua disponible en la finca"
    ERROR_01_AGUA_AGOTADA_USER_MESSAGE = (
        "No hay suficiente agua disponible para continuar el riego. Nivel de agua crítico."
    )

    @staticmethod
    def get_agua_agotada_detallado_message(agua_disponible: float, agua_minima: float) -> str:
        return f"Agua insuficiente para riego. Disponible: {agua_disponible:.2f} L, Mínimo requerido: {agua_minima:.2f} L"

    # ============================================
    # ERRORES DE SUPERFICIE Y PLANTACIÓN
    # ============================================
    ERROR_02_SUPERFICIE_INSUFICIENTE_PREFIX = "No se pudo plantar: "
    ERROR_02_SUPERFICIE_INSUFICIENTE_SUFFIX = " porque no queda superficie disponible en la finca"

    @staticmethod
    def get_superficie_insuficiente_message(cultivo: str) -> str:
        return MensajesException.ERROR_02_SUPERFICIE_INSUFICIENTE_PREFIX + cultivo + \
               MensajesException.ERROR_02_SUPERFICIE_INSUFICIENTE_SUFFIX

    @staticmethod
    def get_superficie_insuficiente_user_message(cultivo: str) -> str:
        return f"No hay suficiente espacio en la plantación para cultivar {cultivo}"

    @staticmethod
    def get_superficie_insuficiente_detallado_message(cultivo: str, superficie_requerida: float, superficie_disponible: float) -> str:
        return f"No se puede plantar {cultivo}. Requiere: {superficie_requerida:.2f} m², Disponible: {superficie_disponible:.2f} m²"

    # ============================================
    # ERRORES DE PERSISTENCIA
    # ============================================
    ERROR_03_ARCHIVO_NO_ENCONTRADO_ESCRITURA = "No se encontró la ruta del archivo para escritura"
    ERROR_04_IO_ESCRITURA = "Se produjo un error de entrada/salida durante la escritura"
    ERROR_05_ARCHIVO_NO_ENCONTRADO_LECTURA = "No se encontró el archivo para lectura"
    ERROR_06_IO_LECTURA = "Se produjo un error de entrada/salida durante la lectura"
    ERROR_07_CLASS_NOT_FOUND = "Error de conversión de clase durante la deserialización"

    @staticmethod
    def get_archivo_no_encontrado_message(nombre_archivo: str) -> str:
        return f"No se encontró el archivo: {nombre_archivo}"

    @staticmethod
    def get_io_error_message(nombre_archivo: str) -> str:
        return f"Error de entrada/salida al procesar el archivo: {nombre_archivo}"

    @staticmethod
    def get_class_not_found_message(nombre_archivo: str) -> str:
        return f"Error de deserialización. Verifique la versión de las clases en: {nombre_archivo}"

    # ============================================
    # MENSAJES DE OPERACIONES EXITOSAS
    # ============================================
    @staticmethod
    def get_persistencia_exitosa_message(propietario: str) -> str:
        return f"Registro persistido exitosamente: {propietario}"

    @staticmethod
    def get_lectura_exitosa_message(propietario: str) -> str:
        return f"Registro leído exitosamente: {propietario}"


# ==============================================================================
# ARCHIVO 28/66: persistencia_excepcion.py
# Directorio: python_forestacion\excepciones
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\excepciones\persistencia_excepcion.py
# ==============================================================================

from enum import Enum
from python_forestacion.excepciones.forestacion_excepcion import ForestacionException
from python_forestacion.excepciones.mensajes_excepcion import MensajesException


class PersistenciaException(ForestacionException):
    class TipoOperacion(Enum):
        ESCRITURA = "ESCRITURA"
        LECTURA = "LECTURA"

    def __init__(self, error_code: str, message: str, user_message: str, tipo_operacion: 'PersistenciaException.TipoOperacion', cause: Exception = None):
        super().__init__(error_code, message, user_message)
        self.tipo_operacion = tipo_operacion
        self.__cause__ = cause  # Para mantener la referencia de la causa original

    @classmethod
    def archivo_no_encontrado(cls, tipo_operacion: 'PersistenciaException.TipoOperacion', nombre_archivo: str, cause: Exception = None):
        if tipo_operacion == cls.TipoOperacion.ESCRITURA:
            return cls(
                MensajesException.ERROR_CODE_03,
                MensajesException.ERROR_03_ARCHIVO_NO_ENCONTRADO_ESCRITURA,
                MensajesException.get_archivo_no_encontrado_message(nombre_archivo),
                tipo_operacion,
                cause
            )
        else:
            return cls(
                MensajesException.ERROR_CODE_05,
                MensajesException.ERROR_05_ARCHIVO_NO_ENCONTRADO_LECTURA,
                MensajesException.get_archivo_no_encontrado_message(nombre_archivo),
                tipo_operacion,
                cause
            )

    @classmethod
    def from_io_error(cls, tipo_operacion: 'PersistenciaException.TipoOperacion', nombre_archivo: str, io_exception: Exception):
        if tipo_operacion == cls.TipoOperacion.ESCRITURA:
            return cls(
                MensajesException.ERROR_CODE_04,
                MensajesException.ERROR_04_IO_ESCRITURA,
                MensajesException.get_io_error_message(nombre_archivo),
                tipo_operacion,
                io_exception
            )
        else:
            return cls(
                MensajesException.ERROR_CODE_06,
                MensajesException.ERROR_06_IO_LECTURA,
                MensajesException.get_io_error_message(nombre_archivo),
                tipo_operacion,
                io_exception
            )

    @classmethod
    def from_class_not_found(cls, nombre_archivo: str, cause: Exception):
        return cls(
            MensajesException.ERROR_CODE_07,
            MensajesException.ERROR_07_CLASS_NOT_FOUND,
            MensajesException.get_class_not_found_message(nombre_archivo),
            cls.TipoOperacion.LECTURA,
            cause
        )


# ==============================================================================
# ARCHIVO 29/66: superficie_insuficiente_excepcion.py
# Directorio: python_forestacion\excepciones
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\excepciones\superficie_insuficiente_excepcion.py
# ==============================================================================

from python_forestacion.excepciones.forestacion_excepcion import ForestacionException
from python_forestacion.excepciones.mensajes_excepcion import MensajesException




class SuperficieInsuficienteException(ForestacionException):
    def __init__(self, tipo_cultivo: str, superficie_requerida: float = 0, superficie_disponible: float = 0):
        if superficie_requerida == 0 and superficie_disponible == 0:
            user_message = MensajesException.getSuperficieInsuficienteUserMessage(tipo_cultivo)
        else:
            user_message = MensajesException.getSuperficieInsuficienteDetalladoMessage(
                tipo_cultivo, superficie_requerida, superficie_disponible
            )

        super().__init__(
            MensajesException.ERROR_CODE_02,
            MensajesException.getSuperficieInsuficienteMessage(tipo_cultivo),
            user_message
        )

        self._tipo_cultivo = tipo_cultivo
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

    # Propiedades de solo lectura
    @property
    def tipo_cultivo(self) -> str:
        return self._tipo_cultivo

    @property
    def superficie_requerida(self) -> float:
        return self._superficie_requerida

    @property
    def superficie_disponible(self) -> float:
        return self._superficie_disponible



################################################################################
# DIRECTORIO: python_forestacion\patrones
################################################################################

# ==============================================================================
# ARCHIVO 30/66: __init__.py
# Directorio: python_forestacion\patrones
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion\patrones\Factory
################################################################################

# ==============================================================================
# ARCHIVO 31/66: __init__.py
# Directorio: python_forestacion\patrones\Factory
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Factory\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 32/66: cultivo_Factory.py
# Directorio: python_forestacion\patrones\Factory
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Factory\cultivo_Factory.py
# ==============================================================================

from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo, TipoAceituna
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

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




################################################################################
# DIRECTORIO: python_forestacion\patrones\Observer
################################################################################

# ==============================================================================
# ARCHIVO 33/66: __init__.py
# Directorio: python_forestacion\patrones\Observer
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Observer\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 34/66: observador_plantacion.py
# Directorio: python_forestacion\patrones\Observer
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Observer\observador_plantacion.py
# ==============================================================================

class ObservadorPlantacion:
    """Observador que reacciona ante cambios en la plantación."""
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"[{self.nombre}] recibió notificación: {mensaje}")


# ==============================================================================
# ARCHIVO 35/66: sujeto_plantacion.py
# Directorio: python_forestacion\patrones\Observer
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Observer\sujeto_plantacion.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: python_forestacion\patrones\Singleton
################################################################################

# ==============================================================================
# ARCHIVO 36/66: __init__.py
# Directorio: python_forestacion\patrones\Singleton
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Singleton\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 37/66: registro_forestal_service.py
# Directorio: python_forestacion\patrones\Singleton
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Singleton\registro_forestal_service.py
# ==============================================================================

from python_forestacion.entidades.terrenos.tierra import Tierra

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



################################################################################
# DIRECTORIO: python_forestacion\patrones\Strategy
################################################################################

# ==============================================================================
# ARCHIVO 38/66: __init__.py
# Directorio: python_forestacion\patrones\Strategy
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Strategy\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 39/66: contexto_cultivo.py
# Directorio: python_forestacion\patrones\Strategy
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Strategy\contexto_cultivo.py
# ==============================================================================

class ContextoCultivo:
    """Contexto que permite cambiar de estrategia según el tipo de cultivo."""
    def __init__(self, estrategia):
        self._estrategia = estrategia

    def set_estrategia(self, nueva_estrategia):
        self._estrategia = nueva_estrategia

    def ejecutar_estrategia(self, cultivo):
        self._estrategia.ejecutar(cultivo)

# ==============================================================================
# ARCHIVO 40/66: estrategia_cultivo.py
# Directorio: python_forestacion\patrones\Strategy
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Strategy\estrategia_cultivo.py
# ==============================================================================

from abc import ABC, abstractmethod

class EstrategiaCultivo(ABC):
    """Interfaz base para estrategias de cultivo."""
    @abstractmethod
    def ejecutar(self, cultivo):
        pass


# ==============================================================================
# ARCHIVO 41/66: estrategia_fertilizacion_manual.py
# Directorio: python_forestacion\patrones\Strategy
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Strategy\estrategia_fertilizacion_manual.py
# ==============================================================================

from python_forestacion.patrones.Strategy.estrategia_cultivo import EstrategiaCultivo

class EstrategiaFertilizacionManual(EstrategiaCultivo):
    def ejecutar(self, cultivo):
        print(f"Fertilización manual aplicada al cultivo {cultivo.nombre}.")


# ==============================================================================
# ARCHIVO 42/66: estrategia_riego_automatizado.py
# Directorio: python_forestacion\patrones\Strategy
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\patrones\Strategy\estrategia_riego_automatizado.py
# ==============================================================================

from python_forestacion.patrones.Strategy.estrategia_cultivo import EstrategiaCultivo

class EstrategiaRiegoAutomatizado(EstrategiaCultivo):
    def ejecutar(self, cultivo):
        print(f"Riego automatizado ejecutado para el cultivo {cultivo.nombre}.")



################################################################################
# DIRECTORIO: python_forestacion\riego
################################################################################

# ==============================================================================
# ARCHIVO 43/66: __init__.py
# Directorio: python_forestacion\riego
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\riego\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion\riego\control
################################################################################

# ==============================================================================
# ARCHIVO 44/66: __init__.py
# Directorio: python_forestacion\riego\control
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\riego\control\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 45/66: control_riego_task.py
# Directorio: python_forestacion\riego\control
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\riego\control\control_riego_task.py
# ==============================================================================

import time
from python_forestacion.excepciones.agua_agotada_excepcion import AguaAgotadaException


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



################################################################################
# DIRECTORIO: python_forestacion\riego\sensores
################################################################################

# ==============================================================================
# ARCHIVO 46/66: __init__.py
# Directorio: python_forestacion\riego\sensores
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\riego\sensores\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 47/66: humedad_reader_task.py
# Directorio: python_forestacion\riego\sensores
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\riego\sensores\humedad_reader_task.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 48/66: temperatura_reader_task.py
# Directorio: python_forestacion\riego\sensores
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\riego\sensores\temperatura_reader_task.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: python_forestacion\servicios
################################################################################

# ==============================================================================
# ARCHIVO 49/66: __init__.py
# Directorio: python_forestacion\servicios
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_forestacion\servicios\cultivos
################################################################################

# ==============================================================================
# ARCHIVO 50/66: __init__.py
# Directorio: python_forestacion\servicios\cultivos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\cultivos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 51/66: arbol_service.py
# Directorio: python_forestacion\servicios\cultivos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\cultivos\arbol_service.py
# ==============================================================================

from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService:
    """
    Servicio para operaciones específicas de árboles.
    Contiene la lógica de negocio de crecimiento y floración.
    """

    def crecer(self, arbol: Arbol, incremento: float) -> bool:
        """
        Hace crecer un árbol incrementando su altura.
        :param arbol: El árbol a crecer
        :param incremento: El incremento de altura (debe ser >0 y <1)
        :return: True si creció exitosamente, False si no
        """
        if 0 < incremento < 1:
            arbol.altura += incremento
            # Consumir agua al crecer
            self.consumir_agua_por_crecimiento(arbol)
            return True
        return False

    def consumir_agua_por_crecimiento(self, arbol: Arbol):
        """
        Consume agua del árbol por el proceso de crecimiento.
        Este método puede ser sobrescrito por servicios específicos.
        """
        if arbol.agua > 0:
            arbol.agua -= 1


# ==============================================================================
# ARCHIVO 52/66: cultivo_service.py
# Directorio: python_forestacion\servicios\cultivos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\cultivos\cultivo_service.py
# ==============================================================================

from python_forestacion.entidades.cultivos.cultivo import Cultivo

class CultivoService:
    """Servicio base para operaciones comunes de cultivos."""

    def mostrar_datos(self, cultivo: Cultivo):
        print(f"Cultivo: {cultivo.__class__.__name__}")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")


# ==============================================================================
# ARCHIVO 53/66: cultivo_service_registry.py
# Directorio: python_forestacion\servicios\cultivos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\cultivos\cultivo_service_registry.py
# ==============================================================================

from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class CultivoServiceRegistry:
    """
    Registry para despachar automáticamente servicios según el tipo de cultivo.
    """

    def __init__(self, pino_service, olivo_service, lechuga_service, zanahoria_service):
        self.pino_service = pino_service
        self.olivo_service = olivo_service
        self.lechuga_service = lechuga_service
        self.zanahoria_service = zanahoria_service

        # Mapeos para métodos de crecimiento/absorción de agua
        self._handlers_crecer = {
            Pino: lambda c: self.pino_service.absorver_agua(c),
            Olivo: lambda c: self.olivo_service.absorver_agua(c),
            Lechuga: lambda c: self.lechuga_service.absorver_agua(c),
            Zanahoria: lambda c: self.zanahoria_service.absorver_agua(c)
        }

        # Mapeos para mostrar datos
        self._handlers_mostrar = {
            Pino: lambda c: self.pino_service.mostrar_datos(c),
            Olivo: lambda c: self.olivo_service.mostrar_datos(c),
            Lechuga: lambda c: self.lechuga_service.mostrar_datos(c),
            Zanahoria: lambda c: self.zanahoria_service.mostrar_datos(c)
        }

    def crecer(self, cultivo):
        handler = self._handlers_crecer.get(type(cultivo))
        if handler is None:
            raise ValueError(f"No hay servicio registrado para: {type(cultivo).__name__}")
        return handler(cultivo)

    def mostrar_datos(self, cultivo):
        handler = self._handlers_mostrar.get(type(cultivo))
        if handler is None:
            raise ValueError(f"No hay servicio registrado para: {type(cultivo).__name__}")
        return handler(cultivo)


# ==============================================================================
# ARCHIVO 54/66: lechuga_service.py
# Directorio: python_forestacion\servicios\cultivos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\cultivos\lechuga_service.py
# ==============================================================================

from python_forestacion.entidades.cultivos.lechuga import Lechuga

class LechugaService:
    """
    Servicio para operaciones específicas de la Lechuga.
    """

    def desarrollar_semilla(self, lechuga: Lechuga):
        print("Desarrollando semilla de lechuga")

    def absorber_agua(self, lechuga: Lechuga) -> int:
        """Corrige typo y usa el método absorber_agua de la clase"""
        lechuga.absorber_agua(1)
        return 1

    def consumir_agua(self, lechuga: Lechuga) -> int:
        lechuga.set_agua(lechuga.get_agua() - 1)
        return 1

    def mostrar_datos(self, lechuga: Lechuga):
        print(f"Cultivo: {type(lechuga).__name__}")
        print(f"Variedad: {lechuga.get_variedad()}")


# ==============================================================================
# ARCHIVO 55/66: olivo_service.py
# Directorio: python_forestacion\servicios\cultivos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\cultivos\olivo_service.py
# ==============================================================================

from datetime import datetime
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.servicios.cultivos.arbol_service import ArbolService

class OlivoService(ArbolService):
    """
    Servicio para operaciones específicas del Olivo.
    Implementa la lógica de negocio estacional del olivo.
    """

    def cosechar(self, olivo: Olivo) -> bool:
        mes = datetime.now().month
        if 5 <= mes <= 7:
            print("Se ha cosechado este olivo")
            return True
        return False

    def florecer(self, olivo: Olivo) -> bool:
        mes = datetime.now().month
        return 9 <= mes <= 12

    def absorber_agua(self, olivo: Olivo) -> int:
        """Corrige typo y usa el método absorber_agua del cultivo"""
        mes = datetime.now().month
        agua_absorbida = 1 if mes in [1,2,3,4,9,10,11,12] else 0
        olivo.absorber_agua(agua_absorbida)
        return agua_absorbida

    def consumir_agua(self, olivo: Olivo) -> int:
        mes = datetime.now().month
        if mes in [1,2,3,4,9,10,11,12]:
            agua_consumida = 2
            self.crecer(olivo, 0.01)
        elif mes in [5,6,7,8]:
            agua_consumida = 1
        else:
            agua_consumida = 0

        olivo.set_agua(olivo.get_agua() - agua_consumida)
        return agua_consumida

    def mostrar_datos(self, olivo: Olivo):
        print(f"Cultivo {type(olivo).__name__}")
        print(f"Fruto: {olivo.get_fruto().name}")
        print(f"Altura: {olivo.get_altura()}")


# ==============================================================================
# ARCHIVO 56/66: pino_service.py
# Directorio: python_forestacion\servicios\cultivos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\cultivos\pino_service.py
# ==============================================================================

from datetime import datetime
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.servicios.cultivos.arbol_service import ArbolService

class PinoService(ArbolService):
    """
    Servicio para operaciones específicas del Pino.
    Implementa la lógica de negocio estacional del pino.
    """

    def secretar_resina(self, pino: Pino):
        print("Estoy secretando resina")

    def florecer(self, pino: Pino) -> bool:
        mes = datetime.now().month
        return 9 <= mes <= 12

    def absorber_agua(self, pino: Pino) -> int:
        """Corrige typo y usa el método absorber_agua del cultivo"""
        mes = datetime.now().month
        agua_absorbida = 2 if mes in [1,2,3,4,9,10,11,12] else 0
        pino.absorber_agua(agua_absorbida)
        return agua_absorbida

    def consumir_agua(self, pino: Pino) -> int:
        mes = datetime.now().month
        if mes in [1,2,3,4,9,10,11,12]:
            agua_consumida = 2
            self.crecer(pino, 0.10)
        elif mes in [5,6,7,8]:
            agua_consumida = 1
        else:
            agua_consumida = 0

        pino.set_agua(pino.get_agua() - agua_consumida)
        return agua_consumida

    def mostrar_datos(self, pino: Pino):
        print(f"Cultivo {type(pino).__name__}")
        print(f"Variedad: {pino.get_variedad()}")
        print(f"Altura: {pino.get_altura()}")


# ==============================================================================
# ARCHIVO 57/66: zanahoria_service.py
# Directorio: python_forestacion\servicios\cultivos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\cultivos\zanahoria_service.py
# ==============================================================================

from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class ZanahoriaService:
    """
    Servicio para operaciones específicas de la Zanahoria.
    """

    def desarrollar_semilla(self, zanahoria: Zanahoria):
        print("Desarrollando semilla de zanahoria")

    def absorver_agua(self, zanahoria: Zanahoria) -> int:
        zanahoria.set_agua(zanahoria.get_agua() + 2)
        return 2

    def consumir_agua(self, zanahoria: Zanahoria) -> int:
        zanahoria.set_agua(zanahoria.get_agua() - 1)
        return 1

    def mostrar_datos(self, zanahoria: Zanahoria):
        print(f"Cultivo: {type(zanahoria).__name__}")
        if zanahoria.is_baby_carrot():
            print("Es baby carrot")



################################################################################
# DIRECTORIO: python_forestacion\servicios\negocio
################################################################################

# ==============================================================================
# ARCHIVO 58/66: __init__.py
# Directorio: python_forestacion\servicios\negocio
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\negocio\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 59/66: box.py
# Directorio: python_forestacion\servicios\negocio
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\negocio\box.py
# ==============================================================================

from typing import Generic, TypeVar, List
from python_forestacion.entidades.cultivos.cultivo import Cultivo

T = TypeVar("T", bound=Cultivo)

class Box(Generic[T]):
    """
    Contenedor genérico tipo-seguro para cultivos cosechados.
    Funciona como DTO (Data Transfer Object).
    """

    def __init__(self):
        self.id: int | None = None
        self.productos: List[T] = []

    def add_item(self, producto: T):
        """Agrega un cultivo a la caja."""
        self.productos.append(producto)

    def get_items(self) -> List[T]:
        """Devuelve todos los cultivos en la caja."""
        return self.productos

    def mostrar_contenido_caja(self):
        """Muestra por consola el contenido de la caja."""
        print("CONTENIDO DE LA CAJA")
        print("____________________")
        for c in self.get_items():
            print(f"Cultivo: {c.__class__.__name__}")


# ==============================================================================
# ARCHIVO 60/66: fincas_service.py
# Directorio: python_forestacion\servicios\negocio
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\negocio\fincas_service.py
# ==============================================================================

import time
from typing import Type, TypeVar, Generic
from concurrent.futures import ThreadPoolExecutor
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.servicios.negocio.box import Box
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask

T = TypeVar("T", bound=Cultivo)

class FincasService:
    """
    Servicio de orquestación para gestión de múltiples fincas.
    Coordina operaciones entre diferentes dominios (cultivos, riego, plantaciones).
    """

    def __init__(self, plantacion_service: PlantacionService, cultivo_service_registry: CultivoServiceRegistry):
        self.fincas: list[RegistroForestal] = []
        self.plantacion_service = plantacion_service
        self.cultivo_service_registry = cultivo_service_registry

    def add_finca(self, finca: RegistroForestal):
        self.fincas.append(finca)

    def remover_finca(self, finca: RegistroForestal):
        self.fincas.remove(finca)

    def fumigar(self, id_finca: int, insecticida: str):
        for finca in self.fincas:
            if finca.plantacion.id == id_finca:
                for c in finca.plantacion.cultivos:
                    print("Se está fumigando el cultivo:")
                    self.mostrar_datos_cultivo(c)
                    print(f"Con el insecticida: {insecticida}")

    def regar(self, duracion_segundos: int = 20):
        """
        Activa el sistema de riego automatizado para todas las fincas.
        """
        for finca in self.fincas:
            tarea_temp = TemperaturaReaderTask()
            tarea_hum = HumedadReaderTask()
            tarea_control = ControlRiegoTask(tarea_temp, tarea_hum, finca.plantacion, self.plantacion_service)

            threads = [
                ThreadPoolExecutor(max_workers=1).submit(tarea_temp.run),
                ThreadPoolExecutor(max_workers=1).submit(tarea_hum.run),
                ThreadPoolExecutor(max_workers=1).submit(tarea_control.run)
            ]

            time.sleep(duracion_segundos)

            # Detener tareas
            tarea_temp.detener()
            tarea_hum.detener()
            tarea_control.detener()

    def cosechar_y_empaquetar(self, tipo_cultivo: Type[T]) -> Box[T]:
        caja = Box[T]()

        for finca in self.fincas:
            for cult in finca.plantacion.cultivos:
                if isinstance(cult, tipo_cultivo):
                    caja.add_item(cult)
            self.plantacion_service.consumir(finca.plantacion, tipo_cultivo)
            print(f"Se cosecharon los/las {tipo_cultivo.__name__}s de la finca {finca.plantacion.nombre}")

        return caja

    def mostrar_datos_cultivo(self, cultivo: Cultivo):
        """Delegar mostrar datos al servicio específico del cultivo."""
        self.cultivo_service_registry.mostrar_datos(cultivo)



################################################################################
# DIRECTORIO: python_forestacion\servicios\personal
################################################################################

# ==============================================================================
# ARCHIVO 61/66: __init__.py
# Directorio: python_forestacion\servicios\personal
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\personal\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 62/66: trabajador_service.py
# Directorio: python_forestacion\servicios\personal
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\personal\trabajador_service.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: python_forestacion\servicios\terrenos
################################################################################

# ==============================================================================
# ARCHIVO 63/66: __init__.py
# Directorio: python_forestacion\servicios\terrenos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\terrenos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 64/66: plantacion_service.py
# Directorio: python_forestacion\servicios\terrenos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\terrenos\plantacion_service.py
# ==============================================================================

from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.excepciones.agua_agotada_excepcion import AguaAgotadaException
from python_forestacion.excepciones.superficie_insuficiente_excepcion import SuperficieInsuficienteException


class PlantacionService:
    """
    Servicio para operaciones sobre Plantación.
    Contiene toda la lógica de negocio de plantar, regar y cosechar.
    """

    def __init__(self, cultivo_service_registry):
        self.cultivo_service_registry = cultivo_service_registry

    def plantar(self, plantacion, especie: str, cantidad: int) -> bool:
        superficie_ocupada = sum(c.get_superficie() for c in plantacion.get_cultivos_interno())
        sup_disponible = plantacion.situada_en.superficie - superficie_ocupada

        for _ in range(cantidad):
            cultivo = self.crear_cultivo(especie)
            if cultivo is None:
                raise ValueError(f"Especie de cultivo no reconocida: {especie}")

            superficie_requerida = cultivo.get_superficie()
            sup_disponible -= superficie_requerida

            if sup_disponible >= 0:
                plantacion.get_cultivos_interno().append(cultivo)
                print(f"Se plantó un/a: {cultivo.__class__.__name__}")
            else:
                raise SuperficieInsuficienteException(
                    cultivo.__class__.__name__,
                    superficie_requerida,
                    sup_disponible + superficie_requerida
                )

        return True

    def crear_cultivo(self, especie: str):
        if especie == "Pino":
            return Pino("cedro")
        elif especie == "Olivo":
            return Olivo(TipoAceituna.NEGRA)
        elif especie == "Lechuga":
            return Lechuga("Mantecosa")
        elif especie == "Zanahoria":
            return Zanahoria(True)
        else:
            return None

    def regar(self, plantacion) -> bool:
        print(f"Regando finca: {plantacion.nombre}")
        AGUA_MINIMA = 10

        for cultivo in plantacion.get_cultivos_interno():
            agua_actual = plantacion.agua_disponible
            if agua_actual > AGUA_MINIMA:
                agua_absorvida = self.absorver_agua_cultivo(cultivo)
                plantacion.agua_disponible = agua_actual - agua_absorvida
            else:
                raise AguaAgotadaException(agua_actual, AGUA_MINIMA)

        return True

    def absorver_agua_cultivo(self, cultivo) -> int:
        return self.cultivo_service_registry.absorber_agua(cultivo)

    def consumir(self, plantacion, tipo_cultivo):
        # Iterar en reversa para poder eliminar mientras iteramos
        for i in range(len(plantacion.get_cultivos_interno()) - 1, -1, -1):
            cult = plantacion.get_cultivos_interno()[i]
            if isinstance(cult, tipo_cultivo):
                del plantacion.get_cultivos_interno()[i]
        return True


# ==============================================================================
# ARCHIVO 65/66: registro_forestal_service.py
# Directorio: python_forestacion\servicios\terrenos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\terrenos\registro_forestal_service.py
# ==============================================================================

from typing import Optional, List, Dict, Any
import os
import pickle
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.excepciones.persistencia_excepcion import PersistenciaException
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry


class RegistroForestalService:
    """
    Servicio para operaciones sobre RegistroForestal.
    Contiene lógica de persistencia y visualización de datos.
    """

    def __init__(self, cultivo_service_registry: CultivoServiceRegistry):
        self.cultivo_service_registry = cultivo_service_registry

    def mostrar_datos(self, registro: RegistroForestal):
        print("REGISTRO FORESTAL")
        print("=================")
        print(f"Padrón:      {registro.id_padron}")
        print(f"Propietario: {registro.propietario}")
        print(f"Avalúo:      {registro.avaluo}")
        print(f"Domicilio:   {registro.tierra.domicilio}")
        print(f"Superficie:  {registro.tierra.superficie}")
        print(f"Cantidad de cultivos plantados: {len(registro.plantacion.cultivos)}")
        print("Listado de Cultivos plantados")
        print("____________________________")

        for cultivo in registro.plantacion.cultivos:
            self._mostrar_datos_cultivo(cultivo)

    def _mostrar_datos_cultivo(self, cultivo: Cultivo):
        """Delega mostrar datos al servicio específico del cultivo usando el registry."""
        self.cultivo_service_registry.mostrar_datos(cultivo)

    def persistir(self, registro: RegistroForestal):
        """Persiste el registro forestal en disco usando pickle."""
        nombre_archivo = f"data/{registro.propietario}.pkl"

        try:
            os.makedirs("data", exist_ok=True)
            with open(nombre_archivo, "wb") as f:
                pickle.dump(registro, f)

            print(f"Persistencia exitosa para: {registro.propietario}")

        except Exception as e:
            raise PersistenciaException(f"Error al persistir {nombre_archivo}: {e}") from e

    @staticmethod
    def leer_registro(propietario: str) -> RegistroForestal:
        """Lee un registro forestal desde disco usando pickle."""
        if not propietario or propietario.strip() == "":
            raise ValueError("El nombre del propietario no puede ser nulo o vacío")

        nombre_archivo = f"data/{propietario}.pkl"

        try:
            with open(nombre_archivo, "rb") as f:
                registro = pickle.load(f)

            print(f"Lectura exitosa para: {propietario}")
            return registro

        except FileNotFoundError as ex:
            raise PersistenciaException(f"Archivo no encontrado: {nombre_archivo}") from ex
        except Exception as ex:
            raise PersistenciaException(f"Error al leer {nombre_archivo}: {ex}") from ex

# ==============================================================================
# ARCHIVO 66/66: tierra_service.py
# Directorio: python_forestacion\servicios\terrenos
# Ruta completa: C:\Users\Facundo\Desktop\Facundo Tareas\Parcial_Dis_Sistemas\python_forestacion\servicios\terrenos\tierra_service.py
# ==============================================================================

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion


class TierraService:
    """
    Servicio para operaciones sobre Tierra.
    Incluye lógica de creación e inicialización.
    """

    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str
    ) -> Tierra:
        """
        Crea una nueva Tierra e inicializa automáticamente su plantación.
        Factory method que encapsula la creación completa.
        """
        tierra = Tierra(id_padron_catastral, superficie, domicilio)

        # Crear plantación asociada automáticamente
        plantacion = Plantacion(1, nombre_plantacion, 100000, tierra)
        tierra.finca = plantacion

        print(f"Tierra creada: {domicilio} con plantación: {nombre_plantacion}")
        return tierra



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 66
# Generado: 2025-11-05 10:21:19
################################################################################
