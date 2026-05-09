class SistemaReservasError(Exception):
    """Excepción base del sistema"""
    pass

class ClienteInvalidoError(SistemaReservasError):
    """Error relacionado con datos inválidos del cliente"""
    pass

class ServicioNoDisponibleError(SistemaReservasError):
    """Error cuando un servicio no está disponible"""
    pass

class ReservaInvalidaError(SistemaReservasError):
    """Error en la creación o modificación de reservas"""
    pass

class ParametroFaltanteError(SistemaReservasError):
    """Error cuando faltan parámetros obligatorios"""
    pass

class CalculoInconsistenteError(SistemaReservasError):
    """Error en cálculos de costos"""
    pass
