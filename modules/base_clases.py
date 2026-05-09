from abc import ABC, abstractmethod

class Service(ABC):
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    @abstractmethod
    def calculate_total(self, quantity):
        """Método abstracto que deben implementar los hijos."""
        pass
