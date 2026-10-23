productos = ["Teclado", "Mouse", "Monitor"]

buscado = input("Buscar producto: ").strip()

if buscado in productos:
    print("Producto encontrado.")
else:
    print("Producto no registrado.")