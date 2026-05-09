from modelo.cliente import Cliente
from modelo.servicio import Servicio
from modelo.reserva import Reserva

try:
    cliente1 = Cliente("Karina Diaz", "karina@email.com")
    servicio1 = Servicio("Reserva de sala", 50)

    reserva1 = Reserva(cliente1, servicio1)
    reserva1.confirmar()

    print("Reserva creada correctamente")
    print("Estado:", reserva1.estado)

except Exception as e:
    print("Error:", e)
