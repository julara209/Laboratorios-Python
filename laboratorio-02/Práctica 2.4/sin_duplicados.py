productos = ["Teclado", "Mouse"]
nombre = input("Producto nuevo: ").strip()

if nombre == "":
    print("No puede registrarse un nombre vacío.")
elif nombre in productos:
    print("El producto está repetido.")
else:
    productos.append(nombre)
    print("Producto agregado.")

print(productos)
