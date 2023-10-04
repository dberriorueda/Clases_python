#nombrar la clase
class Persona:
    def __init__(self,nombre,edad,cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
    def caminar(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años y mi numero de cedula es {self.cedula}")
persona = Persona("Diego",30,1035945)
#print(persona.nombre)
persona.caminar()