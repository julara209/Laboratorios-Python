from pathlib import Path

ruta = Path("historial.txt")

ruta.write_text("", encoding="utf-8")            # empezar limpio para la demostración
with open(ruta, "a", encoding="utf-8") as archivo:
    archivo.write("Registro 1\n")
with open(ruta, "a", encoding="utf-8") as archivo:
    archivo.write("Registro 2\n")


print(ruta.read_text(encoding="utf-8"))
