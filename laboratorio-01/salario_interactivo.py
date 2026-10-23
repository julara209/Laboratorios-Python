nombre = str(input("Ingresa el nombre del trabajador: "))
horas_trabajadas = int(input("Ingresa las horas trabajadas: "))
valor_hora = float(input("Ingresa el valor por hora: "))

total = (horas_trabajadas * valor_hora)

print(" ")
print("=========================")
print("    RESUMEN DE PAGO      ")
print("=========================")
print("Trabajador:", nombre)
print("Horas:", horas_trabajadas)
print("Valor por hora: $", valor_hora)
print("Pago total: $", total)