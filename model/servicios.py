from abc import ABC, abstractmethod #ABC es una clase base abstracta. Una clase que hereda de ABC no puede ser instanciada directamente si tiene al menos un método abstracto.
from .excepciones import ServicioNoDisponibleError

class Servicio(ABC): #Indica que Servicio hereda de ABC, por lo tanto es una clase abstracta.
    _id_counter = 1

    def __init__(self, nombre, costo_base):
        self.id = Servicio._id_counter
        Servicio._id_counter += 1
        self.nombre = nombre
        self.costo_base = costo_base
        self.disponible = True

    @abstractmethod
    def calcular_costo(self, horas, **kwargs):
        pass

    def describir(self): # este es un método concreto que devuelve una descripción básica del servicio.
        return f"{self.nombre} (${self.costo_base}/hora)"

    def activar(self):
        self.disponible = True
                                #estos 2 métodos ermiten controlar la disponibilidad del servicio. Por ejemplo,
                                #si una sala está en mantenimiento, se desactiva y ya no se pueden crear reservas con ella
    def desactivar(self):
        self.disponible = False

#Reserva de Sala
class ReservaSala(Servicio):
    def __init__(self, nombre, costo_base, tiene_proyector=False):
        super().__init__(nombre, costo_base)
        self.tiene_proyector = tiene_proyector #atributo específico de la sala que indica si la sala cuenta con proyector

    def calcular_costo(self, horas, **kwargs):
        if horas <= 0:
            raise ValueError("Las horas deben ser positivas")
        costo = self.costo_base * horas
        if kwargs.get('proyector') and self.tiene_proyector:
            costo += 30 * horas
        if kwargs.get('impuesto'):
            costo *= 1.19
        if horas > 5 and kwargs.get('descuento', False):
            costo *= 0.90
        return round(costo, 2)

#Alquiler de Equipo
class AlquilerEquipo(Servicio):
    def __init__(self, nombre, costo_base, requiere_seguro=False):
        super().__init__(nombre, costo_base)
        self.requiere_seguro = requiere_seguro

    def calcular_costo(self, horas, **kwargs):
        if horas <= 0:
            raise ValueError("Horas inválidas")
        costo = self.costo_base * horas
        if kwargs.get('seguro') and self.requiere_seguro:
            costo += 15 * horas
        if kwargs.get('impuesto', True):   # Por defecto con impuesto
            costo *= 1.19
        return round(costo, 2)

#Asesoría
class Asesoria(Servicio):
    def __init__(self, nombre, costo_base, nivel="Junior"):
        super().__init__(nombre, costo_base)
        niveles = {'Junior': 1.0, 'Senior': 1.5, 'Master': 2.0}
        self.factor = niveles.get(nivel, 1.0)

    def calcular_costo(self, horas, **kwargs):
        if horas <= 0:
            raise ValueError("Horas inválidas")
        costo = self.costo_base * self.factor * horas
        if kwargs.get('premium'):
            costo *= 1.25
        if kwargs.get('impuesto', True):
            costo *= 1.19
        return round(costo, 2)
