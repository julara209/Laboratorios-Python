# Gestor de inventario (POO)

Aplicación de consola que gestiona productos en memoria usando clases, módulos y funciones.

## Estructura

```
gestor_inventario/
├── main.py                  # menú, lectura de datos y mensajes
├── producto.py              # clase Producto y CATEGORIAS
├── inventario.py            # clase Inventario
├── pruebas_independencia.py # dos inventarios no comparten datos
├── pruebas_obligatorias.py  # pruebas automáticas de la tabla del laboratorio
├── depuracion_gestor.py     # errores provocados y su causa
└── README.md
```

## Ejecución

```
python main.py
```
(según tu equipo: `py main.py` o `python3 main.py`)

## Responsabilidades

- **Producto**: guarda código, nombre, categoría, precio y cantidad; valida desde `__init__`;
  el código es de solo lectura; calcula `precio * cantidad`.
- **Inventario**: mantiene su propia lista de productos; evita códigos repetidos; busca,
  actualiza, elimina y genera informes. No usa `input()` ni `print()`.
- **main.py**: única parte que interactúa con el usuario; captura `ValueError` al registrar
  y vuelve a pedir números inválidos.

## Pruebas realizadas

| Caso | Resultado observado |
|------|---------------------|
| Inventario vacío | Listado vacío y resumen en cero |
| Registrar P001 | Aceptado |
| Registrar P001 de nuevo | Rechazado |
| Código o nombre vacío | Rechazado |
| Categoría no permitida | Rechazado |
| Precio cero o negativo | Rechazado |
| Cantidad negativa | Rechazada |
| Cantidad cero | Aceptada (sin stock) |
| Buscar P001 / P999 | Muestra datos / informa que no existe |
| Actualizar a 10 / a -3 | Cambia / rechaza y conserva |
| Eliminar existente / inexistente | Elimina / informa sin fallar |
| Texto en campo numérico | Mensaje y nueva oportunidad |
| Resumen con P001, P002, P003 | 3 productos, 6 unidades, $1740000.0, 2 categorías |
| P002 a 5 unidades | 11 unidades, $1965000.0 |
| Independencia | Primero: 1, Segundo: 0 |
