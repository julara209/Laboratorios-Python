"""Pruebas automáticas de la tabla de pruebas obligatorias (trabajan en una carpeta temporal,
nunca sobre datos/productos.json)."""
import csv
import json
import math
import tempfile
from pathlib import Path

from almacenamiento import cargar_inventario, guardar_inventario, ErrorAlmacenamiento
from inventario import Inventario
from producto import Producto
from reportes import exportar_csv

resultados = []


def comprobar(nombre, condicion):
    resultados.append(condicion)
    print(("OK   " if condicion else "FALLA"), nombre)


def rechaza(*datos):
    try:
        Producto(*datos)
    except ValueError:
        return True
    return False


def lanza_error_carga(ruta):
    try:
        cargar_inventario(ruta)
    except ErrorAlmacenamiento:
        return True
    return False


with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    ruta = tmp / "datos" / "productos.json"

    # Primera ejecución
    comprobar("JSON inexistente -> inventario vacío", cargar_inventario(ruta).listar_productos() == [])

    # Guardar y reiniciar
    inv = Inventario()
    inv.registrar_producto(Producto("P001", "Teclado", "Periféricos", 85000, 4))
    inv.registrar_producto(Producto("P002", "Mouse", "Periféricos", 45000, 0))
    guardar_inventario(inv, ruta)
    contenido = json.loads(ruta.read_text(encoding="utf-8"))
    comprobar("Guardar dos productos -> JSON con ambos", len(contenido) == 2)
    inv2 = cargar_inventario(ruta)
    comprobar("Reiniciar -> se recuperan los dos", [p.codigo for p in inv2.listar_productos()] == ["P001", "P002"])
    comprobar("Se recuperan objetos Producto con sus datos",
              inv2.buscar_por_codigo("P001").precio == 85000.0 and inv2.buscar_por_codigo("P001").cantidad == 4)

    # Reglas
    comprobar("Código duplicado se rechaza", inv2.registrar_producto(Producto("P001", "X", "Accesorios", 1, 1)) is False)
    comprobar("Categoría desconocida se rechaza", rechaza("P9", "A", "Otra", 10, 1))
    comprobar("Precio negativo se rechaza", rechaza("P9", "A", "Accesorios", -1, 1))
    comprobar("Precio nan se rechaza", rechaza("P9", "A", "Accesorios", float("nan"), 1))
    comprobar("Precio inf se rechaza", rechaza("P9", "A", "Accesorios", math.inf, 1))
    comprobar("Cantidad negativa se rechaza", rechaza("P9", "A", "Accesorios", 10, -1))
    comprobar("Cantidad de tipo incorrecto se rechaza", rechaza("P9", "A", "Accesorios", 10, "3"))
    comprobar("Cantidad cero se acepta", not rechaza("P9", "A", "Accesorios", 10, 0))

    # Persistencia de cambios
    inv2.actualizar_existencias("P002", 5)
    inv2.eliminar_producto("P001")
    guardar_inventario(inv2, ruta)
    inv3 = cargar_inventario(ruta)
    comprobar("Actualización se refleja tras reiniciar", inv3.buscar_por_codigo("P002").cantidad == 5)
    comprobar("Eliminado sigue eliminado tras reiniciar", inv3.buscar_por_codigo("P001") is None)

    # Archivos dañados: se informa y NO se sobrescriben
    malo = tmp / "malo.json"
    malo.write_text('[{"codigo": "P001" "nombre": "X"}]', encoding="utf-8")
    original = malo.read_text(encoding="utf-8")
    comprobar("JSON con sintaxis incorrecta -> error", lanza_error_carga(malo))
    comprobar("...y el archivo queda intacto", malo.read_text(encoding="utf-8") == original)

    estructura = tmp / "estructura.json"
    estructura.write_text('{"codigo": "P001"}', encoding="utf-8")
    comprobar("JSON con estructura inesperada -> error", lanza_error_carga(estructura))

    incompleto = tmp / "incompleto.json"
    incompleto.write_text('[{"codigo": "P001"}]', encoding="utf-8")
    comprobar("Registro con campos faltantes -> error", lanza_error_carga(incompleto))

    repetido = tmp / "repetido.json"
    repetido.write_text(json.dumps([
        {"codigo": "P001", "nombre": "A", "categoria": "Accesorios", "precio": 10, "cantidad": 1},
        {"codigo": "P001", "nombre": "B", "categoria": "Accesorios", "precio": 20, "cantidad": 2},
    ]), encoding="utf-8")
    comprobar("JSON con código repetido -> sin carga parcial", lanza_error_carga(repetido))

    una_mala = tmp / "una_mala.json"
    una_mala.write_text(json.dumps([
        {"codigo": "P001", "nombre": "A", "categoria": "Accesorios", "precio": 10, "cantidad": 1},
        {"codigo": "P002", "nombre": "B", "categoria": "Accesorios", "precio": -20, "cantidad": 2},
    ]), encoding="utf-8")
    comprobar("Un registro inválido -> se rechaza TODA la carga", lanza_error_carga(una_mala))

    # Error de escritura: la "ruta" del archivo es una carpeta
    carpeta = tmp / "es_carpeta.json"
    carpeta.mkdir()
    try:
        guardar_inventario(inv2, carpeta)
        fallo_informado = False
    except ErrorAlmacenamiento:
        fallo_informado = True
    comprobar("Error de escritura -> se informa (no se confirma)", fallo_informado)

    # Prueba numérica + CSV
    inv = Inventario()
    inv.registrar_producto(Producto("P001", "Teclado", "Periféricos", 85000, 4))
    inv.registrar_producto(Producto("P002", "Mouse", "Periféricos", 45000, 0))
    inv.registrar_producto(Producto("P003", "Monitor", "Componentes", 700000, 2))
    r = inv.resumen()
    comprobar("Resumen: 3 productos, 6 unidades, $1740000.0, 2 categorías",
              (r["productos"], r["unidades"], r["valor"], len(r["categorias"])) == (3, 6, 1740000.0, 2))
    comprobar("Sin existencias: Mouse", inv.productos_sin_stock() == ["Mouse"])

    ruta2 = tmp / "datos2" / "productos.json"
    guardar_inventario(inv, ruta2)
    r2 = cargar_inventario(ruta2).resumen()
    comprobar("Tras reiniciar los resultados son los mismos", r2 == r)

    inv.actualizar_existencias("P002", 5)
    guardar_inventario(inv, ruta2)
    r3 = cargar_inventario(ruta2).resumen()
    comprobar("Mouse a 5: 11 unidades y $1965000.0", (r3["unidades"], r3["valor"]) == (11, 1965000.0))

    ruta_csv = exportar_csv(inv, tmp / "reportes" / "inventario.csv")
    with ruta_csv.open(newline="", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    comprobar("CSV con encabezados correctos",
              list(filas[0].keys()) == ["codigo", "nombre", "categoria", "precio", "cantidad", "valor_inventario"])
    p002 = [f for f in filas if f["codigo"] == "P002"][0]
    comprobar("CSV: P002 tiene valor_inventario 225000.0", float(p002["valor_inventario"]) == 225000.0)

print()
print("RESULTADO:", sum(resultados), "de", len(resultados), "pruebas correctas")
