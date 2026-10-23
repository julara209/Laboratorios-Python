from producto import Producto
from inventario import Inventario

inventario = Inventario()

print("Agregar P001:", inventario.agregar(Producto("P001", "Teclado")))   # True
print("Agregar P002:", inventario.agregar(Producto("P002", "Mouse")))     # True
print("Agregar P001 repetido:", inventario.agregar(Producto("P001", "Otro")))   # False

for producto in inventario.listar():
    print(producto.codigo, "-", producto.nombre)

encontrado = inventario.buscar_por_codigo("P002")
if encontrado is not None:
    print("Encontrado:", encontrado.nombre)
else:
    print("Producto no registrado.")

print("Eliminar P999 (no existe):", inventario.eliminar("P999"))   # False
print("Eliminar P002:", inventario.eliminar("P002"))               # True
print("Quedan:", len(inventario.listar()))                          # 1
