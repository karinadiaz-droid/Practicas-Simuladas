class GestionReservasError(Exception):
    """Clase base para otras excepciones de este sistema."""
    pass

class ClienteInvalidoError(GestionReservasError):
    """Se lanza cuando los datos del cliente no cumplen las validaciones."""
    pass

class ServicioNoDisponibleError(GestionReservasError):
    """Se lanza cuando se intenta reservar un servicio agotado o inexistente."""
    pass

class ErrorProcesamientoReserva(GestionReservasError):
    """Se lanza ante fallos críticos durante el cálculo o confirmación."""
    pass
