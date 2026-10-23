total = 0
depositos = 0

valor = float(input("Depósito (0 para terminar): "))

while valor != 0:
    if valor < 0:
        print("El depósito debe ser positivo.")
    else:
        total += valor
        depositos += 1
        print("Ahorro acumulado:", total)
    valor = float(input("Depósito (0 para terminar): "))

print("Depósitos válidos:", depositos)
print("Total ahorrado:", total)
