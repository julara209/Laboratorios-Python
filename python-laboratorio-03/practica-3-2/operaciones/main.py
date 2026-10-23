import operaciones

subtotal = operaciones.calcular_subtotal(85000, 3)
descuento = operaciones.calcular_descuento(subtotal, 10)

print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("Total:", subtotal - descuento)

from operaciones import calcular_subtotal, calcular_descuento

subtotal = calcular_subtotal(40000, 2)
descuento = calcular_descuento(subtotal, 5)
print(subtotal - descuento)
