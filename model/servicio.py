from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass
class ReservaSala(Servicio):
    def __init__(self, nombre, precio_hora):
        super().__init__(nombre)
        self.precio_hora = precio_hora

    def calcular_costo(self, horas):
        return self.precio_hora * horas

    def descripcion(self):
        return f"Servicio de reserva de sala: {self.nombre}"
