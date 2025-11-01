from typing import Generic, TypeVar, List
from entidades.cultivos.cultivo import Cultivo

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
