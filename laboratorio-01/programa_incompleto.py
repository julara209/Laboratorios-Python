producto = str(input("Ingrese el nombre del producto: "))
precio = float(input("Ingrese el valor unitario:"))
cantidad = int(input("Ingrese la cantidad:"))

subtotal = precio * cantidad

print("Producto:", producto)
print("Subtotal: $", subtotal)