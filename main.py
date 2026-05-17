# =========================================================
# SISTEMA INTEGRAL DE GESTIÓN DE RESERVAS - SOFTWARE FJ
# Archivo principal: main.py
# =========================================================

# =========================
# IMPORTACIONES
# =========================
from modelo.cliente import Cliente
from modelo.servicios import ReservaSala, AlquilerEquipo, Asesoria
from modelo.reserva import Reserva
from modelo.excepciones import (
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaInvalidaError
)
import logging
logging.basicConfig(
    filename='sistema.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# =========================
# CONFIGURACIÓN DE LOGS
# =========================

logging.basicConfig(
    filename='sistema.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# =========================================================
# CLASE PRINCIPAL DEL SISTEMA
# =========================================================

class Sistema:

    # =====================================================
    # CONSTRUCTOR
    # =====================================================

    def __init__(self):

        self.clientes = []
        self.servicios = []
        self.reservas = []

        self._cargar_ejemplo()

    # =====================================================
    # CARGAR DATOS DE EJEMPLO
    # =====================================================

    def _cargar_ejemplo(self):

        # -------------------------
        # Servicios de ejemplo
        # -------------------------

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

        # -------------------------
        # Clientes de ejemplo
        # -------------------------

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

    print(f"❌ Error: {e}")

    # =====================================================
    # MENÚ PRINCIPAL
    # =====================================================

    def menu(self):

        while True:

            print("\n" + "=" * 60)
            print("🏢 SISTEMA DE GESTIÓN DE RESERVAS")
            print("=" * 60)

            print("1. Gestionar Clientes")
            print("2. Ver Servicios")
            print("3. Nueva Reserva")
            print("4. Ver Reservas")
            print("5. Gestionar Reserva")
            print("6. Demostrar Sobrecarga")
            print("7. Salir")

            opcion = input("👉 Seleccione una opción: ")

            if opcion == '1':

                self.submenu_clientes()

            elif opcion == '2':

                self.mostrar_servicios()

            elif opcion == '3':

                self.nueva_reserva()

            elif opcion == '4':

                self.mostrar_reservas()

            elif opcion == '5':

                self.gestionar_reserva()

            elif opcion == '6':

                self.demostrar_sobrecarga()

            elif opcion == '7':

                print("\n👋 Gracias por usar el sistema")
                print("📄 Revise 'sistema.log' para más detalles")

                break

            else:

                print("❌ Opción inválida")

    # =====================================================
    # SUBMENÚ CLIENTES
    # =====================================================

    def submenu_clientes(self):

        while True:

            print("\n" + "-" * 40)
            print("👤 GESTIÓN DE CLIENTES")
            print("-" * 40)

            print("1. Listar clientes")
            print("2. Crear cliente")
            print("3. Activar / Desactivar cliente")
            print("4. Volver")

            opcion = input("Seleccione una opción: ")

            # =============================================
            # LISTAR CLIENTES
            # =============================================

            if opcion == '1':

                if not self.clientes:

                    print("❌ No hay clientes registrados")

                else:

                    for cliente in self.clientes:

                        print(cliente.info())

                input("\nPresione Enter para continuar...")

            # =============================================
            # CREAR CLIENTE
            # =============================================

            elif opcion == '2':

                try:

                    nombre = input("Nombre: ").strip()

                    email = input("Email: ").strip()

                    telefono = input("Teléfono: ").strip()

                    cliente = Cliente(
                        nombre,
                        email,
                        telefono
                    )

                    self.clientes.append(cliente)

                except ClienteInvalidoError as e:

                    logging.error(e)

                    print(f"❌ Error: {e}")

                else:

                    print("\n✅ Cliente creado exitosamente")
                    print(f"ID asignado: {cliente.id}")

                finally:

                    print("✔️ Proceso finalizado")

                input("\nPresione Enter para continuar...")

            # =============================================
            # ACTIVAR / DESACTIVAR CLIENTE
            # =============================================

            elif opcion == '3':

                if not self.clientes:

                    print("❌ No hay clientes")

                else:

                    for cliente in self.clientes:

                        print(cliente.info())

                    try:

                        id_cliente = int(
                            input("ID del cliente: ")
                        )

                        cliente = next(

                            (
                                c for c in self.clientes
                                if c.id == id_cliente
                            ),

                            None
                        )

                        if cliente:

                            print(
                                f"Estado actual: "
                                f"{'Activo' if cliente.activo else 'Inactivo'}"
                            )

                            accion = input(
                                "(a) Activar / (d) Desactivar: "
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

            # =============================================
            # VOLVER
            # =============================================

            elif opcion == '4':

                break

            else:

                print("❌ Opción inválida")

    # =====================================================
    # MOSTRAR SERVICIOS
    # =====================================================

    def mostrar_servicios(self):

        print("\n" + "=" * 60)
        print("🎯 SERVICIOS DISPONIBLES")
        print("=" * 60)

        for servicio in self.servicios:

            estado = (
                "✅ Disponible"
                if servicio.disponible
                else "❌ No disponible"
            )

            print(
                f"ID: {servicio.id} | "
                f"{servicio.describir()} | "
                f"{estado}"
            )

        input("\nPresione Enter para continuar...")

    # =====================================================
    # NUEVA RESERVA
    # =====================================================

    def nueva_reserva(self):

        if not self.clientes:

            print("❌ Debe existir al menos un cliente")

            return

        # =============================================
        # SELECCIÓN DE CLIENTE
        # =============================================

        print("\n📋 CLIENTES")

        for cliente in self.clientes:

            print(
                f"{cliente.id}. "
                f"{cliente.nombre}"
            )

        try:

            id_cliente = int(
                input("Seleccione ID cliente: ")
            )

            cliente = next(

                (
                    c for c in self.clientes
                    if c.id == id_cliente and c.activo
                ),

                None
            )

            if not cliente:

                print("❌ Cliente inválido o inactivo")

                return

        except ValueError as e:

            logging.error(e)

            print("❌ ID inválido")

            return

        # =============================================
        # SELECCIÓN DE SERVICIO
        # =============================================

        print("\n🎯 SERVICIOS")

        for servicio in self.servicios:

            if servicio.disponible:

                print(
                    f"{servicio.id}. "
                    f"{servicio.describir()}"
                )

        try:

            id_servicio = int(
                input("Seleccione ID servicio: ")
            )

            servicio = next(

                (
                    s for s in self.servicios
                    if s.id == id_servicio and s.disponible
                ),

                None
            )

            if not servicio:

                raise ServicioNoDisponibleError(
                    "Servicio no disponible"
                )

        except ValueError as e:

            logging.error(e)

            print("❌ ID inválido")

            return

        except ServicioNoDisponibleError as e:

            logging.error(e)

            print(f"❌ {e}")

            return

        # =============================================
        # DURACIÓN
        # =============================================

        try:

            horas = float(
                input("Duración en horas: ")
            )

            if horas <= 0:

                raise ReservaInvalidaError(
                    "La duración debe ser positiva"
                )

        except ValueError as e:

            logging.error(e)

            print("❌ Número inválido")

            return

        except ReservaInvalidaError as e:

            logging.error(e)

            print(f"❌ {e}")

            return

        # =============================================
        # PARÁMETROS EXTRA
        # =============================================

        extras = {}

        if isinstance(servicio, ReservaSala):

            if input(
                "¿Agregar proyector? (s/n): "
            ).lower() == 's':

                extras['proyector'] = True

            if input(
                "¿Aplicar impuesto? (s/n): "
            ).lower() == 's':

                extras['impuesto'] = True

        elif isinstance(servicio, AlquilerEquipo):

            if input(
                "¿Agregar seguro? (s/n): "
            ).lower() == 's':

                extras['seguro'] = True

        elif isinstance(servicio, Asesoria):

            if input(
                "¿Modalidad premium? (s/n): "
            ).lower() == 's':

                extras['premium'] = True

        # =============================================
        # CREAR RESERVA
        # =============================================

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

        except (
            ReservaInvalidaError,
            ServicioNoDisponibleError
        ) as e:

            logging.error(e)

            print(f"❌ Error: {e}")

        except Exception as e:

            logging.error(e)

            print(f"❌ Error inesperado: {e}")

        else:

            print("\n" + "=" * 50)
            print("✅ RESERVA CREADA EXITOSAMENTE")
            print("=" * 50)

            print(f"Cliente: {cliente.nombre}")
            print(f"Servicio: {servicio.nombre}")
            print(f"Costo total: ${reserva.costo}")

            print("=" * 50)

        finally:

            print("✔️ Proceso de reserva finalizado")

        input("\nPresione Enter para continuar...")

    # =====================================================
    # MOSTRAR RESERVAS
    # =====================================================

    def mostrar_reservas(self):

        if not self.reservas:

            print("❌ No hay reservas")

        else:

            print("\n" + "=" * 60)
            print("📋 LISTADO DE RESERVAS")
            print("=" * 60)

            for reserva in self.reservas:

                print(reserva.info())

        input("\nPresione Enter para continuar...")

    # =====================================================
    # GESTIONAR RESERVAS
    # =====================================================

    def gestionar_reserva(self):

        if not self.reservas:

            print("❌ No existen reservas")

            return

        self.mostrar_reservas()

        try:

            id_reserva = int(
                input("ID de la reserva: ")
            )

            reserva = next(

                (
                    r for r in self.reservas
                    if r.id == id_reserva
                ),

                None
            )

            if not reserva:

                print("❌ Reserva no encontrada")

                return

            print("\n1. Confirmar")
            print("2. Cancelar")

            opcion = input("Seleccione opción: ")

            if opcion == '1':

                forma_pago = input(
                    "Forma de pago: "
                )

                referencia = input(
                    "Referencia: "
                ) or None

                if reserva.confirmar(
                    forma_pago,
                    referencia
                ):

                    print("✅ Reserva confirmada")

                else:

                    print("❌ No fue posible confirmar")

            elif opcion == '2':

                motivo = input(
                    "Motivo cancelación: "
                )

                if reserva.cancelar(motivo):

                    print("✅ Reserva cancelada")

                else:

                    print("❌ No fue posible cancelar")

        except ValueError as e:

            logging.error(e)

            print("❌ ID inválido")

        finally:

            print("✔️ Gestión finalizada")

        input("\nPresione Enter para continuar...")

    # =====================================================
    # DEMOSTRAR SOBRECARGA
    # =====================================================

    def demostrar_sobrecarga(self):

        print("\n" + "=" * 60)
        print("💰 SOBRECARGA DE MÉTODOS")
        print("=" * 60)

        sala = self.servicios[0]

        print(f"\nServicio: {sala.describir()}")

        print(
            f"Sin extras: "
            f"${sala.calcular_costo(3)}"
        )

        print(
            f"Con impuesto: "
            f"${sala.calcular_costo(3, impuesto=True)}"
        )

        print(
            f"Con proyector: "
            f"${sala.calcular_costo(3, proyector=True)}"
        )

        print(
            f"Con descuento + impuesto: "
            f"${sala.calcular_costo(8, descuento=True, impuesto=True)}"
        )

        print(
            "\n✅ El mismo método recibe "
            "diferentes parámetros"
        )

        input("\nPresione Enter para continuar...")


# =========================================================
# EJECUCIÓN PRINCIPAL
# =========================================================

if __name__ == "__main__":

    sistema = Sistema()

    sistema.menu()
