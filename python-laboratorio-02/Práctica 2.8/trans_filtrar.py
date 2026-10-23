nombres = ["  ana ", "CARLOS", " Laura ", ""]

normalizados = [
    nombre.strip().title()
    for nombre in nombres
    if nombre.strip() != ""
]

print(normalizados)