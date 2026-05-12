import re #este es un módulo de expresiones regulares para la validacion de un email
from datetime import datetime # esto es para obtener la fecha y hora cuando se crea el cliente
from .excepciones import ClienteInvalidoError # importa la excepción personalizada desde el mismo paquete (models/excepciones.py)

class Cliente:
    _id_counter = 1

    #utilizaremoe el metodo constructor init par asignar valores iniciales a los atributos o datos en este caso
    def __init__(self, nombre, email, telefono):
        self.id = Cliente._id_counter
        Cliente._id_counter += 1
        self._nombre = None
        self._email = None
        self._telefono = None
        self.activo = True
        self.fecha_registro = datetime.now()
        #hacemos validaciones a traves de setters, un método que permite modificar de manera controlada el valor de un atributo
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    @property #Las propiedades permiten (@property) controlar el acceso a los atributos privados
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
         if not valor or len(valor.strip()) < 3: #con esto se comprueba que no se ingrese un valor vacío o incorrecto
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
        if not valor or len(re.sub(r'\D', '', valor)) < 10:
            raise ClienteInvalidoError(f"Teléfono inválido: '{valor}'. son como mínimo 10 dígitos")
        self._telefono = valor

    def info(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"ID:{self.id} | {self.nombre} | {self.email} | {estado}"

