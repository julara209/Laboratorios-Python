import csv
from pathlib import Path

ruta = Path("reporte.csv")

with ruta.open("r", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for producto in lector:
        print(producto["codigo"], producto["nombre"], producto["precio"])
