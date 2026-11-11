import operaciones

# Error original: print(calcular_subtotal(10000, 3))
# Con "import operaciones" el nombre pertenece al módulo, hay que usar el prefijo.
print(operaciones.calcular_subtotal(10000, 3))

# Otra opción válida:
# from operaciones import calcular_subtotal
# print(calcular_subtotal(10000, 3))
