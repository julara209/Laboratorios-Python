notas = [2.5, 3.0, 4.8, 1.9, 3.7, 5.0]

aprobadas = [n for n in notas if n >= 3.0]
inferiores = [n for n in notas if n < 3.0]
dobles = [n * 2 for n in notas]

print("Aprobadas:", aprobadas)
print("Inferiores a 3.0:", inferiores)
print("Multiplicadas por 2:", dobles)
