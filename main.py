from datetime import datetime, timedelta
from models.cliente import Cliente
from models.servicios import ReservaSala, AlquilerEquipo, Asesoria
from models.reserva import Reserva
from models.excepciones import ClienteInvalidoError, ServicioNoDisponibleError, ReservaInvalidaError

class Sistema:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []
        self._cargar_ejemplo()

    def _cargar_ejemplo(self):
        # Servicios de ejemplo
        self.servicios = [
            ReservaSala("Sala Premium", 120, tiene_proyector=True),
            ReservaSala("Sala Básica", 80, tiene_proyector=False),
            AlquilerEquipo("Proyector 4K", 50, requiere_seguro=True),
            AlquilerEquipo("Laptop Gaming", 30, requiere_seguro=False),
            Asesoria("Python Avanzado", 100, nivel="Senior"),
            Asesoria("Machine Learning", 150, nivel="Master")
        ]
        # Clientes de ejemplo
        try:
            self.clientes.append(Cliente("Karina Diaz", "karina@mail.com", "3137654321"))
            self.clientes.append(Cliente("Jose Blanco", "jose@mail.com", "3121234567"))
        except ClienteInvalidoError as e:
            print(f"Error cargando ejemplo: {e}")

    def menu(self): #con esta parte del código estamos creando lo primero que el usuario va a ver
        while True:
            print("\n" + "="*60)
            print("🏢 SISTEMA DE RESERVAS")
            print("="*60)
            print("1. Gestionar Clientes")
            print("2. Ver Servicios")
            print("3. Nueva Reserva (para hacer una reserva primero debe ser un cliente)")
            print("4. Ver Reservas")
            print("5. Gestionar Reserva (Confirmar/Cancelar)")
            print("6. Demostrar Sobrecarga de Métodos")
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
                print("\n👋 ¡Hasta luego! Revisa 'sistema.log' para eventos.\n")
                break
            else:
                print("❌ Opción inválida")

    def submenu_clientes(self):
        while True:
            print("\n" + "-"*40)
            print("CLIENTES")
            print("1. Listar clientes")
            print("2. Crear nuevo cliente")
            print("3. Activar/Desactivar cliente")
            print("4. Volver")
            op = input("Opción: ")
            if op == '1':
                if not self.clientes:
                    print("No hay clientes.")
                else:
                    for c in self.clientes:
                        print(c.info())
                input("Presione Enter...")
            elif op == '2':
                try:
                    nom = input("Nombre completo: ").strip()
                    email = input("Email: ").strip()
                    tel = input("Teléfono: ").strip()
                    cliente = Cliente(nom, email, tel)
                    self.clientes.append(cliente)
                    print(f"✅ Cliente {cliente.nombre} creado con ID {cliente.id}")
                except ClienteInvalidoError as e:
                    print(f"❌ Error: {e}")
                except Exception as e:
                    print(f"❌ Error inesperado: {e}")
                input("Presione Enter...")
            elif op == '3':
                if not self.clientes:
                    print("No hay clientes.")
                else:
                    for c in self.clientes:
                        print(c.info())
                    try:
                        id_cli = int(input("ID del cliente: "))
                        cliente = next((c for c in self.clientes if c.id == id_cli), None)
                        if cliente:
                            print(f"Estado actual: {'Activo' if cliente.activo else 'Inactivo'}")
                            accion = input("¿(a)activar o (d)desactivar? ").lower()
                            if accion == 'a':
                                cliente.activo = True
                                print("✅ Cliente activado")
                            elif accion == 'd':
                                cliente.activo = False
                                print("✅ Cliente desactivado")
                            else:
                                print("Opción inválida")
                        else:
                            print("Cliente no encontrado")
                    except ValueError:
                        print("ID inválido")
                input("Presione Enter...")
            elif op == '4':
                break
            else:
                print("Opción inválida")

    def mostrar_servicios(self):
        print("\n" + "="*60)
        print("🎯 SERVICIOS DISPONIBLES")
        for s in self.servicios:
            estado = "✅ Disponible" if s.disponible else "❌ No disponible"
            print(f"ID:{s.id} | {s.describir()} | {estado}")
        input("Presione Enter...")

    def nueva_reserva(self):
        if not self.clientes:
            print("❌ No hay clientes registrados. Cree uno primero.")
            return
        print("\n📋 Clientes:")
        for c in self.clientes:
            print(f"  {c.id}. {c.nombre} ({'Activo' if c.activo else 'Inactivo'})")
        try:
            id_cli = int(input("ID del cliente: "))
            cliente = next((c for c in self.clientes if c.id == id_cli and c.activo), None)
            if not cliente:
                print("❌ Cliente no encontrado o inactivo")
                return
        except ValueError:
            print("ID inválido")
            return

        print("\n🎯 Servicios:")
        for s in self.servicios:
            if s.disponible:
                print(f"  {s.id}. {s.describir()}")
        try:
            id_ser = int(input("ID del servicio: "))
            servicio = next((s for s in self.servicios if s.id == id_ser and s.disponible), None)
            if not servicio:
                print("❌ Servicio no disponible")
                return
        except ValueError:
            print("ID inválido")
            return

        try:
            horas = float(input("Duración en horas: "))
            if horas <= 0:
                print("La duración debe ser positiva")
                return
        except ValueError:
            print("Número inválido")
            return

        # Parámetros extras según el tipo de servicio (demostración de polimorfismo)
        extras = {}
        if isinstance(servicio, ReservaSala):
            if input("¿Incluir proyector? (s/n): ").lower() == 's':
                extras['proyector'] = True
            if input("¿Aplicar impuesto 19%? (s/n): ").lower() == 's':
                extras['impuesto'] = True
            if horas > 5 and input("¿Aplicar descuento por volumen? (s/n): ").lower() == 's':
                extras['descuento'] = True
        elif isinstance(servicio, AlquilerEquipo):
            if servicio.requiere_seguro and input("¿Incluir seguro? (s/n): ").lower() == 's':
                extras['seguro'] = True
            if input("¿Aplicar impuesto? (s/n): ").lower() == 's':
                extras['impuesto'] = True
        elif isinstance(servicio, Asesoria):
            if input("¿Modalidad premium (+25%)? (s/n): ").lower() == 's':
                extras['premium'] = True
            if input("¿Aplicar impuesto? (s/n): ").lower() == 's':
                extras['impuesto'] = True

        fecha = datetime.now() + timedelta(days=1)  # Fecha por defecto: mañana
        try:
            reserva = Reserva(cliente, servicio, fecha, horas, extras)
            self.reservas.append(reserva)
            print(f"\n✅ Reserva #{reserva.id} creada exitosamente.")
            print(f"   Costo total: ${reserva.costo}")
            if input("¿Confirmar reserva ahora? (s/n): ").lower() == 's':
                forma = input("Forma de pago (efectivo/tarjeta/transferencia): ").strip()
                ref = input("Referencia (opcional): ").strip() or None
                if reserva.confirmar(forma, ref):
                    print("✅ Reserva confirmada")
                else:
                    print("❌ No se pudo confirmar")
        except (ReservaInvalidaError, ServicioNoDisponibleError) as e:
            print(f"❌ Error al crear reserva: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        input("Presione Enter...")

    def mostrar_reservas(self):
        if not self.reservas:
            print("❌ No hay reservas.")
        else:
            print("\n" + "="*60)
            print("📋 LISTADO DE RESERVAS")
            for r in self.reservas:
                print(r.info())
        input("Presione Enter...")

    def gestionar_reserva(self):
        if not self.reservas:
            print("No hay reservas.")
            return
        self.mostrar_reservas()
        try:
            id_r = int(input("ID de la reserva a gestionar: "))
            reserva = next((r for r in self.reservas if r.id == id_r), None)
            if not reserva:
                print("Reserva no encontrada")
                return
            print(f"\nEstado actual: {reserva.estado}")
            print("1. Confirmar")
            print("2. Cancelar")
            print("3. Volver")
            op = input("Opción: ")
            if op == '1':
                forma = input("Forma de pago: ")
                ref = input("Referencia (opcional): ") or None
                if reserva.confirmar(forma, ref):
                    print("✅ Reserva confirmada")
                else:
                    print("❌ No se pudo confirmar (solo reservas pendientes)")
            elif op == '2':
                motivo = input("Motivo de cancelación: ")
                if reserva.cancelar(motivo):
                    print("✅ Reserva cancelada")
                else:
                    print("❌ No se pudo cancelar (solo reservas pendientes o confirmadas)")
            else:
                print("Volviendo...")
        except ValueError:
            print("ID inválido")
        input("Presione Enter...")

    def demostrar_sobrecarga(self):
        print("\n" + "="*60)
        print("💰 DEMOSTRACIÓN DE SOBRECARGA DE MÉTODOS")
        print("Un mismo método 'calcular_costo' se comporta diferente según los parámetros\n")
        # Tomamos un servicio de ejemplo
        sala = self.servicios[0]  # Sala Premium
        print(f"Servicio: {sala.describir()}")
        print(f"  • Sin extras: ${sala.calcular_costo(3)}")
        print(f"  • Con impuesto 19%: ${sala.calcular_costo(3, impuesto=True)}")
        print(f"  • Con proyector + impuesto: ${sala.calcular_costo(3, proyector=True, impuesto=True)}")
        print(f"  • 8 horas con descuento + impuesto: ${sala.calcular_costo(8, descuento=True, impuesto=True)}")
        print("\nNota: El mismo método acepta diferentes combinaciones de parámetros opcionales.")
        input("Presione Enter...")

if __name__ == "__main__":
    sistema = Sistema()
    sistema.menu()
