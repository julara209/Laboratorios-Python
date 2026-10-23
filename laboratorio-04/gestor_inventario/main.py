import math

from producto import Producto, CATEGORIAS
from almacenamiento import cargar_inventario, guardar_inventario, ErrorAlmacenamiento, RUTA_JSON
from reportes import exportar_csv, RUTA_CSV, BASE_DIR
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
    print("8. Guardar inventario")
    print("9. Exportar reporte CSV")
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
        if not math.isfinite(precio):
            print("El precio debe ser un número finito.")
            continue
        if precio <= 0:
            print("El precio debe ser mayor que cero.")
            continue
        return precio


def mostrar_producto(producto):
    print(producto.codigo, "-", producto.nombre, "-", producto.categoria,
          "- $" + str(producto.precio), "-", producto.cantidad, "unidades")


def guardar(inventario):
    """Intenta guardar e informa. Solo anuncia éxito si la escritura se confirmó."""
    try:
        guardar_inventario(inventario)
    except ErrorAlmacenamiento as error:
        print(error)
        print("Advertencia: los cambios podrían existir solo en memoria.")
        return False
    print("Inventario guardado.")
    return True


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
        return False
    if not inventario.registrar_producto(producto):
        print("El código ya existe. No se registró el producto.")
        return False
    print("Producto registrado.")
    return True


def listar(inventario):
    productos = inventario.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for producto in productos:
        mostrar_producto(producto)


def buscar(inventario):
    producto = inventario.buscar_por_codigo(input("Código: ").strip())
    if producto is None:
        print("El producto no existe.")
    else:
        mostrar_producto(producto)


def actualizar(inventario):
    codigo = input("Código: ").strip()
    if inventario.buscar_por_codigo(codigo) is None:
        print("El producto no existe.")
        return False
    nueva = leer_cantidad("Nueva cantidad: ")
    if inventario.actualizar_existencias(codigo, nueva):
        print("Existencias actualizadas.")
        return True
    print("No se pudo actualizar. Se conserva la cantidad anterior.")
    return False


def eliminar(inventario):
    if inventario.eliminar_producto(input("Código: ").strip()):
        print("Producto eliminado.")
        return True
    print("El producto no existe.")
    return False


def sin_stock(inventario):
    agotados = inventario.productos_sin_stock()
    if not agotados:
        print("No hay productos sin existencias.")
        return
    print("Sin existencias:")
    for nombre in agotados:
        print("-", nombre)


def resumen(inventario):
    datos = inventario.resumen()
    print("Productos registrados:", datos["productos"])
    print("Unidades disponibles:", datos["unidades"])
    print("Valor total: $" + str(datos["valor"]))
    print("Categorías utilizadas:", ", ".join(datos["categorias"]) if datos["categorias"] else "ninguna")


def exportar(inventario):
    try:
        ruta = exportar_csv(inventario)
    except OSError as error:
        print("No se pudo exportar el reporte:", error)
        return
    print("Reporte exportado:", ruta.relative_to(BASE_DIR).as_posix())


def main():
    bloqueado = False
    try:
        inventario = cargar_inventario()
    except ErrorAlmacenamiento as error:
        print("No se pudo cargar el inventario guardado.")
        print(error)
        print("El archivo", RUTA_JSON, "NO será modificado.")
        print("Modo protegido: registrar, actualizar, eliminar y guardar están deshabilitados.")
        inventario = Inventario()
        bloqueado = True

    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion in ("1", "4", "5", "8") and bloqueado:
            print("Operación deshabilitada: el archivo de datos tiene problemas.")
        elif opcion == "1":
            if registrar(inventario):
                guardar(inventario)
        elif opcion == "2":
            listar(inventario)
        elif opcion == "3":
            buscar(inventario)
        elif opcion == "4":
            if actualizar(inventario):
                guardar(inventario)
        elif opcion == "5":
            if eliminar(inventario):
                guardar(inventario)
        elif opcion == "6":
            sin_stock(inventario)
        elif opcion == "7":
            resumen(inventario)
        elif opcion == "8":
            guardar(inventario)
        elif opcion == "9":
            exportar(inventario)
        elif opcion == "0":
            print("Programa finalizado.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
