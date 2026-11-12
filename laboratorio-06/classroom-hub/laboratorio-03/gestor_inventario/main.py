from producto import Producto, CATEGORIAS
from inventario import Inventario


def mostrar_menu():
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
    print("0. Salir")


def leer_cantidad(mensaje="Cantidad: "):
    while True:
        try:
            cantidad = int(input(mensaje))
        except ValueError:
            print("Debes escribir un número entero.")
            continue

        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            continue

        return cantidad


def leer_precio(mensaje="Precio: "):
    while True:
        try:
            precio = float(input(mensaje))
        except ValueError:
            print("Debes escribir un número válido.")
            continue

        if precio <= 0:
            print("El precio debe ser mayor que cero.")
            continue

        return precio


def mostrar_producto(producto):
    print(producto.codigo, "-", producto.nombre, "-", producto.categoria,
          "- $" + str(float(producto.precio)), "-", producto.cantidad, "unidades")


def registrar(inventario):
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría (" + ", ".join(CATEGORIAS) + "): ").strip()
    precio = leer_precio()
    cantidad = leer_cantidad()

    try:
        producto = Producto(codigo, nombre, categoria, precio, cantidad)
    except ValueError as error:
        print("No se registró el producto:", error)
        return

    if inventario.registrar_producto(producto):
        print("Producto registrado.")
    else:
        print("El código ya existe. No se registró el producto.")


def listar(inventario):
    productos = inventario.listar_productos()
    if len(productos) == 0:
        print("No hay productos registrados.")
        return
    for producto in productos:
        mostrar_producto(producto)


def buscar(inventario):
    codigo = input("Código: ").strip()
    producto = inventario.buscar_por_codigo(codigo)
    if producto is None:
        print("El producto no existe.")
    else:
        mostrar_producto(producto)


def actualizar(inventario):
    codigo = input("Código: ").strip()
    if inventario.buscar_por_codigo(codigo) is None:
        print("El producto no existe.")
        return
    nueva = leer_cantidad("Nueva cantidad: ")
    if inventario.actualizar_existencias(codigo, nueva):
        print("Existencias actualizadas.")
    else:
        print("No se pudo actualizar. Se conserva la cantidad anterior.")


def eliminar(inventario):
    codigo = input("Código: ").strip()
    if inventario.eliminar_producto(codigo):
        print("Producto eliminado.")
    else:
        print("El producto no existe.")


def sin_stock(inventario):
    agotados = inventario.productos_sin_stock()
    if len(agotados) == 0:
        print("No hay productos sin existencias.")
        return
    print("Sin existencias:")
    for nombre in agotados:
        print("-", nombre)


def resumen(inventario):
    datos = inventario.resumen()
    print("Productos registrados:", datos["productos"])
    print("Unidades disponibles:", datos["unidades"])
    print("Valor del inventario: $" + str(datos["valor"]))
    if datos["categorias"]:
        print("Categorías utilizadas:", ", ".join(datos["categorias"]))
    else:
        print("Categorías utilizadas: ninguna")


def main():
    inventario = Inventario()
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            registrar(inventario)
        elif opcion == "2":
            listar(inventario)
        elif opcion == "3":
            buscar(inventario)
        elif opcion == "4":
            actualizar(inventario)
        elif opcion == "5":
            eliminar(inventario)
        elif opcion == "6":
            sin_stock(inventario)
        elif opcion == "7":
            resumen(inventario)
        elif opcion == "0":
            print("Programa finalizado.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
