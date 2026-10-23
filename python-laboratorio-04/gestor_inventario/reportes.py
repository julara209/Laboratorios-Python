import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_CSV = BASE_DIR / "reportes" / "inventario.csv"

CAMPOS = ["codigo", "nombre", "categoria", "precio", "cantidad", "valor_inventario"]


def exportar_csv(inventario, ruta=RUTA_CSV):
    """Escribe el CSV y devuelve su ruta. Puede lanzar OSError si falla la escritura."""
    filas = []
    for producto in inventario.listar_productos():
        fila = producto.a_diccionario()
        fila["valor_inventario"] = producto.calcular_valor()   # precio * cantidad
        filas.append(fila)

    ruta.parent.mkdir(parents=True, exist_ok=True)
    with ruta.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(filas)
    return ruta
