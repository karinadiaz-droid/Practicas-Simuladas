# Practicas-Simuladas
Sistema en Python orientado a objetos para gestionar clientes, servicios y reservas, con manejo de excepciones y registro de errores.
class Cliente:
    def __init__(self, nombre, edad):
        if not nombre:
            raise ValueError("Nombre inválido")
        if edad <= 0:
            raise ValueError("Edad inválida")

        self.nombre = nombre
        self.edad = edad
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
