import json
from pathlib import Path

RUTA = Path("productos.json")


def cargar():
    if not RUTA.exists():
        print("No existe el archivo: se inicia con una lista vacía.")
        return [], False
    try:
        with RUTA.open("r", encoding="utf-8") as archivo:
            productos = json.load(archivo)
    except json.JSONDecodeError as error:
        print("Error de formato en el JSON:", error)
        print("No se sobrescribirá el archivo. Revísalo antes de continuar.")
        return [], True
    if not isinstance(productos, list):
        print("Estructura inesperada: se esperaba una lista. No se sobrescribirá.")
        return [], True
    print("Productos cargados:", len(productos))
    return productos, False


productos, bloqueado = cargar()
if bloqueado:
    print("Guardado deshabilitado hasta resolver el problema.")
else:
    print("Se puede trabajar y guardar con normalidad.")
