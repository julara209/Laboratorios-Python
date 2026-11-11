codigo_buscado = input("Código: ").strip()
encontrado = False

for producto in productos:
    if producto["codigo"] == codigo_buscado:
        print("Encontrado:", producto["nombre"])
        encontrado = True
        break

if not encontrado:
    print("No se encontró el producto.")