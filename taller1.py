#nombrar la clase estudiante
class Estudiante:
    #Llamar metodo constructor
    def __init__(self,nombre,edad,cedula,carerra):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.carrera = carrera

    def estudiar(self):
        print(f"Hola soy {self.nombre} y estoy estudiando  {self.carrera}")

while True:
    nombre = input("Digite el nombre del estudiante:")

    while True:
        edad = (input("Digite la edad del estudiante:"))
        if edad.isdigit():
            edad = int(edad)
            break
        else:
            print("No valido. Digite una edad correcta.")

    while True:
        cedula = (input("Digite la identificacion del estudiante:"))
        if cedula.isdigit():
            cedula = int(cedula)
            break
        else:
            print("No valido. Digite su numero de identificacion.")

    carrera = input("Digite la carrera del estudiante:")
    estudiante = Estudiante(nombre,edad,cedula,carrera)
    
    print("Opciones:")
    print("1- Estudiar")
    print("2- Salir")

    opcion = input("Seleccione una opcion (1/2): ")

    if opcion == '1':
        estudiante.estudiar()
        print(f"""
        El nombre del estudiante: {nombre}
        La edad del estudiante: {edad}
        La cedula del estudiante: {cedula}
        La carrera del estudiante: {carrera}
        """)
        break
    elif opcion == '2':
        print("Saliendo del programa")
        break
    else:
        print("Opcion no valida. Intente de nuevo.")
    
    
    