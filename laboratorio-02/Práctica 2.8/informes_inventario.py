productos = [
    {"nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"nombre": "Mouse", "precio": 45000, "cantidad": 0},
    {"nombre": "Monitor", "precio": 700000, "cantidad": 2}
]

sin_existencias = [p for p in productos if p["cantidad"] == 0]
caros = [p["nombre"] for p in productos if p["precio"] > 100000]
cantidades = {p["cantidad"] for p in productos}
nombre_precio = {p["nombre"]: p["precio"] for p in productos}

print("Sin existencias:", sin_existencias)
print("Precio > 100000:", caros)
print("Cantidades diferentes:", cantidades)
print("Nombre -> precio:", nombre_precio)

disponibles = [p["nombre"] for p in productos if p["cantidad"] > 0]
valores = [p["precio"] * p["cantidad"] for p in productos]
print("Disponibles:", disponibles)
print("Valor total:", sum(valores))
