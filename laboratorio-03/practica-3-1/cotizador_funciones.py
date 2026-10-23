def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_descuento(subtotal, porcentaje):
    return subtotal * porcentaje / 100


def calcular_impuesto(base, porcentaje):
    return base * porcentaje / 100


precio = 100000
cantidad = 2
porcentaje_descuento = 10
porcentaje_impuesto = 19

subtotal = calcular_subtotal(precio, cantidad)
descuento = calcular_descuento(subtotal, porcentaje_descuento)
base = subtotal - descuento
impuesto = calcular_impuesto(base, porcentaje_impuesto)
total = base + impuesto

print("Subtotal:", subtotal)                        # 200000
print("Descuento:", descuento)                      # 20000.0
print("Base después del descuento:", base)          # 180000.0
print("Impuesto:", impuesto)                        # 34200.0
print("Total:", total)                              # 214200.0
