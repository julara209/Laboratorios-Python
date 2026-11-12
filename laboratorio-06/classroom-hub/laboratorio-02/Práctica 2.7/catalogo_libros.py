libros = [
    {"codigo": "L001", "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967},
    {"codigo": "L002", "titulo": "El coronel no tiene quien le escriba", "autor": "Gabriel García Márquez", "anio": 1961},
    {"codigo": "L003", "titulo": "La vorágine", "autor": "José Eustasio Rivera", "anio": 1924}
]

codigo = input("Código a buscar: ").strip()
encontrado = None

for libro in libros:
    if libro["codigo"] == codigo:
        encontrado = libro
        break

if encontrado is not None:
    print(encontrado["titulo"], "-", encontrado["autor"], "-", encontrado["anio"])
else:
    print("Libro no localizado.")

nuevo_codigo = input("Código del nuevo libro: ").strip()
repetido = False
for libro in libros:
    if libro["codigo"] == nuevo_codigo:
        repetido = True
        break

if repetido:
    print("Ese código ya existe.")
elif nuevo_codigo == "":
    print("El código no puede estar vacío.")
else:
    libros.append({
        "codigo": nuevo_codigo,
        "titulo": input("Título: ").strip(),
        "autor": input("Autor: ").strip(),
        "anio": int(input("Año: "))
    })
    print("Libro agregado.")
