producto = {
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 85000.0
}

for clave in producto:
    print(clave)

for valor in producto.values():
    print(valor)

for clave, valor in producto.items():
    print(clave, ":", valor)