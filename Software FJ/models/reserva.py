# ==========================================
#    GESTIÓN DE RESERVAS
# ==========================================

from models.cliente import Cliente
from models.servicio import Servicio
from exceptions.personalizadas import OperacionNoPermitidaException

class Reserva:
    def __init__(self, id_reserva: int, cliente: Cliente, servicio: Servicio, duracion_horas: int):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        
        # Validación polimórfica antes de la asignación
        self.servicio.validar_parametros(duracion_horas)
        self.duracion_horas = duracion_horas
        self.__estado = "Confirmada"

    @property
    def estado(self):
        return self.__estado

    def procesar_reserva(self):
        if self.__estado == "Procesada":
            raise OperacionNoPermitidaException("Error: Esta reserva ya se encuentra procesada.")
        if self.__estado == "Cancelada":
            raise OperacionNoPermitidaException("Error: No se puede procesar una reserva cancelada.")
        self.__estado = "Procesada"

    def cancelar_reserva(self):
        if self.__estado == "Procesada":
            raise OperacionNoPermitidaException("Error: No se puede cancelar una reserva que ya fue completada.")
        self.__estado = "Cancelada"
