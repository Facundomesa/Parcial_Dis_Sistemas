from entidades.terrenos.tierra import Tierra

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
