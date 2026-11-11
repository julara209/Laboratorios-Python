productos = ["Teclado", "Mouse", "Monitor"]

productos.remove("Mouse")

print(productos)

nombre = input("Producto a eliminar: ").strip()

if nombre in productos:
    productos.remove(nombre)
    print("Producto eliminado.")
else:
    print("No se encontró el producto.")