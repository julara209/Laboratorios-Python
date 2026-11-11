from pathlib import Path

ruta = Path("mensaje.txt")

try:
    contenido = ruta.read_text(encoding="utf-8")
except FileNotFoundError:
    print("No existe mensaje.txt. Ejecuta primero escribir_archivo.py.")
else:
    print("Contenido:")
    print(contenido)
