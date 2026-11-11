<<<<<<< HEAD
# ClassroomHub

ClassroomHub es un portal de recursos de aprendizaje construido con Django (Laboratorios 6 y 7). Los recursos y categorías se guardan en una base de datos MariaDB/MySQL, se administran desde Django Admin y se muestran en páginas públicas de solo lectura.

El recorrido que practica el proyecto es **URL → vista → plantilla → respuesta**, ahora con datos persistentes: **modelo → base de datos → vista → plantilla**.

## Requisitos

- Python 3.12
- Django 4.2 LTS (la versión que usa este proyecto; ver requirements.txt)
- MariaDB 10.4 o superior, o MySQL 8
- Controlador `mysqlclient` y `python-dotenv` (incluidos en `requirements.txt`)

## Instalación

1. Clona el repositorio y entra en la carpeta del proyecto:

   ```bash
   git clone https://github.com/julara209/Laboratorios-Python.git
   cd Laboratorios-Python/laboratorio-07/classroom-hub
   ```

2. Crea y activa el entorno virtual:

   ```bash
   py -3.12 -m venv venv
   venv\Scripts\activate          # Windows (CMD)
   # source venv/bin/activate     # Linux / macOS
   ```

3. Instala las dependencias:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Creación de la base de datos

Conéctate al servidor como administrador y ejecuta:

```sql
CREATE DATABASE classroom_hub CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'classroomhub_user'@'localhost' IDENTIFIED BY 'TU_CONTRASEÑA';
GRANT ALL PRIVILEGES ON classroom_hub.* TO 'classroomhub_user'@'localhost';
GRANT ALL PRIVILEGES ON test_classroom_hub.* TO 'classroomhub_user'@'localhost';
FLUSH PRIVILEGES;
```

La cuenta de la aplicación solo tiene permisos sobre `classroom_hub` y sobre la base descartable de pruebas `test_classroom_hub`. No se usan permisos globales.

## Configuración (`.env`)

Copia la plantilla y completa los valores reales:

```bash
copy .env.example .env         # Windows
# cp .env.example .env         # Linux / macOS
```

Variables: `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`. El archivo `.env` contiene secretos y **no se versiona**.

## Conexión

`config/settings.py` usa el backend `django.db.backends.mysql` (válido tanto para MySQL como para MariaDB) con el controlador `mysqlclient`, y lee los datos de conexión desde `.env`.

## Migraciones y superusuario

```bash
python manage.py migrate
python manage.py createsuperuser
```

Los archivos de migración (`pages/migrations/`) sí se versionan; el contenido de la base no.

## Ejecución

```bash
python manage.py check
python manage.py runserver
```

| Ruta | Descripción |
|---|---|
| `/` | Página principal |
| `/resources/` | Recursos guardados en la base de datos, con su categoría |
| `/resources/available/` | Solo recursos disponibles (solo lectura) |
| `/about/` | Propósito del proyecto |
| `/admin/` | Django Admin para mantener categorías y recursos |

Cualquier otra dirección responde con `404`.

## Pruebas

```bash
python manage.py test pages
```

Las pruebas usan una base descartable (`test_classroom_hub`) que Django crea y elimina, sin tocar los datos reales. Verifican las páginas, la lectura desde la base, la relación con la categoría, la protección `PROTECT` al borrar categorías y la ruta de recursos disponibles.

## Estructura

```text
classroom-hub/
├── manage.py
├── requirements.txt
├── .env.example             # Plantilla sin secretos
├── .gitignore
├── config/                  # Configuración del proyecto
└── pages/
    ├── models.py            # Category y Resource
    ├── admin.py
    ├── views.py
    ├── urls.py
    ├── tests.py
    ├── migrations/
    └── templates/pages/
```
=======
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
>>>>>>> f761b3e7de80d8f339aeb439f3fe1f998cd211cb
