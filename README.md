# Repositorio de laboratorios de Python

- **Aprendiz:** Angie Espinosa
- **Ficha:** 3388087

Repositorio acumulativo con los laboratorios de Python y Django. Cada carpeta conserva sus
ejercicios y su proyecto final; no se reemplazan las versiones anteriores.

| Laboratorio | Tema | Proyecto final | Cómo ejecutarlo |
|-------------|------|----------------|-----------------|
| [laboratorio-01](laboratorio-01/) | Variables, tipos, operadores e `input()` | Cotizador de compra | `cd laboratorio-01` y `python cotizador_compra.py` |
| [laboratorio-02](laboratorio-02/) | Decisiones, ciclos y colecciones | Gestor de inventario (procedural) | `python gestor_inventario.py` dentro de su carpeta |
| [laboratorio-03](laboratorio-03/) | Funciones, módulos y POO | Gestor de inventario con clases | `cd` a `gestor_inventario` y `python main.py` |
| [laboratorio-04](laboratorio-04/) | Excepciones, archivos y persistencia | Gestor de inventario persistente (JSON y CSV) | `cd` a `gestor_inventario` y `python main.py` |
| [laboratorio-06](laboratorio-06/) | Fundamentos de Django: URLs, vistas y plantillas | ClassroomHub (sitio web de 3 páginas) | `cd laboratorio-06`, crear y activar el entorno virtual, `python -m pip install -r requirements.txt` y `python manage.py runserver` |

Según el equipo, `python` puede ser `py` o `python3`.

## Notas sobre el laboratorio 6

- Usa Django 6.1.3 con Python 3.12 o superior. Requiere su propio entorno virtual (`.venv`), que no se sube al repositorio.
- Rutas disponibles: `/`, `/resources/` y `/about/`.
- Pruebas: `python manage.py test pages`.
- Instrucciones completas en el [README del laboratorio](laboratorio-06/README.md).