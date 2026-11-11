lista1 = ["Ana", "Luis", "Ana", "Camila"]
lista2 = ["Luis", "Pedro", "Camila", "Sara"]

participantes = set(lista1 + lista2)
print("Personas diferentes:", len(participantes))

participantes.add("Julián")
participantes.discard("Pedro")
print(participantes)
print("Personas ahora:", len(participantes))
