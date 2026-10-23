original = ["Teclado", "Mouse"]
otra_referencia = original

otra_referencia.append("Monitor")

print(original)

original = ["Teclado", "Mouse"]
copia = original.copy()

copia.append("Monitor")

print("Original:", original)
print("Copia:", copia)