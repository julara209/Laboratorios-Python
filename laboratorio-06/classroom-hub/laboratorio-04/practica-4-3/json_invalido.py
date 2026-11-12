import json
from pathlib import Path

Path("copia_danada.json").write_text('[{"codigo": "P001" "nombre": "Teclado"}]', encoding="utf-8")

try:
    with Path("copia_danada.json").open("r", encoding="utf-8") as archivo:
        productos = json.load(archivo)
except json.JSONDecodeError as error:
    print("El archivo no contiene JSON válido:", error)
except FileNotFoundError:
    print("El archivo no existe.")
