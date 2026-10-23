try:
    precio = float(input("Precio: "))
    print("Precio ingresado:", precio)
except ValueError:
    print("Debes escribir un número válido.")
