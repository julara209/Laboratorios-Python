invitados = []

for i in range(5):
    nombre = input(f"Invitado {i + 1}: ").strip()
    invitados.append(nombre)

print("Cantidad de invitados:", len(invitados))
print(invitados)
