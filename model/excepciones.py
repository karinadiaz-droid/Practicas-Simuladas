# Excepciones personalizadas del sistema
class SistemaError(Exception): #con esto se define una nueva clase llamada SistemaError
    #(Exception) indica que esta clase hereda de la clase Exception (que es la clase base para todas las excepciones en Python)
    """Excepción base del sistema"""
    pass

class ClienteInvalidoError(SistemaError): #ClienteInvalidoError es un tipo específico de SistemaError.
    """Error en datos del cliente"""
    pass #en Python, los bloques (como el cuerpo de una clase o función) no pueden estar vacíos. El pass sirve como un marcador de posición para indicar "no hay contenido adicional"

class ServicioNoDisponibleError(SistemaError): #se lanza cuando se intenta reservar un servicio que tiene disponible = False 
                                               # (desactivado por el administrador), o cuando el servicio no existe. Así se distingue de otros errores de reserva.
    """Error cuando un servicio no está disponible"""
    pass

class ReservaInvalidaError(SistemaError): #se lanza cuando los datos de la reserva no cumplen las reglas de negocio como]: cliente inactivo, duración no positiva, o cualquier otra inconsistencia
    """Error en la creación o gestión de reservas"""
    pass
