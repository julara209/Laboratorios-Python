nombre_producto = "Teclado inalambrico"
precio = 100000.0
cantidad = 2
porcentaje_descuento = 0.10
porcentaje_impuesto = 0.19

subtotal = cantidad * precio
valor_descuento = subtotal * porcentaje_descuento
base_descuento = subtotal - valor_descuento
valor_impuesto = base_descuento * porcentaje_impuesto
total_final = base_descuento + valor_descuento


print("=========================")
print("    CALCULA SALARIO      ")
print("=========================")
print("Nombre del producto:", nombre_producto)
print("Precio unitario: $", precio)
print("Cantidad:", cantidad)
print("Subtotal: $", subtotal)
print("Descuento: $", valor_descuento)
print("Base después del descuento: $", base_descuento)
print("Impuesto: $", valor_impuesto)
print("Total final: $", total_final)

