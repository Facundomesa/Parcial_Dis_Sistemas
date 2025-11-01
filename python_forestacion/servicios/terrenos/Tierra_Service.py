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
