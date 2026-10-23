productos = ["Teclado", "Mouse", "Monitor"]
nuevos = ["Impresora", "Cámara"]

productos[1] = "Mouse inalámbrico"
print("1)", productos)

productos.insert(0, "Parlantes")
print("2)", productos)

productos.extend(nuevos)
print("3)", productos)

productos.remove("Monitor")
print("4)", productos)

ultimo = productos.pop()
print("5)", productos)
print("Extraído:", ultimo)
