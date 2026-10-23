def agotados_for(productos):
    nombres = []
    for p in productos:
        if p["cantidad"] == 0:
            nombres.append(p["nombre"])
    return nombres


def agotados(productos):
    return [p["nombre"] for p in productos if p["cantidad"] == 0]


datos = [
    {"nombre": "Teclado", "cantidad": 4},
    {"nombre": "Mouse", "cantidad": 0},
    {"nombre": "Monitor", "cantidad": 0}
]
print(agotados_for(datos))
print(agotados(datos))
