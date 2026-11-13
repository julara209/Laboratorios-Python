# ClassroomHub

ClassroomHub es un portal de recursos de aprendizaje construido con Django (Laboratorios 6 a 9). Los recursos y las categorías se guardan en una base de datos MariaDB/MySQL. Las páginas públicas son de solo lectura, las cuentas pueden registrarse e iniciar sesión, y desde el Laboratorio 9 las personas autorizadas pueden **crear, editar y eliminar recursos desde la propia aplicación**, con un permiso distinto para cada operación.

El recorrido que practica el proyecto es **modelo → base de datos → vista → plantilla**, con cuatro niveles de acceso: visitante anónimo, cuenta autenticada, revisor (`Catalog reviewers`) y editor (`Catalog editors`).

## Requisitos

- Python 3.12 o superior (desarrollado con Python 3.15.0)
- Django 6.1.3 (versión fijada en `requirements.txt`)
- MariaDB 10.11 o superior (desarrollado con 11.4.13), o MySQL 8. Django 6.x no admite versiones anteriores de MariaDB.
- Controlador `mysqlclient` y `python-dotenv` (incluidos en `requirements.txt`)

## Instalación

1. Clona el repositorio y entra en la carpeta del proyecto:

   ```bash
   git clone https://github.com/julara209/Laboratorios-Python.git
   cd Laboratorios-Python/laboratorio-06-07-08-09/classroom-hub
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

## Migraciones y superusuario

```bash
python manage.py migrate
python manage.py createsuperuser
```

El CRUD de recursos usa las tablas que ya existen: el Laboratorio 9 no añade modelos ni migraciones. Los archivos de `pages/migrations/` se versionan; el contenido de la base no.

## Datos de ejemplo

Las categorías se gestionan solo desde Django Admin (`/admin/`). Antes de crear recursos, crea al menos una categoría en **Pages > Categories**, porque el formulario de recursos ofrece únicamente las categorías existentes.

## Ejecución

```bash
python manage.py check
python manage.py runserver
```

| Ruta | Método | Acceso | Descripción |
|---|---|---|---|
| `/` | GET | Público | Página principal |
| `/resources/` | GET | Público | Catálogo guardado en la base, con enlace al detalle |
| `/resources/<pk>/` | GET | Público | Detalle de un recurso (404 si no existe) |
| `/resources/available/` | GET | Público | Solo recursos disponibles (solo lectura) |
| `/about/` | GET | Público | Propósito del proyecto |
| `/resources/new/` | GET, POST | `pages.add_resource` | Crear un recurso |
| `/resources/<pk>/edit/` | GET, POST | `pages.change_resource` | Editar un recurso existente |
| `/resources/<pk>/delete/` | GET, POST | `pages.delete_resource` | GET muestra la confirmación; POST elimina |
| `/resources/review/` | GET | `pages.view_resource` | Revisión de solo lectura del catálogo |
| `/accounts/signup/` | GET, POST | Público | Registro de cuentas comunes |
| `/accounts/login/` | GET, POST | Público | Inicio de sesión |
| `/accounts/logout/` | POST | Autenticado | Cierre de sesión; un GET responde `405` |
| `/dashboard/` | GET | Autenticado | Panel privado con contador en la sesión |
| `/admin/` | — | Personal (`is_staff`) | Django Admin: categorías, recursos, usuarios y grupos |

Sin sesión, las rutas protegidas redirigen al login; con sesión pero sin el permiso correspondiente responden `403`.

## Grupos y permisos

Los permisos **no** se asignan desde el registro público: `/accounts/signup/` crea cuentas sin grupos ni privilegios. Los asigna una persona administradora.

| Grupo | Permisos | Qué puede hacer |
|---|---|---|
| `Catalog reviewers` | `view_resource` | Abrir `/resources/review/` (solo lectura) |
| `Catalog editors` | `view_resource`, `add_resource`, `change_resource`, `delete_resource` | Revisar, crear, editar y eliminar recursos |

Ninguno de los dos grupos concede `is_staff`: las vistas dependen de permisos, no de ser administrador.

### Crear el grupo de editores desde Django Admin

1. Entra en `/admin/` con el superusuario.
2. En **Groups**, crea `Catalog editors` y añade los cuatro permisos `pages | resource | Can view / add / change / delete resource`.
3. En **Users**, abre una cuenta de demostración y agrégala al grupo. No marques *Staff status* ni *Superuser status*.

### Crear el grupo de editores desde el shell

```bash
python manage.py shell
```

```python
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from pages.models import Resource

content_type = ContentType.objects.get_for_model(Resource)
codes = ["view_resource", "add_resource", "change_resource", "delete_resource"]
permissions = list(Permission.objects.filter(content_type=content_type, codename__in=codes))

if len(permissions) != len(codes):
    raise RuntimeError("Expected resource permissions were not found")

editors, _ = Group.objects.get_or_create(name="Catalog editors")
editors.permissions.add(*permissions)

User = get_user_model()
account = User.objects.get(username="NOMBRE_DE_USUARIO")
account.groups.add(editors)

# Vuelve a leer el usuario: Django guarda los permisos en caché en cada instancia
account = User.objects.get(pk=account.pk)
print(account.has_perm("pages.change_resource"))   # True
```

El grupo `Catalog reviewers` se crea igual, con el permiso `view_resource` únicamente.

Un superusuario siempre tiene todos los permisos, por lo que no sirve para comprobar un `403`: usa cuentas comunes o de grupo.

## Pruebas

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test pages
```

Las pruebas usan una base descartable (`test_classroom_hub`) que Django crea y elimina, sin tocar los datos reales. Son **60 pruebas**: 12 del Laboratorio 7 (páginas, lectura desde la base, relación con la categoría, protección `PROTECT` y `/resources/available/`), 18 del Laboratorio 8 (registro, login, logout por POST, CSRF, sesiones y revisión) y 30 del Laboratorio 9 (`ResourceCrudTests`: detalle, creación, edición, eliminación, validación, permisos, 404 y CSRF).

## Seguridad

- Cada operación del CRUD comprueba su permiso en el servidor; ocultar un enlace en la plantilla no sustituye esa comprobación.
- Los formularios incluyen `{% csrf_token %}` y no se usa `csrf_exempt`.
- La eliminación requiere una confirmación y un `POST`; un `GET` nunca borra datos.
- `ResourceForm` declara los campos editables de forma explícita (`title`, `description`, `resource_type`, `category`, `available`).
- Credenciales, `.env` y cookies de sesión no se versionan.

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
    ├── forms.py             # ResourceForm (ModelForm)
    ├── admin.py
    ├── views.py             # Páginas públicas, cuentas, panel, revisión y CRUD de recursos
    ├── urls.py              # app_name = "pages"
    ├── tests.py
    ├── migrations/
    └── templates/pages/     # base, home, resources, resource_detail, resource_form,
                             # resource_confirm_delete, about, signup, login, dashboard, review
```
