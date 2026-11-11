# Laboratorio 2: Decisiones, ciclos y colecciones

Ejercicios de condiciones, ciclos, listas, tuplas, conjuntos, diccionarios y comprensiones,
más el **gestor de inventario** de consola.

## Contenido

| Carpeta | Tema |
|---------|------|
| Práctica 2.1 | Comparaciones y decisiones (`if`, `elif`, `else`) |
| Práctica 2.2 | Condiciones compuestas y validaciones |
| Práctica 2.3 | Ciclos `for` y `while` |
| Práctica 2.4 | Listas |
| Práctica 2.5 | Tuplas |
| Práctica 2.6 | Conjuntos |
| Práctica 2.7 | Diccionarios y colecciones anidadas |
| Práctica 2.8 | Comprensiones |
| Práctica 2.9 | Gestor de inventario (`gestor_inventario.py`) |

## Gestor de inventario

Cada producto es un diccionario (`codigo`, `nombre`, `categoria`, `precio`, `cantidad`) guardado
en la lista `productos`. Las categorías permitidas están en la tupla `CATEGORIAS`.
Los datos permanecen en memoria mientras el programa está abierto.

Opciones: registrar, listar, buscar por código, actualizar existencias, eliminar,
consultar productos sin stock y resumen del inventario.

## Ejecución

Desde la carpeta `Práctica 2.9`:

```
python gestor_inventario.py
```
(según el equipo: `py` o `python3`)

## Pruebas realizadas

| Prueba | Resultado |
|--------|-----------|
| Listar sin productos | Mensaje de inventario vacío |
| Registrar código repetido | Rechazado |
| Nombre vacío, categoría inválida, precio negativo, cantidad negativa | Rechazados |
| Cantidad cero | Aceptada como producto sin stock |
| Buscar código inexistente | Informa que no existe |
| Actualizar a -3 | Rechazado, se conserva la cantidad anterior |
| Eliminar código inexistente | Informa sin fallar |
| P001 (85000 x 4), P002 (45000 x 0), P003 (700000 x 2) | 3 productos, 6 unidades, $1740000.0, 2 categorías, Mouse sin stock |