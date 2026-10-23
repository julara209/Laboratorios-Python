materias = ["Matemáticas", "Programación", "Física"]
materias.append("Inglés")   

for posicion, materia in enumerate(materias, start=1):
    print(posicion, "-", materia)
