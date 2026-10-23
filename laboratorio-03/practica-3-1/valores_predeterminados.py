def calcular_total(precio, cantidad, descuento=0):
    subtotal = precio * cantidad
    return subtotal - subtotal * descuento / 100


print(calcular_total(50000, 2))                                  # 100000.0
print(calcular_total(50000, 2, 10))                              # 90000.0
print(calcular_total(precio=50000, cantidad=2, descuento=20))    # 80000.0

