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
