unidades_disponibles = 12
unidades_solicitadas = 8   # prueba también 12 y 15

hay_suficientes = unidades_disponibles >= unidades_solicitadas
son_iguales = unidades_disponibles == unidades_solicitadas
se_exceden = unidades_solicitadas > unidades_disponibles

print("¿Hay suficientes unidades?", hay_suficientes)
print("¿Las cantidades son iguales?", son_iguales)
print("¿Se pidieron más de las disponibles?", se_exceden)
