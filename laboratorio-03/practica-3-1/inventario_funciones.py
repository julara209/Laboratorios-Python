def mostrar_productos(productos):
    for p in productos:
        print(p["codigo"], "-", p["nombre"], "-", f"${p['precio']}", "-", p["cantidad"], "unidades")


def buscar_producto(productos, codigo):
    for p in productos:
        if p["codigo"] == codigo:
            return p
    return None


def valor_inventario(productos):
    total = 0
    for p in productos:
        total += p["precio"] * p["cantidad"]
    return total


def productos_sin_stock(productos):
    return [p["nombre"] for p in productos if p["cantidad"] == 0]


productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 85000.0, "cantidad": 4},
    {"codigo": "P002", "nombre": "Mouse", "precio": 45000.0, "cantidad": 0},
    {"codigo": "P003", "nombre": "Monitor", "precio": 700000.0, "cantidad": 2}
]

print("== Productos ==")
mostrar_productos(productos)

print("== Búsqueda ==")
print("P003:", buscar_producto(productos, "P003"))
print("P999:", buscar_producto(productos, "P999"))

print("== Valor del inventario ==")
print(valor_inventario(productos))         

print("== Sin stock ==")
print(productos_sin_stock(productos))       
