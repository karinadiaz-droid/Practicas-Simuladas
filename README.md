# Sistema Integral Orientado a Objetos – Software FJ
# ============================================================
# SISTEMA INTEGRAL ORIENTADO A OBJETOS - SOFTWARE FJ
# ============================================================
# Autor: David Alexander Camargo Álvarez
# Descripción:
# Sistema orientado a objetos sin base de datos para gestionar
# clientes, servicios y reservas.
# ============================================================

# ==============================
# IMPORTACIÓN DE LIBRERÍAS
# ==============================

from abc import ABC, abstractmethod
from datetime import datetime
import logging


# ============================================================
# CONFIGURACIÓN DEL SISTEMA DE LOGS
# ============================================================
# Esta configuración permite guardar todos los eventos y errores
# en un archivo llamado software_fj.log
# ============================================================

logging.basicConfig(filename="software_fj.log",level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")


# ============================================================
# EXCEPCIONES PERSONALIZADAS
# ============================================================
# Estas excepciones permiten controlar errores específicos
# del sistema.
# ============================================================

class ClienteError(Exception):
    """Excepción personalizada para errores relacionados con clientes."""
    pass

class ServicioError(Exception):
    """Excepción personalizada para errores relacionados con servicios."""
    pass

class ReservaError(Exception):
    """Excepción personalizada para errores relacionados con reservas."""
    pass

# ============================================================
# CLASE ABSTRACTA PERSONA
# ============================================================
# Esta clase representa una entidad general del sistema.
# ============================================================

class Persona(ABC):

    # --------------------------------------------------------
    # Constructor de la clase Persona
    # --------------------------------------------------------
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    # --------------------------------------------------------
    # Método abstracto que debe implementarse en las clases
    # derivadas.
    # --------------------------------------------------------
    @abstractmethod
    def mostrar_datos(self):
        pass

# ============================================================
# CLASE CLIENTE
# ============================================================
# Esta clase hereda de Persona y aplica encapsulación.
# ============================================================

class Cliente(Persona):

    # --------------------------------------------------------
    # Constructor de Cliente
    # --------------------------------------------------------
    def __init__(self, nombre, identificacion, correo):
        super().__init__(nombre, identificacion)

        # Encapsulación de atributos privados
        self.__correo = None

        # Validación del correo
        self.correo = correo

    # --------------------------------------------------------
    # Getter del correo
    # --------------------------------------------------------
    @property
    def correo(self):
        return self.__correo

    # --------------------------------------------------------
    # Setter del correo con validaciones
    # --------------------------------------------------------
    @correo.setter
    def correo(self, valor):

        if "@" not in valor:
            raise ClienteError("El correo electrónico no es válido")

        self.__correo = valor

    # --------------------------------------------------------
    # Método que muestra información del cliente
    # --------------------------------------------------------
    def mostrar_datos(self):
        return f"Cliente: {self.nombre} - ID: {self.identificacion} - Correo: {self.correo}"


# ============================================================
# CLASE ABSTRACTA SERVICIO
# ============================================================
# Clase base para todos los servicios del sistema.
# ============================================================

class Servicio(ABC):

    # --------------------------------------------------------
    # Constructor de Servicio
    # --------------------------------------------------------
    def __init__(self, nombre, tarifa_base):

        if tarifa_base <= 0:
            raise ServicioError("La tarifa debe ser mayor que cero")

        self.nombre = nombre
        self.tarifa_base = tarifa_base

    # --------------------------------------------------------
    # Método abstracto para calcular costos
    # --------------------------------------------------------
    @abstractmethod
    def calcular_costo(self, horas, descuento=0):
        pass

    # --------------------------------------------------------
    # Método abstracto para describir servicios
    # --------------------------------------------------------
    @abstractmethod
    def descripcion(self):
        pass

# ============================================================
# CLASE RESERVA DE SALAS
# ============================================================
# Servicio especializado para reservas de salas.
# ============================================================

class ReservaSala(Servicio):

    # --------------------------------------------------------
    # Constructor de ReservaSala
    # --------------------------------------------------------
    def __init__(self, capacidad, tarifa_base=50000):

        super().__init__("Reserva de Sala", tarifa_base)
        self.capacidad = capacidad

    # --------------------------------------------------------
    # Método sobrescrito para calcular costos
    # --------------------------------------------------------
    def calcular_costo(self, horas, descuento=0):

        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores a cero")

        costo = self.tarifa_base * horas
        costo -= costo * descuento

        return costo

    # --------------------------------------------------------
    # Método sobrescrito de descripción
    # --------------------------------------------------------
    def descripcion(self):
        return f"Servicio de reserva de sala para {self.capacidad} personas"


# ============================================================
# CLASE ALQUILER DE EQUIPOS
# ============================================================
# Servicio especializado para alquiler de equipos.
# ============================================================

class AlquilerEquipos(Servicio):

    # --------------------------------------------------------
    # Constructor de AlquilerEquipos
    # --------------------------------------------------------
    def __init__(self, tipo_equipo, tarifa_base=70000):

        super().__init__("Alquiler de Equipos", tarifa_base)
        self.tipo_equipo = tipo_equipo

    # --------------------------------------------------------
    # Método sobrescrito para calcular costos
    # --------------------------------------------------------
    def calcular_costo(self, horas, descuento=0):

        if horas <= 0:
            raise ServicioError("Cantidad de horas inválida")

        costo = self.tarifa_base * horas
        iva = costo * 0.19

        costo_total = costo + iva
        costo_total -= costo_total * descuento

        return costo_total

    # --------------------------------------------------------
    # Método sobrescrito de descripción
    # --------------------------------------------------------
    def descripcion(self):
        return f"Alquiler de equipos tipo: {self.tipo_equipo}"


# ============================================================
# CLASE ASESORÍA ESPECIALIZADA
# ============================================================
# Servicio especializado para asesorías.
# ============================================================

class AsesoriaEspecializada(Servicio):

    # --------------------------------------------------------
    # Constructor de AsesoriaEspecializada
    # --------------------------------------------------------
    def __init__(self, area, tarifa_base=100000):

        super().__init__("Asesoría Especializada", tarifa_base)
        self.area = area

    # --------------------------------------------------------
    # Método sobrescrito para calcular costos
    # --------------------------------------------------------
    def calcular_costo(self, horas, descuento=0):

        if horas <= 0:
            raise ServicioError("Las horas deben ser válidas")

        costo = self.tarifa_base * horas

        # Recargo adicional para asesorías largas
        if horas > 5:
            costo += 50000

        costo -= costo * descuento

        return costo

    # --------------------------------------------------------
    # Método sobrescrito de descripción
    # --------------------------------------------------------
    def descripcion(self):
        return f"Asesoría especializada en: {self.area}"


# ============================================================
# CLASE RESERVA
# ============================================================
# Clase encargada de integrar cliente, servicio y duración.
# ============================================================

class Reserva:

    # --------------------------------------------------------
    # Constructor de Reserva
    # --------------------------------------------------------
    def __init__(self, cliente, servicio, horas):

        if not isinstance(cliente, Cliente):
            raise ReservaError("El objeto cliente no es válido")

        if not isinstance(servicio, Servicio):
            raise ReservaError("El servicio no es válido")

        if horas <= 0:
            raise ReservaError("Las horas deben ser mayores a cero")

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    # --------------------------------------------------------
    # Método para confirmar una reserva
    # --------------------------------------------------------
    def confirmar(self):

        try:
            self.estado = "Confirmada"

            logging.info(
                f"Reserva confirmada para {self.cliente.nombre}"
            )

        except Exception as e:
            logging.error(f"Error al confirmar reserva: {e}")
            raise ReservaError("No fue posible confirmar la reserva") from e

    # --------------------------------------------------------
    # Método para cancelar una reserva
    # --------------------------------------------------------
    def cancelar(self):

        try:
            self.estado = "Cancelada"

            logging.warning(
                f"Reserva cancelada para {self.cliente.nombre}"
            )

        except Exception as e:
            logging.error(f"Error al cancelar reserva: {e}")
            raise ReservaError("No fue posible cancelar la reserva") from e

    # --------------------------------------------------------
    # Método para procesar la reserva
    # --------------------------------------------------------
    def procesar(self, descuento=0):

        try:

            costo = self.servicio.calcular_costo(self.horas, descuento)

        except ServicioError as e:

            logging.error(f"Error en el servicio: {e}")
            raise ReservaError("No se pudo procesar la reserva") from e

        else:

            logging.info(f"Reserva procesada correctamente para {self.cliente.nombre}")

            return costo

        finally:

            logging.info("Finalizó el proceso de reserva")


# ============================================================
# CLASE GESTOR DEL SISTEMA
# ============================================================
# Clase encargada de administrar listas internas.
# ============================================================

class SistemaSoftwareFJ:

    # --------------------------------------------------------
    # Constructor del sistema
    # --------------------------------------------------------
    def __init__(self):

        self.clientes = []
        self.servicios = []
        self.reservas = []

    # --------------------------------------------------------
    # Método para agregar clientes
    # --------------------------------------------------------
    def agregar_cliente(self, cliente):

        try:

            if not isinstance(cliente, Cliente):
                raise ClienteError("Objeto cliente inválido")

            self.clientes.append(cliente)

            logging.info(f"Cliente agregado: {cliente.nombre}")

        except ClienteError as e:

            logging.error(f"Error al agregar cliente: {e}")
            print(f"ERROR CLIENTE: {e}")

    # --------------------------------------------------------
    # Método para agregar servicios
    # --------------------------------------------------------
    def agregar_servicio(self, servicio):

        try:

            if not isinstance(servicio, Servicio):
                raise ServicioError("Servicio inválido")

            self.servicios.append(servicio)

            logging.info(f"Servicio agregado: {servicio.nombre}")

        except ServicioError as e:

            logging.error(f"Error al agregar servicio: {e}")
            print(f"ERROR SERVICIO: {e}")

    # --------------------------------------------------------
    # Método para registrar reservas
    # --------------------------------------------------------
    def registrar_reserva(self, reserva):

        try:

            if not isinstance(reserva, Reserva):
                raise ReservaError("Reserva inválida")

            self.reservas.append(reserva)

            logging.info("Reserva registrada correctamente")

        except ReservaError as e:

            logging.error(f"Error registrando reserva: {e}")
            print(f"ERROR RESERVA: {e}")


# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================
# Esta función simula operaciones válidas e inválidas.
# ============================================================


def main():

    # --------------------------------------------------------
    # Creación del sistema
    # --------------------------------------------------------
    sistema = SistemaSoftwareFJ()

    print("\n=========== SOFTWARE FJ ===========\n")

    # ========================================================
    # OPERACIÓN 1 - CLIENTE VÁLIDO
    # ========================================================

    try:

        cliente1 = Cliente("David camargo", "1010", "david@gmail.com")

        sistema.agregar_cliente(cliente1)

        print(cliente1.mostrar_datos())

    except Exception as e:

        logging.error(e)
        print(e)

    # ========================================================
    # OPERACIÓN 2 - CLIENTE INVÁLIDO
    # ========================================================

    try:

        cliente2 = Cliente("Karina dias","2020", "correo_invalido")

        sistema.agregar_cliente(cliente2)

    except ClienteError as e:

        logging.error(e)
        print(f"ERROR DETECTADO: {e}")

    # ========================================================
    # OPERACIÓN 3 - SERVICIO VÁLIDO
    # ========================================================

    try:

        sala = ReservaSala(capacidad=20)

        sistema.agregar_servicio(sala)

        print(sala.descripcion())

    except Exception as e:

        logging.error(e)
        print(e)

    # ========================================================
    # OPERACIÓN 4 - SERVICIO INVÁLIDO
    # ========================================================

    try:

        servicio_invalido = ReservaSala(capacidad=10, tarifa_base=-500)

        sistema.agregar_servicio(servicio_invalido)

    except ServicioError as e:

        logging.error(e)
        print(f"ERROR DETECTADO: {e}")

    # ========================================================
    # OPERACIÓN 5 - ALQUILER DE EQUIPOS
    # ========================================================

    try:

        equipos = AlquilerEquipos("Computadores")

        sistema.agregar_servicio(equipos)

        print(equipos.descripcion())

    except Exception as e:

        logging.error(e)
        print(e)

    # ========================================================
    # OPERACIÓN 6 - ASESORÍA
    # ========================================================

    try:

        asesoria = AsesoriaEspecializada("Ciberseguridad")

        sistema.agregar_servicio(asesoria)

        print(asesoria.descripcion())

    except Exception as e:

        logging.error(e)
        print(e)

    # ========================================================
    # OPERACIÓN 7 - RESERVA EXITOSA
    # ========================================================

    try:

        reserva1 = Reserva(cliente1, sala, 3)

        sistema.registrar_reserva(reserva1)

        reserva1.confirmar()

        costo = reserva1.procesar(descuento=0.10)

        print(f"Costo total reserva: ${costo}")

    except Exception as e:

        logging.error(e)
        print(e)

    # ========================================================
    # OPERACIÓN 8 - RESERVA INVÁLIDA
    # ========================================================

    try:

        reserva2 = Reserva(cliente1, sala, -2)

        sistema.registrar_reserva(reserva2)

    except ReservaError as e:

        logging.error(e)
        print(f"ERROR DETECTADO: {e}")

    # ========================================================
    # OPERACIÓN 9 - PROCESO CON ERROR
    # ========================================================

    try:

        reserva3 = Reserva(cliente1, equipos, 0)

        sistema.registrar_reserva(reserva3)

    except ReservaError as e:

        logging.error(e)
        print(f"ERROR DETECTADO: {e}")

    # ========================================================
    # OPERACIÓN 10 - CANCELACIÓN DE RESERVA
    # ========================================================

    try:

        reserva4 = Reserva(cliente1, asesoria, 6)

        sistema.registrar_reserva(reserva4)

        reserva4.cancelar()

        print("Reserva cancelada correctamente")

    except Exception as e:

        logging.error(e)
        print(e)

    print("\n=========== FIN DEL SISTEMA ===========")


# ============================================================
# EJECUCIÓN PRINCIPAL DEL PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()
