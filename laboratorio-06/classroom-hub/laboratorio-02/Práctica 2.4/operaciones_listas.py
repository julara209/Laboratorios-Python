productos = ["Teclado", "Mouse", "Monitor"]

productos[1] = "Mouse inalámbrico"
productos.insert(1, "Cámara web")

eliminado = productos.pop()

print("Elementos:", productos)
print("Extraído:", eliminado)