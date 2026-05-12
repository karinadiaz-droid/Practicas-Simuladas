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
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        patron = r'^[\w\.-]+@[\w\.-]+\w+$'
        if not re.match(patron, valor):
            raise ClienteInvalidoError(f"email inválido: '{valor}'")
        self.email = valor.lower()

 @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not valor or len(re.sub(r'\D', '', valor)) < 7:
            raise ClienteInvalidoError(f"Teléfono inválido: '{valor}'. son como mínimo 10 dígitos")
        self._telefono = valor

    def info(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"ID:{self.id} | {self.nombre} | {self.email} | {estado}"

