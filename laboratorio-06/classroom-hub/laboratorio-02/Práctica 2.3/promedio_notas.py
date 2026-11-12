cantidad = int(input("Cantidad de notas: "))

if cantidad <= 0:
    print("La cantidad debe ser mayor que cero.")
else:
    suma = 0
    for i in range(1, cantidad + 1):
        nota = float(input(f"Nota {i}: "))
        suma += nota
    print("Promedio:", suma / cantidad)
