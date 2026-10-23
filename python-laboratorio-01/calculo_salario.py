nombre_trabajador = "Luisa"
horas_trabajadas = 40
valor_hora = 300000.0

pago_total = horas_trabajadas * valor_hora

APORTE = 0.04
valor_aporte = pago_total * APORTE

print("=========================")
print("    CALCULA SALARIO      ")
print("=========================")
print("Nombre:", nombre_trabajador)
print("Horas trabajadas:", horas_trabajadas)
print("Valor por hora: $", valor_hora)
print("Pago total: $", pago_total)
print("Aporte del 4%: $", valor_aporte)