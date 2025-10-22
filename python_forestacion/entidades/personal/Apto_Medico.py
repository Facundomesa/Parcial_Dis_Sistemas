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
