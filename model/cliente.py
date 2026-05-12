import re
from datetime import datetime
from .excepciones import ClienteInvalidoError

class Cliente:
    _id_counter = 1

    def __init__(self, nombre, email, telefono):
        self.id = Cliente._id_counter
        Cliente._id_counter += 1
        self._nombre = None
        self._email = None
        self._telefono = None
        self.activo = True
        self.fecha_registro = datetime.now()
        #hacemos validaciones a traves de setters
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
         if not valor or len(valor.strip()) < 3:
            raise ClienteInvalidoError(f"Nombre inválido: '{valor}'. mínimo 3 letras")
        self._nombre = valor.strip().title()

    @property

        

        if edad <= 0:
            raise ValueError("Edad inválida")

        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad
