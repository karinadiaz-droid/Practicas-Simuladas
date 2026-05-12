lass Estudiante:
    def _init_(Self, nombre, edad, codigo, carrera,):
        try:
            if not nombre or not codigo or not carrera:
                raise ValueError("los campos nombre, codigo y carrera no pueden estar vacios.")
            if edad <= 0:
                raise ValueError("la edad debe ser mayor que cero.")
            Self.nombre = nombre
            Self.edad = edad
            Self.codigo = codigo
            Self.carrera = carrera
        except ValueError as e:
            print(f"Error al crear el estudiante: {e}")
            
    def mostrar_datos(Self):
        return f"nombre: {Self.nombre}, edad: {Self.edad}, codigo: {Self.codigo}, carrera: {Self.carrera}"
    
    def presentarse(Self):
        return f"hola mi nombre es {Self.nombre} y estudio {Self.carrera}."
