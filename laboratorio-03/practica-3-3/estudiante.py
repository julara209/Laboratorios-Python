class Estudiante:
    def __init__(self, nombre, ficha, promedio):
        self.nombre = nombre
        self.ficha = ficha
        self.promedio = promedio

    def mostrar_perfil(self):
        print("Nombre:", self.nombre)
        print("Ficha:", self.ficha)
        print("Promedio:", self.promedio)

    def aprobo(self):
        return self.promedio >= 3.0


ana = Estudiante("Ana", "2900001", 2.8)
luis = Estudiante("Luis", "2900002", 4.1)

ana.mostrar_perfil()
print("¿Aprobó Ana?", ana.aprobo())      
print("¿Aprobó Luis?", luis.aprobo())    
