import csv
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
RUTA_JSON = BASE / "inventario.json"
RUTA_CSV = BASE / "inventario.csv"


def guardar(productos):
    with RUTA_JSON.open("w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=4)


def cargar():
    if not RUTA_JSON.exists():
        return [], False                       
    try:
        with RUTA_JSON.open("r", encoding="utf-8") as archivo:
            return json.load(archivo), False
    except json.JSONDecodeError as error:
        print("JSON dañado:", error, "- no se sobrescribirá.")
        return [], True                        


def exportar(productos):
    with RUTA_CSV.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["codigo", "nombre", "precio", "cantidad"])
        escritor.writeheader()
        escritor.writerows(productos)


productos, bloqueado = cargar()
print("Productos cargados:", len(productos))

opcion = ""
while opcion != "0":
    print("\n1. Agregar producto\n2. Listar\n3. Guardar JSON\n4. Exportar CSV\n0. Salir")
    opcion = input("Opción: ").strip()
    if opcion == "1":
        productos.append({
            "codigo": input("Código: ").strip(),
            "nombre": input("Nombre: ").strip(),
            "precio": float(input("Precio: ")),
            "cantidad": int(input("Cantidad: ")),
        })
    elif opcion == "2":
        for p in productos:
            print(p["codigo"], "-", p["nombre"], "-", p["precio"], "-", p["cantidad"])
    elif opcion == "3":
        if bloqueado:
            print("Guardado deshabilitado: el JSON existente está dañado.")
        else:
            guardar(productos)
            print("Inventario guardado.")
    elif opcion == "4":
        exportar(productos)
        print("CSV exportado:", RUTA_CSV.name)
    elif opcion == "0":
        print("Programa terminado.")
    else:
        print("Opción no válida.")
