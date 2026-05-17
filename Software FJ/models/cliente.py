# ==========================================
#    CLASES BASE Y ENCAPSULAMIENTO
# ==========================================

from exceptions.personalizadas import DatosInvalidosException

class EntidadSistema:
    """Clase base para todos los objetos que tengan un ID en el sistema."""
    def __init__(self, id_entidad: int):
        self.id_entidad = id_entidad

class Cliente(EntidadSistema):
    def __init__(self, id_entidad: int, nombre: str, correo: str):
        super().__init__(id_entidad)
        self.nombre = nombre  # Activa el setter de validación
        self.correo = correo  # Activa el setter de validación

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or len(valor.strip()) == 0:
            raise DatosInvalidosException("El nombre del cliente no puede estar vacío.")
        self.__nombre = valor

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor: str):
        if "@" not in valor:
            raise DatosInvalidosException(f"El correo '{valor}' no es un formato válido.")
        self.__correo = valor
