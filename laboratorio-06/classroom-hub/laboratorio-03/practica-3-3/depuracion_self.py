class Saludo:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print("Hola,", self.nombre)


saludo = Saludo("Ana")
saludo.mostrar()
