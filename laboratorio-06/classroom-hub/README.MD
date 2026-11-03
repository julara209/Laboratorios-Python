# ClassroomHub

ClassroomHub es un pequeño portal de recursos de aprendizaje construido con Django como primer proyecto web (Laboratorio 6). Tiene tres páginas públicas que se renderizan con plantillas HTML compartidas y muestran datos de ejemplo enviados desde las vistas.

El objetivo del proyecto es practicar y comprender el recorrido **URL → vista → plantilla → respuesta**.

## Versiones utilizadas

- Python 3.12 o superior (3.12, 3.13, 3.14 o 3.15)
- Django 6.1.3

> Si usas Python 3.10 u 3.11, instala `Django==5.2.19` y actualiza `requirements.txt` con esa versión.

## Instalación

1. Clona el repositorio y entra en la carpeta:

   ```bash
   git clone <URL-DEL-REPOSITORIO>
   cd classroom-hub
   ```

2. Crea el entorno virtual:

   ```bash
   python -m venv .venv
   ```

3. Activa el entorno:

   - Windows (PowerShell):

     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```

   - Linux / macOS:

     ```bash
     source .venv/bin/activate
     ```

   > En Windows, si usas el lanzador `py`, reemplaza `python` por `py` al crear el entorno. Si PowerShell bloquea la activación, selecciona el intérprete de `.venv` en VS Code o ejecuta `.\.venv\Scripts\python.exe` directamente.

4. Instala las dependencias:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Verifica la instalación:

   ```bash
   python -m django --version
   ```

   Debe mostrar `6.1.3`.

## Ejecución

Comprueba la configuración e inicia el servidor de desarrollo:

```bash
python manage.py check
python manage.py runserver
```

Abre `http://127.0.0.1:8000/` en el navegador. Para detener el servidor, presiona `Ctrl+C`.

Si el puerto 8000 está ocupado, usa otro: `python manage.py runserver 8001`.

## Rutas públicas

| Ruta | Descripción |
|---|---|
| `/` | Página principal con mensaje de bienvenida |
| `/resources/` | Lista de recursos de ejemplo con su disponibilidad |
| `/about/` | Información sobre el propósito del proyecto |

Cualquier otra dirección responde con un error `404`.

## Pruebas

```bash
python manage.py test pages
```

Resultado esperado: 5 pruebas exitosas. Verifican las tres páginas, la navegación y la respuesta `404` para rutas inexistentes.

## Estructura del proyecto

```text
classroom-hub/
├── manage.py
├── requirements.txt
├── config/                  # Configuración del proyecto
│   ├── settings.py
│   └── urls.py              # Rutas principales
└── pages/                   # Aplicación de páginas públicas
    ├── urls.py              # Rutas de la aplicación
    ├── views.py             # Vistas
    ├── tests.py             # Pruebas automatizadas
    └── templates/pages/
        ├── base.html        # Plantilla base compartida
        ├── home.html
        ├── resources.html
        └── about.html
```

## Qué todavía no incluye

- Base de datos propia ni modelos (los recursos son datos de ejemplo definidos en `pages/views.py`).
- Formularios.
- Inicio de sesión ni usuarios.
- Crear, editar o eliminar recursos (CRUD).
- Archivos estáticos separados (el CSS está dentro de `base.html`).
- Despliegue en producción (`runserver` es solo para desarrollo local).

Estos temas se abordarán en los laboratorios siguientes, empezando por modelos, ORM, migraciones y el administrador de Django.

## Cómo se verificó

- `python manage.py check` termina sin problemas.
- `python manage.py test pages` supera las 5 pruebas.
- Se comprobó manualmente la navegación entre las tres páginas, el estado "Coming soon" de un recurso no disponible, el mensaje de lista vacía y el `404` en `/not-found/`.

## Notas de seguridad

- No subas `.venv/`, `.env` ni `db.sqlite3` al repositorio (ya están en `.gitignore`).
- `DEBUG=True` y la clave generada por Django son solo para el entorno de aprendizaje; no los uses en producción.