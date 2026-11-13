# ClassroomHub

ClassroomHub es un portal de recursos de aprendizaje construido con Django (Laboratorios 6, 7 y 8). Los recursos y las categorías se guardan en una base de datos MariaDB/MySQL, se administran desde Django Admin y se muestran en páginas públicas de solo lectura. Desde el Laboratorio 8 la aplicación también tiene **registro de cuentas, inicio y cierre de sesión, un panel privado y una página de revisión restringida por permisos**.

El recorrido que practica el proyecto es **modelo → base de datos → vista → plantilla**, ahora con tres niveles de acceso: visitante anónimo, usuario autenticado y usuario autorizado.

## Requisitos

- Python 3.12 o superior (desarrollado con Python 3.15.0)
- Django 6.1.3 (versión fijada en `requirements.txt`)
- MariaDB 10.11 o superior (desarrollado con 11.4.13), o MySQL 8. Django 6.x no admite versiones anteriores de MariaDB.
- Controlador `mysqlclient` y `python-dotenv` (incluidos en `requirements.txt`)

## Instalación

1. Clona el repositorio y entra en la carpeta del proyecto:

   ```bash
   git clone https://github.com/julara209/Laboratorios-Python.git
   cd Laboratorios-Python/laboratorio-08/classroom-hub
   ```

2. Crea y activa el entorno virtual:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate          # Windows (CMD)
   # source .venv/bin/activate     # Linux / macOS
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

Variables: `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`. El archivo `.env` contiene secretos y **no se versiona**. Nunca subas contraseñas reales, cookies de sesión ni exportaciones de la base con datos privados.

## Conexión

`config/settings.py` usa el backend `django.db.backends.mysql` (válido tanto para MySQL como para MariaDB) con el controlador `mysqlclient`, y lee los datos de conexión desde `.env`.

## Migraciones y superusuario

```bash
python manage.py migrate
python manage.py createsuperuser
```

`migrate` también crea las tablas de cuentas, grupos, permisos y sesiones de Django (`auth_*` y `django_session`). Los archivos de migración (`pages/migrations/`) sí se versionan; el contenido de la base no.

## Ejecución

```bash
python manage.py check
python manage.py runserver
```

| Ruta | Acceso | Descripción |
|---|---|---|
| `/` | Público | Página principal |
| `/resources/` | Público | Recursos guardados en la base, con su categoría |
| `/resources/available/` | Público | Solo recursos disponibles (solo lectura) |
| `/about/` | Público | Propósito del proyecto |
| `/accounts/signup/` | Público | Registro de cuentas comunes |
| `/accounts/login/` | Público | Inicio de sesión (`LoginView`) |
| `/accounts/logout/` | Solo POST | Cierre de sesión (`LogoutView`); un GET responde `405` |
| `/dashboard/` | Autenticado | Panel privado con un contador guardado en la sesión |
| `/resources/review/` | Permiso `pages.view_resource` | Revisión del catálogo; sin sesión redirige al login y sin permiso responde `403` |
| `/admin/` | Personal (`is_staff`) | Django Admin para mantener categorías, recursos, usuarios y grupos |

Cualquier otra dirección responde con `404`.

## Cuentas, grupos y permisos

- **Registro:** `/accounts/signup/` usa `UserCreationForm` y crea cuentas comunes, sin `is_staff` ni `is_superuser`. Después de registrarse hay que iniciar sesión.
- **Cierre de sesión:** se hace con un formulario `POST` con `{% csrf_token %}` (botón *Log out* del menú), no con un enlace.
- **Grupo revisor:** `/resources/review/` solo la ven las cuentas con el permiso `pages.view_resource`. Para otorgarlo, crea el grupo **Catalog reviewers**.

### Crear el grupo desde Django Admin

1. Entra en `/admin/` con el superusuario.
2. En **Groups**, crea `Catalog reviewers` y añade el permiso `pages | resource | Can view resource`.
3. En **Users**, abre la cuenta que será revisora y agrégala al grupo. No marques *Staff status* ni *Superuser status*: no hacen falta.

### Crear el grupo desde el shell

```bash
python manage.py shell
```

```python
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from pages.models import Resource

content_type = ContentType.objects.get_for_model(Resource)
view_permission = Permission.objects.get(content_type=content_type, codename="view_resource")

reviewers, _ = Group.objects.get_or_create(name="Catalog reviewers")
reviewers.permissions.add(view_permission)

User = get_user_model()
account = User.objects.get(username="NOMBRE_DE_USUARIO")
account.groups.add(reviewers)

# Vuelve a leer el usuario: Django guarda los permisos en caché en cada instancia
account = User.objects.get(pk=account.pk)
print(account.has_perm("pages.view_resource"))   # True
```

Un superusuario siempre tiene todos los permisos, por lo que no sirve para comprobar el `403`: usa una cuenta común.

## Pruebas

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test pages
```

Las pruebas usan una base descartable (`test_classroom_hub`) que Django crea y elimina, sin tocar los datos reales. Son **30 pruebas**: las 12 del Laboratorio 7 (páginas, lectura desde la base, relación con la categoría, protección `PROTECT` y ruta de recursos disponibles) y 18 del Laboratorio 8 que verifican registro, login, logout por POST, protección CSRF, sesión, redirecciones y los accesos `302`, `403` y `200` de `/resources/review/`.

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
    ├── views.py             # Páginas públicas, signup, dashboard y resource_review
    ├── urls.py              # app_name = "pages"
    ├── tests.py
    ├── migrations/
    └── templates/pages/     # base, home, resources, about, signup, login, dashboard, review
```
