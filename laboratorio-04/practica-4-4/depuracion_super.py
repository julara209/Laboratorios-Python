class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class Aprendiz(Persona):
    def __init__(self, nombre, ficha):
        super().__init__(nombre)       
        self.ficha = ficha


aprendiz = Aprendiz("Carlos", "123456")
print(aprendiz.nombre, aprendiz.ficha)
