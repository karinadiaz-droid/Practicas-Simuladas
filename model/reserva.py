from datetime import datetime
import logging
from .excepciones import ReservaInvalidaError, ServicioNoDisponibleError

# Configuración de logging
logging.basicConfig( # logging es un módulo estándar de Python para registrar eventos, errores y mensajes de información.
    filename='sistema.log', #todos los mensajes de log se escribirán en este archivo (se crea en el mismo directorio donde se ejecuta el programa
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Reserva:
    _id_counter = 1

    def __init__(self, cliente, servicio, fecha_inicio, horas, extras=None):
        # Validaciones iniciales con excepciones personalizadas
        if not cliente or not cliente.activo: #verifica que se haya pasado un objeto cliente
            raise ReservaInvalidaError("Cliente no válido o inactivo")
        if not servicio or not servicio.disponible:
            raise ServicioNoDisponibleError(f"Servicio '{servicio.nombre}' no disponible")
        if horas <= 0:
            raise ReservaInvalidaError("La duración debe ser positiva")
        if fecha_inicio < datetime.now():
            raise ReservaInvalidaError("No se puede reservar en el pasado")

        self.id = Reserva._id_counter
        Reserva._id_counter += 1
        self.cliente = cliente
        self.servicio = servicio
        self.fecha_inicio = fecha_inicio
        self.horas = horas
        self.extras = extras or {}
        self.estado = "PENDIENTE"
        # Cálculo del costo usando polimorfismo
        self.costo = self.servicio.calcular_costo(horas, **self.extras)
        logging.info(f"Reserva {self.id} creada - Cliente: {cliente.nombre} - Servicio: {servicio.nombre} - Costo: ${self.costo}")

    def confirmar(self, forma_pago="efectivo", referencia=None):
        """Sobrecarga: se puede llamar solo con forma_pago o con referencia adicional"""
        if self.estado != "PENDIENTE": #solo se puede confirmar una reserva si está en estado "PENDIENTE". Si ya está confirmada, cancelada o cualquier otro, se rechaza
            logging.warning(f"Intento de confirmar reserva {self.id} en estado {self.estado}")
            return False
        self.estado = "CONFIRMADA"
        mensaje = f"Reserva {self.id} confirmada - Pago: {forma_pago}"
        if referencia:
            mensaje += f" - Ref: {referencia}"
        logging.info(mensaje)
        return True

    def cancelar(self, motivo=""):
        if self.estado not in ["PENDIENTE", "CONFIRMADA"]:
            logging.warning(f"Intento de cancelar reserva {self.id} en estado {self.estado}")
            return False
        self.estado = "CANCELADA"
        logging.warning(f"Reserva {self.id} cancelada. Motivo: {motivo or 'No especificado'}")
        return True

    def info(self):
        return (f"#{self.id} | {self.cliente.nombre} | {self.servicio.nombre} | "
                f"{self.horas}h | {self.estado} | ${self.costo}")
