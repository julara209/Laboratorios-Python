import validaciones

nombre = input("Nombre: ")
categoria = input("Categoría: ").strip()
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

if (
    validaciones.nombre_valido(nombre)
    and validaciones.categoria_valida(categoria, validaciones.CATEGORIAS)
    and validaciones.precio_valido(precio)
    and validaciones.cantidad_valida(cantidad)
):
    print("Datos aceptados.")
else:
    print("Revisa los datos.")
