
producto = {"codigo": "P001", "nombre": "Teclado"}
print(producto.get("marca", "Sin marca"))   # corrección con get()

productos = [{"precio": 85000, "cantidad": 4}, {"precio": 700000, "cantidad": 2}]
mal = sum([p["precio"] for p in productos])                    # solo suma precios
bien = sum([p["precio"] * p["cantidad"] for p in productos])   # precio * cantidad
print("Incorrecto:", mal, "| Correcto:", bien)
