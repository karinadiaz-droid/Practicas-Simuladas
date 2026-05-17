# ==========================================
#    SIMULACIÓN DE LAS 10 OPERACIONES
# ==========================================

from repository.memoria import BaseDatosSimulada
from models.cliente import Cliente
from models.servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from models.reserva import Reserva
from utils.logger import Logger
from exceptions.personalizadas import DatosInvalidosException, ServicioNoDisponibleException, OperacionNoPermitidaException

def iniciar_simulador():
    print("=============================================================")
    print(" INICIANDO PRUEBAS UNITARIAS DEL SISTEMA EN MODULOS (10 OPS) ")
    print("=============================================================\n")
    
    # Instanciamos la persistencia en memoria
    db = BaseDatosSimulada()
    
    # Precarga de datos del sistema
    cliente_valido = Cliente(1, "Carlos Blanco", "carlos@email.com")
    db.guardar_cliente(cliente_valido)
    
    sala = ReservaSala(101, "Sala Ejecutiva A", 60.0)
    pc_disponible = AlquilerEquipo(102, "Portátil HP 2026", 20.0, stock=1)
    pc_agotado = AlquilerEquipo(103, "Impresora 5G", 35.0, stock=0)
    asesoria_ti = AsesoriaEspecializada(104, "Consultoría Software FJ", 120.0)
    
    db.guardar_servicio(sala)
    db.guardar_servicio(pc_disponible)
    db.guardar_servicio(pc_agotado)
    db.guardar_servicio(asesoria_ti)
    
    reserva_ejemplo = None

    # ---------------------------------------------------------------
    # OPERACIONES EXITOSAS (1 - 5)
    # ---------------------------------------------------------------
    print(">>> [EJECUTANDO OPERACIONES EXITOSAS]")

    # Operación 1: Registro exitoso en logs
    print("[Op 1] Registrando auditoría de encendido del sistema...")
    Logger.registrar_evento("INFO: El sistema modular se inició correctamente.")

    # Operación 2: Creación exitosa de reserva de sala
    try:
        print("[Op 2] Solicitando reserva de sala válida por 5 horas...")
        reserva_ejemplo = Reserva(501, cliente_valido, sala, 5)
        db.guardar_reserva(reserva_ejemplo)
        print(f"      -> Éxito. Estado inicial: {reserva_ejemplo.estado}")
    except Exception as e:
        print(f"      -> Fallo inesperado: {e}")

    # Operación 3: Ejecución de polimorfismo con parámetros de sobrecarga
    print("[Op 3] Evaluando costos polimórficos con IVA (19%) y Descuento (15%)...")
    costo_con_descuento = sala.calcular_costo(5, impuesto=0.19, descuento=0.15)
    print(f"      -> Costo total computado: ${costo_con_descuento}")

    # Operación 4: Cambio de estado correcto de una reserva
    try:
        print("[Op 4] Modificando estado de reserva a 'Procesada'...")
        reserva_ejemplo.procesar_reserva()
        print(f"      -> Éxito. Nuevo estado: {reserva_ejemplo.estado}")
    except Exception as e:
        print(f"      -> Fallo: {e}")

    # Operación 5: Creación exitosa de consultoría respetando el mínimo de tiempo
    try:
        print("[Op 5] Solicitando asesoría especializada por 3 horas...")
        reserva_consultoria = Reserva(502, cliente_valido, asesoria_ti, 3)
        db.guardar_reserva(reserva_consultoria)
        print("      -> Éxito. Reserva agendada.")
    except Exception as e:
        print(f"      -> Fallo: {e}")


    # ---------------------------------------------------------------
    # OPERACIONES CON ERRORES CONTROLADOS (6 - 10)
    # ---------------------------------------------------------------
    print("\n>>> [EJECUTANDO PRUEBAS DE RESILIENCIA Y ERRORES]")

    # Operación 6: Intento de guardar cliente inválido
    try:
        print("[Op 6] Creando cliente con formato de email corrupto...")
        cliente_malo = Cliente(2, "Jose Armando Blanco", "email_invalido.com")
    except DatosInvalidosException as error:
        print(f"      -> Atrapado: {error}")
        Logger.registrar_evento(f"ERROR OPERACIONAL: {error}")

    # Operación 7: Violación de límites de tiempo en Sala
    try:
        print("[Op 7] Intentando reservar sala por un lapso prohibido de 18 horas...")
        reserva_mala = Reserva(503, cliente_valido, sala, 18)
    except DatosInvalidosException as error:
        print(f"      -> Atrapado: {error}")
        Logger.registrar_evento(f"ERROR OPERACIONAL: {error}")

    # Operación 8: Intento de reserva de artículos sin existencias
    try:
        print("[Op 8] Solicitando alquiler de equipo con stock en cero...")
        reserva_sin_stock = Reserva(504, cliente_valido, pc_agotado, 2)
    except ServicioNoDisponibleException as error:
        print(f"      -> Atrapado: {error}")
        Logger.registrar_evento(f"ERROR OPERACIONAL: {error}")

    # Operación 9: Violación de condiciones de negocio en asesoría
    try:
        print("[Op 9] Agendando asesoría flash ilegal (Menos del mínimo de 2 horas)...")
        reserva_corta = Reserva(505, cliente_valido, asesoria_ti, 1)
    except DatosInvalidosException as error:
        print(f"      -> Atrapado: {error}")
        Logger.registrar_evento(f"ERROR OPERACIONAL: {error}")

    # Operación 10: Uso de try-except-finally e intento de operación prohibida
    print("[Op 10] Intentando dar de baja la reserva ya completada de la Op 4...")
    try:
        reserva_ejemplo.cancelar_reserva()
    except OperacionNoPermitidaException as error:
        print(f"      -> Atrapado de forma segura: {error}")
        Logger.registrar_evento(f"ERROR OPERACIONAL: {error}")
    finally:
        print("      -> [Bloque Finally] Procesos de limpieza ejecutados. Aplicación estable.")

    print("\n=============================================================")
    print(" SIMULACIÓN MODULAR FINALIZADA CON ÉXITO SIN CAÍDAS DEL LOGIC ")
    print("=============================================================")

if __name__ == "__main__":
    iniciar_simulador()
