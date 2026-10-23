import json


class Producto:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def a_diccionario(self):
        return {"codigo": self.codigo, "nombre": self.nombre}

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos["codigo"], datos["nombre"])


producto = Producto("P001", "Teclado")

# Un objeto propio NO se serializa directamente:
try:
    print(json.dumps(producto))
except TypeError as error:
    print("TypeError:", error)

# Solución: convertir a diccionario
print(json.dumps(producto.a_diccionario(), ensure_ascii=False))

# Reconstruir un objeto desde un diccionario
nuevo = Producto.desde_diccionario({"codigo": "P002", "nombre": "Mouse"})
print(type(nuevo))
print(nuevo.nombre)
