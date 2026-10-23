curso = {
    "nombre": "Fundamentos de Python",
    "codigo": "FP01",
    "temas": ["Variables", "Ciclos", "Colecciones"],
    "instructor": {"nombre": "María", "area": "Software"}
}

print("Curso:", curso["nombre"])
print("Segundo tema:", curso["temas"][1])
print("Instructor:", curso["instructor"]["nombre"])
print("Cantidad de temas:", len(curso["temas"]))
