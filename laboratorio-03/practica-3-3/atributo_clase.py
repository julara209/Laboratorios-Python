class Registro:
    elementos = []


primero = Registro()
segundo = Registro()

primero.elementos.append("Teclado")
print(segundo.elementos)

# Solución: crear la lista en __init__ (atributo de INSTANCIA)
class Registro:
    def __init__(self):
        self.elementos = []


primero = Registro()
segundo = Registro()

primero.elementos.append("Teclado")

print("Primero:", primero.elementos)
print("Segundo:", segundo.elementos)