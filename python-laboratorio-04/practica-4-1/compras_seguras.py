total = 0.0
compras = 0

while True:
    try:
        importe = float(input("Importe de la compra (0 para terminar): "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if importe == 0:
        break
    if importe < 0:
        print("El importe debe ser positivo.")
        continue

    total += importe
    compras += 1
    print("Acumulado:", total)

print("Compras aceptadas:", compras)
print("Total:", total)
