from modelo.cliente import Cliente
from modelo.servicio import ReservaSala
from modelo.reserva import Reserva

try:
    cliente1 = Cliente("Karina Diaz", 22)
    servicio1 = ReservaSala("Sala principal", 50)

    reserva1 = Reserva(cliente1, servicio1)
    reserva1.confirmar()

    print("Reserva creada correctamente")
    print("Estado:", reserva1.estado)
    print("Costo:", servicio1.calcular_costo(2))

except Exception as e:
    print("Error:", e)
