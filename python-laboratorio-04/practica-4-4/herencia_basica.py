class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def describir(self):
        return f"Empleado: {self.nombre}"


class Instructor(Empleado):
    def explicar(self):
        return f"{self.nombre} está orientando una actividad."


persona = Instructor("Laura")

print(persona.describir())   
print(persona.explicar())    
