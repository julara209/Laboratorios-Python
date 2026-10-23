valor_inventario = 0

for producto in productos:
    valor_inventario += producto["precio"] * producto["cantidad"]

print("Valor del inventario:", valor_inventario)