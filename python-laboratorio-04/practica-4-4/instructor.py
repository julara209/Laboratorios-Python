class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre


class Instructor(Empleado):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre)          
        self.especialidad = especialidad


instructor = Instructor("Ana", "Python")

print(instructor.nombre)
print(instructor.especialidad)
