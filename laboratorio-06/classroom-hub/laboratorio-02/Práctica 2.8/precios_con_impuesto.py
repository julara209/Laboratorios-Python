precios = [10000, 20000, 50000, 80000]

con_for = []
for precio in precios:
    con_for.append(precio * 1.19)

con_comprension = [precio * 1.19 for precio in precios]

print(con_for)
print(con_comprension)
print("¿Equivalentes?", con_for == con_comprension)
