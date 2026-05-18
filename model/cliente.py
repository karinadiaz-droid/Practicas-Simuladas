from model.excepciones import ClienteInvalidoError


class Cliente:

    contador_id = 1

    def __init__(self, nombre, email, telefono):

        self.id = Cliente.contador_id
        Cliente.contador_id += 1

        self.nombre = nombre
        self.email = email
        self.telefono = telefono

        self.activo = True

    # ==========================
    # GETTER Y SETTER NOMBRE
    # ==========================
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):

        if not valor.strip():

            raise ClienteInvalidoError(
                "El nombre no puede estar vacío"
            )

        self._nombre = valor.strip().title()

    # ==========================
    # GETTER Y SETTER EMAIL
    # ==========================
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):

        if "@" not in valor or "." not in valor:

            raise ClienteInvalidoError(
                "Correo electrónico inválido"
            )

        self._email = valor.strip().lower()

    # ==========================
    # GETTER Y SETTER TELEFONO
    # ==========================
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):

        if not valor.isdigit():

            raise ClienteInvalidoError(
                "El teléfono solo debe contener números"
            )

        if len(valor) < 7:

            raise ClienteInvalidoError(
                "El teléfono es demasiado corto"
            )

        self._telefono = valor

    # ==========================
    # MÉTODO INFO
    # ==========================
    def info(self):

        estado = (
            "Activo"
            if self.activo
            else "Inactivo"
        )

        return (
            f"ID: {self.id} | "
            f"Nombre: {self.nombre} | "
            f"Email: {self.email} | "
            f"Teléfono: {self.telefono} | "
            f"Estado: {estado}"
        )