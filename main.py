from datetime import datetime, timedelta
import logging

from model.cliente import Cliente
from model.servicios import ReservaSala, AlquilerEquipo, Asesoria
from model.reserva import Reserva
from model.excepciones import (
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaInvalidaError
)
# CONFIGURACIÓN DE LOGS
logging.basicConfig(
    filename='sistema.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class Sistema:

    def __init__(self):

        self.clientes = []
        self.servicios = []
        self.reservas = []

        self._cargar_ejemplo()

    # ==========================
    # CARGAR DATOS DE EJEMPLO
    # ==========================
    def _cargar_ejemplo(self):

        self.servicios = [

            ReservaSala(
                "Sala Premium",
                120,
                tiene_proyector=True
            ),

            ReservaSala(
                "Sala Básica",
                80,
                tiene_proyector=False
            ),

            AlquilerEquipo(
                "Proyector 4K",
                50,
                requiere_seguro=True
            ),

            AlquilerEquipo(
                "Laptop Gaming",
                30,
                requiere_seguro=False
            ),

            Asesoria(
                "Python Avanzado",
                100,
                nivel="Senior"
            ),

            Asesoria(
                "Machine Learning",
                150,
                nivel="Master"
            )
        ]

        try:

            self.clientes.append(
                Cliente(
                    "Karina Diaz",
                    "karina@mail.com",
                    "3137654321"
                )
            )

            self.clientes.append(
                Cliente(
                    "Jose Blanco",
                    "jose@mail.com",
                    "3121234567"
                )
            )

        except ClienteInvalidoError as e:

            logging.error(e)

            print(f"❌ Error cargando ejemplos: {e}")

    # ==========================
    # MENÚ PRINCIPAL
    # ==========================
    def menu(self):

        while True:

            print("\n" + "=" * 60)
            print("🏢 SISTEMA DE RESERVAS SOFTWARE FJ")
            print("=" * 60)

            print("1. Gestionar Clientes")
            print("2. Ver Servicios")
            print("3. Nueva Reserva")
            print("4. Ver Reservas")
            print("5. Gestionar Reserva")
            print("6. Demostrar Sobrecarga")
            print("7. Salir")

            op = input("👉 Opción: ")

            if op == '1':
                self.submenu_clientes()

            elif op == '2':
                self.mostrar_servicios()

            elif op == '3':
                self.nueva_reserva()

            elif op == '4':
                self.mostrar_reservas()

            elif op == '5':
                self.gestionar_reserva()

            elif op == '6':
                self.demostrar_sobrecarga()

            elif op == '7':

                print("\n👋 Gracias por usar el sistema")
                break

            else:
                print("❌ Opción inválida")

    # ==========================
    # SUBMENÚ CLIENTES
    # ==========================
    def submenu_clientes(self):

        while True:

            print("\n" + "-" * 40)
            print("GESTIÓN DE CLIENTES")

            print("1. Listar clientes")
            print("2. Crear cliente")
            print("3. Activar / Desactivar")
            print("4. Volver")

            op = input("👉 Opción: ")

            # =====================
            # LISTAR CLIENTES
            # =====================
            if op == '1':

                if not self.clientes:

                    print("❌ No hay clientes")

                else:

                    for c in self.clientes:
                        print(c.info())

                input("\nPresione Enter...")

            # =====================
            # CREAR CLIENTE
            # =====================
            elif op == '2':

                try:

                    nom = input("Nombre completo: ").strip()
                    email = input("Email: ").strip()
                    tel = input("Teléfono: ").strip()

                    cliente = Cliente(nom, email, tel)

                    self.clientes.append(cliente)

                    print(
                        f"✅ Cliente {cliente.nombre} "
                        f"creado con ID {cliente.id}"
                    )

                except ClienteInvalidoError as e:

                    logging.error(e)

                    print(f"❌ Error: {e}")

                except Exception as e:

                    logging.error(e)

                    print(f"❌ Error inesperado: {e}")

                input("\nPresione Enter para continuar...")

            # =====================
            # ACTIVAR / DESACTIVAR
            # =====================
            elif op == '3':

                if not self.clientes:

                    print("❌ No hay clientes")

                else:

                    for c in self.clientes:
                        print(c.info())

                    try:

                        id_cli = int(input("ID cliente: "))

                        cliente = next(
                            (
                                c for c in self.clientes
                                if c.id == id_cli
                            ),
                            None
                        )

                        if cliente:

                            print(
                                f"Estado actual: "
                                f"{'Activo' if cliente.activo else 'Inactivo'}"
                            )

                            accion = input(
                                "(a) activar / (d) desactivar: "
                            ).lower()

                            if accion == 'a':

                                cliente.activo = True
                                print("✅ Cliente activado")

                            elif accion == 'd':

                                cliente.activo = False
                                print("✅ Cliente desactivado")

                            else:
                                print("❌ Opción inválida")

                        else:
                            print("❌ Cliente no encontrado")

                    except ValueError as e:

                        logging.error(e)

                        print("❌ ID inválido")

                input("\nPresione Enter para continuar...")

            elif op == '4':
                break

            else:
                print("❌ Opción inválida")

    # ==========================
    # MOSTRAR SERVICIOS
    # ==========================
    def mostrar_servicios(self):

        print("\n" + "=" * 60)
        print("🎯 SERVICIOS DISPONIBLES")
        print("=" * 60)

        for s in self.servicios:

            estado = (
                "✅ Disponible"
                if s.disponible
                else "❌ No disponible"
            )

            print(
                f"ID:{s.id} | "
                f"{s.describir()} | "
                f"{estado}"
            )

        input("\nPresione Enter...")

    # ==========================
    # NUEVA RESERVA
    # ==========================
    def nueva_reserva(self):

        if not self.clientes:

            print("❌ No hay clientes registrados")
            return

        print("\n📋 CLIENTES")

        for c in self.clientes:

            print(
                f"{c.id}. "
                f"{c.nombre} "
                f"({'Activo' if c.activo else 'Inactivo'})"
            )

        try:

            id_cli = int(input("ID cliente: "))

            cliente = next(
                (
                    c for c in self.clientes
                    if c.id == id_cli and c.activo
                ),
                None
            )

            if not cliente:

                print("❌ Cliente no encontrado")
                return

        except ValueError as e:

            logging.error(e)

            print("❌ ID inválido")
            return

        print("\n🎯 SERVICIOS")

        for s in self.servicios:

            if s.disponible:
                print(f"{s.id}. {s.describir()}")

        try:

            id_ser = int(input("ID servicio: "))

            servicio = next(
                (
                    s for s in self.servicios
                    if s.id == id_ser and s.disponible
                ),
                None
            )

            if not servicio:

                print("❌ Servicio no disponible")
                return

        except ValueError as e:

            logging.error(e)

            print("❌ ID inválido")
            return

        try:

            horas = float(input("Duración en horas: "))

            if horas <= 0:

                print("❌ Duración inválida")
                return

        except ValueError as e:

            logging.error(e)

            print("❌ Número inválido")
            return

        extras = {}

        fecha = datetime.now() + timedelta(days=1)

        try:

            reserva = Reserva(
                cliente,
                servicio,
                fecha,
                horas,
                extras
            )

            self.reservas.append(reserva)

            print("\n✅ Reserva creada exitosamente")
            print(f"💰 Total: ${reserva.costo}")

        except (
            ReservaInvalidaError,
            ServicioNoDisponibleError
        ) as e:

            logging.error(e)

            print(f"❌ Error: {e}")

        except Exception as e:

            logging.error(e)

            print(f"❌ Error inesperado: {e}")

        input("\nPresione Enter...")

    # ==========================
    # MOSTRAR RESERVAS
    # ==========================
    def mostrar_reservas(self):

        if not self.reservas:

            print("❌ No hay reservas")

        else:

            print("\n" + "=" * 60)
            print("📋 LISTADO DE RESERVAS")
            print("=" * 60)

            for r in self.reservas:
                print(r.info())

        input("\nPresione Enter...")

    # ==========================
    # GESTIONAR RESERVAS
    # ==========================
    def gestionar_reserva(self):

        if not self.reservas:

            print("❌ No hay reservas")
            return

        self.mostrar_reservas()

        try:

            id_r = int(input("ID reserva: "))

            reserva = next(
                (
                    r for r in self.reservas
                    if r.id == id_r
                ),
                None
            )

            if not reserva:

                print("❌ Reserva no encontrada")
                return

            print("\n1. Confirmar")
            print("2. Cancelar")

            op = input("👉 Opción: ")

            if op == '1':

                forma = input("Forma de pago: ")

                if reserva.confirmar(forma):

                    print("✅ Reserva confirmada")

            elif op == '2':

                motivo = input("Motivo cancelación: ")

                if reserva.cancelar(motivo):

                    print("✅ Reserva cancelada")

        except ValueError as e:

            logging.error(e)

            print("❌ ID inválido")

        input("\nPresione Enter...")

    # ==========================
    # SOBRECARGA
    # ==========================
    def demostrar_sobrecarga(self):

        print("\n" + "=" * 60)
        print("💰 DEMOSTRACIÓN DE SOBRECARGA")
        print("=" * 60)

        sala = self.servicios[0]

        print(f"Servicio: {sala.describir()}")

        print(
            f"Sin extras: "
            f"${sala.calcular_costo(3)}"
        )

        print(
            f"Con impuesto: "
            f"${sala.calcular_costo(3, impuesto=True)}"
        )

        print(
            f"Con descuento: "
            f"${sala.calcular_costo(8, descuento=True)}"
        )

        input("\nPresione Enter...")


# ==========================
# EJECUCIÓN PRINCIPAL
# ==========================
if __name__ == "__main__":

    sistema = Sistema()

    sistema.menu()