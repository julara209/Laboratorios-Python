# Gestor de inventario persistente

Aplicación de consola que conserva los productos entre ejecuciones usando JSON y exporta reportes CSV.

## Estructura

```
gestor_inventario/
├── main.py                  # menú, lectura de datos y mensajes
├── producto.py              # clase Producto (validaciones, a_diccionario, desde_diccionario)
├── inventario.py            # clase Inventario (colección de productos, exportar_datos, desde_datos)
├── almacenamiento.py        # leer y escribir datos/productos.json
├── reportes.py              # exportar reportes/inventario.csv
├── pruebas_persistencia.py  # pruebas automáticas (carpeta temporal)
├── depuracion_gestor.py     # errores provocados, causa y corrección
├── datos/productos.json     # se genera al guardar
└── reportes/inventario.csv  # se genera al exportar
```

## Ejecución

```
python main.py
python pruebas_persistencia.py
```
(según tu equipo: `py` o `python3`)

## Responsabilidades

| Módulo | Conoce el sistema de archivos | Responsabilidad |
|--------|:---:|-----------------|
| producto.py | No | Reglas de un producto y conversión a/desde diccionario |
| inventario.py | No | Colección de productos, operaciones y carga sin estados parciales |
| almacenamiento.py | Sí | Guardar y cargar JSON; informa errores con `ErrorAlmacenamiento` |
| reportes.py | Sí | Generar el CSV con `valor_inventario = precio * cantidad` |
| main.py | No directamente | Interacción con el usuario y coordinación |

## Comportamiento ante archivos

- JSON inexistente: se inicia con inventario vacío.
- JSON válido: se recuperan los productos.
- JSON dañado, con estructura inesperada, registros inválidos o códigos repetidos: se informa,
  **no se sobrescribe** y la aplicación entra en modo protegido (no permite modificar ni guardar).
- Tras cada operación aceptada (registrar, actualizar, eliminar) se guarda; solo se anuncia
  "Inventario guardado." si la escritura se confirmó.

## Pruebas realizadas

Ejecuta `python pruebas_persistencia.py` para repetir las comprobaciones de la tabla obligatoria,
la prueba numérica (3 productos, 6 unidades, $1740000.0; con Mouse a 5: 11 unidades, $1965000.0)
y el CSV (P002 con valor_inventario 225000.0). Las pruebas manuales con archivo dañado deben
hacerse sobre una copia de `productos.json`; anota aquí tus resultados reales.
