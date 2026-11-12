import json
from pathlib import Path

ruta = Path("libros.json")

libros = [
    {"codigo": "L001", "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967},
    {"codigo": "L002", "titulo": "La vorágine", "autor": "José Eustasio Rivera", "anio": 1924},
    {"codigo": "L003", "titulo": "María", "autor": "Jorge Isaacs", "anio": 1867},
]

# Guardar
with ruta.open("w", encoding="utf-8") as archivo:
    json.dump(libros, archivo, ensure_ascii=False, indent=4)
print("Libros guardados en", ruta)

# Leer y mostrar 
with ruta.open("r", encoding="utf-8") as archivo:
    cargados = json.load(archivo)

for libro in cargados:
    print(libro["codigo"], "-", libro["titulo"], "-", libro["autor"], "-", libro["anio"])
