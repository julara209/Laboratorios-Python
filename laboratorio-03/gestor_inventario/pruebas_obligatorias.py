from inventario import Inventario
from producto import Producto


def intentar(*datos):
    try:
        return Producto(*datos)
    except ValueError:
        return None


inv = Inventario()
print("Inventario vacío:", inv.listar_productos(), inv.resumen())

p1 = Producto("P001", "Teclado", "Periféricos", 85000, 4)
print("Registrar P001:", inv.registrar_producto(p1))                                      
print("Registrar P001 otra vez:", inv.registrar_producto(Producto("P001", "X", "Accesorios", 1, 1)))  
print("Código vacío rechazado:", intentar("  ", "A", "Accesorios", 10, 1) is None)
print("Nombre vacío rechazado:", intentar("P9", "   ", "Accesorios", 10, 1) is None)
print("Categoría inválida rechazada:", intentar("P9", "A", "Otra", 10, 1) is None)
print("Precio cero rechazado:", intentar("P9", "A", "Accesorios", 0, 1) is None)
print("Precio negativo rechazado:", intentar("P9", "A", "Accesorios", -5, 1) is None)
print("Cantidad negativa rechazada:", intentar("P9", "A", "Accesorios", 10, -1) is None)
print("Cantidad cero aceptada:", intentar("P9", "A", "Accesorios", 10, 0) is not None)

print("Buscar P001:", inv.buscar_por_codigo("P001").nombre)
print("Buscar P999:", inv.buscar_por_codigo("P999"))
print("Actualizar a 10:", inv.actualizar_existencias("P001", 10), inv.buscar_por_codigo("P001").cantidad)
print("Actualizar a -3:", inv.actualizar_existencias("P001", -3), inv.buscar_por_codigo("P001").cantidad)
print("Eliminar existente:", inv.eliminar_producto("P001"))
print("Eliminar inexistente:", inv.eliminar_producto("P001"))

# Comprobación numérica
inv = Inventario()
inv.registrar_producto(Producto("P001", "Teclado", "Periféricos", 85000, 4))
inv.registrar_producto(Producto("P002", "Mouse", "Periféricos", 45000, 0))
inv.registrar_producto(Producto("P003", "Monitor", "Componentes", 700000, 2))
print(inv.resumen(), inv.productos_sin_stock())
inv.actualizar_existencias("P002", 5)
print(inv.resumen())
