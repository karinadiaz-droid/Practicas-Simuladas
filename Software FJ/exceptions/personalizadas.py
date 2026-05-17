class SistemaException(Exception):
    """Clase base para todas las excepciones del proyecto."""
    pass

class DatosInvalidosException(SistemaException):
    """Se lanza cuando los datos ingresados no cumplen con las validaciones."""
    pass

class OperacionNoPermitidaException(SistemaException):
    """Se lanza cuando se intenta cambiar el estado de una reserva de forma ilegal."""
    pass

class ServicioNoDisponibleException(SistemaException):
    """Se lanza cuando no hay stock o disponibilidad del servicio solicitado."""
    pass
