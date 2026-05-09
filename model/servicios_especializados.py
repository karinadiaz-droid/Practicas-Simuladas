from modelo.servicios import Servicio

class ReservaSala(Servicio):

    def calcular_costo(self):
        return 50000


class AlquilerEquipo(Servicio):

    def calcular_costo(self):
        return 80000


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self):
        return 120000
