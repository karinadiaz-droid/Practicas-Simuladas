class Cliente:
    def __init__(self, nombre, edad):
        if not nombre:
            raise ValueError("Nombre inválido")
        if edad <= 0:
            raise ValueError("Edad inválida")

        self.nombre = nombre
        self.edad = edad
      
