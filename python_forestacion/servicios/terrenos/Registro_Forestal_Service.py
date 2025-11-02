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