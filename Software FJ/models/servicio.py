# ==========================================
#    POLIMORFISMO (Clases de Servicio)
# ==========================================

from abc import ABC, abstractmethod
from models.cliente import EntidadSistema
from exceptions.personalizadas import DatosInvalidosException, ServicioNoDisponibleException

class Servicio(EntidadSistema, ABC):
    def __init__(self, id_entidad: int, nombre_servicio: str, precio_base: float):
        super().__init__(id_entidad)
        self.nombre_servicio = nombre_servicio
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, horas: int) -> float:
        pass

    @abstractmethod
    def describir_servicio(self) -> str:
        pass

    @abstractmethod
    def validar_parametros(self, horas: int):
        pass


class ReservaSala(Servicio):
    def calcular_costo(self, horas: int, impuesto: float = 0.0, descuento: float = 0.0) -> float:
        # Simulación de sobrecarga de métodos mediante parámetros opcionales
        costo = self.precio_base * horas
        costo += costo * impuesto
        costo -= costo * descuento
        return max(0.0, costo)

    def describir_servicio(self) -> str:
        return f"Sala de Reuniones Premium (Precio base: ${self.precio_base}/hr)"

    def validar_parametros(self, horas: int):
        if horas <= 0 or horas > 12:
            raise DatosInvalidosException("El alquiler de salas debe ser entre 1 y 12 horas.")


class AlquilerEquipo(Servicio):
    def __init__(self, id_entidad: int, nombre_servicio: str, precio_base: float, stock: int):
        super().__init__(id_entidad, nombre_servicio, precio_base)
        self.stock = stock

    def calcular_costo(self, horas: int) -> float:
        return self.precio_base * horas

    def describir_servicio(self) -> str:
        return f"Alquiler de equipo informático (Stock actual: {self.stock})"

    def validar_parametros(self, horas: int):
        if horas <= 0:
            raise DatosInvalidosException("La duración del alquiler debe ser mayor a cero horas.")
        if self.stock <= 0:
            raise ServicioNoDisponibleException("No quedan unidades de este equipo en el inventario.")


class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, horas: int) -> float:
        return self.precio_base * horas

    def describir_servicio(self) -> str:
        return f"Asesoría Profesional Técnica (Costo: ${self.precio_base}/hr)"

    def validar_parametros(self, horas: int):
        if horas < 2:
            raise DatosInvalidosException("Las asesorías requieren de un agendamiento mínimo de 2 horas.")
