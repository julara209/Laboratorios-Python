"""Depuración: problemas provocados en una copia del proyecto, su causa y la corrección."""

# 1) Olvidar encoding="utf-8" al guardar texto con caracteres especiales
#    ruta.open("w") -> en algunos sistemas usa otra codificación y "Periféricos" se guarda mal
#    (o falla al leer). Corrección: SIEMPRE encoding="utf-8" al abrir y al leer.

# 2) Ruta relativa que apunta a otra carpeta
#    Path("datos/productos.json") depende de desde dónde ejecutas Python.
#    Corrección: BASE_DIR = Path(__file__).resolve().parent y RUTA_JSON = BASE_DIR / "datos" / ...

# 3) json.dump() directamente sobre un objeto Producto
#    -> TypeError: Object of type Producto is not JSON serializable.
#    Corrección: guardar inventario.exportar_datos() (lista de diccionarios).

# 4) Cargar un JSON con código repetido sin validar
#    Causa: se agregaban los registros a la lista sin comprobar duplicados.
#    Corrección: Inventario.desde_datos() registra uno por uno con registrar_producto()
#    y lanza ValueError si un código ya existe.

# 5) Sobrescribir un JSON dañado con una lista vacía
#    except Exception: datos = []; guardar(datos)   <- pierde información recuperable.
#    Corrección: cargar_inventario() lanza ErrorAlmacenamiento; main.py entra en modo
#    protegido y deshabilita guardar y modificar.

# 6) CSV que suma precios en lugar de multiplicar por cantidades
#    fila["valor_inventario"] = producto.precio              <- incorrecto
#    fila["valor_inventario"] = producto.calcular_valor()    <- correcto: precio * cantidad

# 7) Modificar datos y asumir que ya se guardaron
#    Causa: faltaba llamar a guardar() tras una operación aceptada, o se ignoraba su resultado.
#    Corrección: guardar() tras cada operación válida y avisar si el guardado falla.
