class ErrorReserva(Exception):
    pass


class Reserva:
    def __init__(self, cliente, servicio):
        if cliente is None or servicio is None:
            raise ErrorReserva("Cliente o servicio inválido")

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"
