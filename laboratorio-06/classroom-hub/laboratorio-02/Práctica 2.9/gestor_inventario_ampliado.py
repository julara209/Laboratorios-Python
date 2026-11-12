# Lista de diccionarios para productos
# Tupla de categorías válidas
# Ciclo del menú
#   Registrar (cambia la lista)
#   Listar (lee)
#   Buscar (lee)
#   Actualizar (cambia un diccionario)
#   Eliminar (cambia la lista)
#   Filtrar sin stock (lee)
#   Mostrar resumen (lee)

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")

productos = []
opcion = ""

while opcion != "0":
    print()
    print("================================")
    print("       GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("8. Aumentar o disminuir existencias")
    print("9. Listar ordenados por nombre")
    print("10. Diccionario código -> nombre")
    print("11. Buscar por categoría")
    print("12. Producto con mayor valor de inventario")
    print("0. Salir")

    opcion = input("Opción: ").strip()

    if opcion == "1":
        codigo = input("Código: ").strip()
        nombre = input("Nombre: ").strip()
        categoria = input("Categoría: ").strip()
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))

        repetido = False
        for p in productos:
            if p["codigo"] == codigo:
                repetido = True
                break

        if codigo == "" or nombre == "" or categoria == "":
            print("Los campos de texto no pueden estar vacíos.")
        elif repetido:
            print("El código ya existe.")
        elif categoria not in CATEGORIAS:
            print("Categoría no permitida. Opciones:", ", ".join(CATEGORIAS))
        elif precio <= 0:
            print("El precio debe ser mayor que cero.")
        elif cantidad < 0:
            print("La cantidad no puede ser negativa.")
        else:
            productos.append({
                "codigo": codigo,
                "nombre": nombre,
                "categoria": categoria,
                "precio": precio,
                "cantidad": cantidad
            })
            print("Producto registrado.")

    elif opcion == "2":
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            for p in productos:
                print(p["codigo"], "-", p["nombre"], "-", p["categoria"],
                      "- $" + str(p["precio"]), "-", p["cantidad"], "unidades")

    elif opcion == "3":
        codigo_buscado = input("Código: ").strip()
        encontrado = None
        for p in productos:
            if p["codigo"] == codigo_buscado:
                encontrado = p
                break

        if encontrado is not None:
            print(encontrado["codigo"], "-", encontrado["nombre"], "-",
                  encontrado["categoria"], "- $" + str(encontrado["precio"]),
                  "-", encontrado["cantidad"], "unidades")
        else:
            print("El producto no existe.")

    elif opcion == "4":
        codigo_buscado = input("Código: ").strip()
        encontrado = None
        for p in productos:
            if p["codigo"] == codigo_buscado:
                encontrado = p
                break

        if encontrado is None:
            print("El producto no existe.")
        else:
            nueva = int(input("Nueva cantidad: "))
            if nueva < 0:
                print("La cantidad no puede ser negativa. Se conserva la anterior.")
            else:
                encontrado["cantidad"] = nueva
                print("Existencias actualizadas.")

    elif opcion == "5":
        codigo_buscado = input("Código: ").strip()
        encontrado = None
        for p in productos:
            if p["codigo"] == codigo_buscado:
                encontrado = p
                break

        if encontrado is not None:
            productos.remove(encontrado)
            print("Producto eliminado.")
        else:
            print("El producto no existe.")

    elif opcion == "6":
        agotados = [p["nombre"] for p in productos if p["cantidad"] == 0]
        if len(agotados) == 0:
            print("No hay productos sin existencias.")
        else:
            print("Sin existencias:")
            for nombre in agotados:
                print("-", nombre)

    elif opcion == "7":
        total_unidades = sum([p["cantidad"] for p in productos])
        valor = sum([p["precio"] * p["cantidad"] for p in productos])
        usadas = {p["categoria"] for p in productos}

        print("Productos:", len(productos))
        print("Unidades:", total_unidades)
        print("Valor del inventario: $" + str(valor))
        print("Categorías utilizadas:", ", ".join(sorted(usadas)) if usadas else "Ninguna")

    elif opcion == "8":
        codigo_buscado = input("Código: ").strip()
        encontrado = None
        for p in productos:
            if p["codigo"] == codigo_buscado:
                encontrado = p
                break

        if encontrado is None:
            print("El producto no existe.")
        else:
            movimiento = int(input("Movimiento (+ entra, - sale): "))
            nueva = encontrado["cantidad"] + movimiento
            if nueva < 0:
                print("Operación rechazada: las existencias quedarían negativas.")
            else:
                encontrado["cantidad"] = nueva
                print("Existencias actuales:", nueva)

    elif opcion == "9":
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            for p in sorted(productos, key=lambda x: x["nombre"]):
                print(p["codigo"], "-", p["nombre"], "-", p["cantidad"], "unidades")

    elif opcion == "10":
        codigo_nombre = {p["codigo"]: p["nombre"] for p in productos}
        print(codigo_nombre)

    elif opcion == "11":
        cat = input("Categoría: ").strip()
        de_categoria = [p["nombre"] for p in productos if p["categoria"] == cat]
        if len(de_categoria) == 0:
            print("No hay productos en esa categoría.")
        else:
            print("Productos en", cat + ":")
            for nombre in de_categoria:
                print("-", nombre)

    elif opcion == "12":
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            # lambda: mini-función anónima (aún no vista en el curso)
            mayor = max(productos, key=lambda x: x["precio"] * x["cantidad"])
            print(mayor["nombre"], "- valor: $" + str(mayor["precio"] * mayor["cantidad"]))

    elif opcion == "0":
        print("Programa finalizado.")
    else:
        print("Opción no válida.")
