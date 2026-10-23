from pathlib import Path

carpeta = Path("reportes")
carpeta.mkdir(parents=True, exist_ok=True)

ruta = carpeta / "resumen.txt"
ruta.write_text(
    "Productos registrados: 3\n"
    "Unidades disponibles: 6\n"
    "Valor del inventario: 1740000\n",
    encoding="utf-8",
)

print(ruta.read_text(encoding="utf-8"))
print("Guardado en:", ruta.resolve())
