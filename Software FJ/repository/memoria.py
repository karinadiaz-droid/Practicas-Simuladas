# Simulación de persistencia en memoria para cumplir la condición de "no usar bases de datos"
class BaseDatosSimulada:
    def __init__(self):
        self.clientes = {}
        self.servicios = {}
        self.reservas = {}

    def guardar_cliente(self, cliente):
        self.clientes[cliente.id_entidad] = cliente

    def guardar_servicio(self, servicio):
        self.servicios[servicio.id_entidad] = servicio

    def guardar_reserva(self, reserva):
        self.reservas[reserva.id_reserva] = reserva
