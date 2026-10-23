import json
from pathlib import Path

from inventario import Inventario

BASE_DIR = Path(__file__).resolve().parent
RUTA_JSON = BASE_DIR / "datos" / "productos.json"


class ErrorAlmacenamiento(Exception):
    """Fallo al leer o escribir el archivo del inventario."""


def guardar_inventario(inventario, ruta=RUTA_JSON):
    """Guarda el inventario en JSON. Lanza ErrorAlmacenamiento si no se pudo confirmar."""
    datos = inventario.exportar_datos()
    try:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with ruta.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
    except (OSError, TypeError) as error:
        raise ErrorAlmacenamiento(f"No se pudo guardar: {error}") from error
    return ruta


def cargar_inventario(ruta=RUTA_JSON):
    """Devuelve un Inventario.

    - Archivo inexistente: inventario vacío.
    - Archivo válido: inventario con sus productos.
    - Archivo dañado o inválido: lanza ErrorAlmacenamiento y NO toca el archivo.
    """
    if not ruta.exists():
        return Inventario()
    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except json.JSONDecodeError as error:
        raise ErrorAlmacenamiento(f"El JSON tiene un error de formato: {error}") from error
    except (OSError, UnicodeDecodeError) as error:
        raise ErrorAlmacenamiento(f"No se pudo leer el archivo: {error}") from error

    try:
        return Inventario.desde_datos(datos)
    except ValueError as error:
        raise ErrorAlmacenamiento(f"Datos inválidos en el archivo: {error}") from error
