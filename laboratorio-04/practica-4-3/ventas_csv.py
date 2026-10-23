import csv
from pathlib import Path

ventas = [
    {"codigo": "V001", "producto": "Teclado", "cantidad": 2, "total": 170000},
    {"codigo": "V002", "producto": "Mouse", "cantidad": 3, "total": 135000},
    {"codigo": "V003", "producto": "Monitor", "cantidad": 1, "total": 700000},
    {"codigo": "V004", "producto": "Memoria USB", "cantidad": 5, "total": 125000},
]

ruta = Path("ventas.csv")
with ruta.open("w", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["codigo", "producto", "cantidad", "total"])
    escritor.writeheader()
    escritor.writerows(ventas)

total_vendido = 0
with ruta.open("r", newline="", encoding="utf-8") as archivo:
    for fila in csv.DictReader(archivo):
        total_vendido += float(fila["total"])      

print("Total vendido:", total_vendido)     
