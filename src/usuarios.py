class Usuario:
    def __init__(self, nombre, correo, edad, intereses):
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.intereses = intereses

    def to_dict(self):
        
        return {
            "nombre": self.nombre,
            "correo": self.correo,
            "edad": self.edad,
            "intereses": self.intereses
        }