

<p style="text-align: center;"><img src="static/images/logo.png"  width="500"></p>

# Baddy

Business Analytics & Data Dashboard for You

## Installation

### Clone the repository

```bash
git clone git@github.com:angus-tests/baddy.git
```

### Install dependencies

```bash
poetry install
```

### Start Tailwind CSS

```bash
npm i
npm run watch
```

### Migrate & run the app

```bash
python manage.py migrate
python manage.py runserver
```
### Seeding groups

To seed the groups, run the following command:
```bash
python manage.py seed_groups
```

### Create a superuser

To access the admin panel, create a superuser with the following command:
```bash
python manage.py createsuperuser
```

Then login to the admin panel at http://127.0.0.1:8000/admin/

## Testing when `DEBUG=False`

When `DEBUG=False` static files are not served correctly. To overcome this, run the app with the following command:

```bash
python manage.py runserver --insecure
```

## Settings

To switch between development and production settings, set the `DJANGO_ENV` environment variable.

## Docker locally

To run the app locally with Docker, run the following command:

```bash
docker build -t baddy .
```

Then you can use the docker-compose file to run the app:

```bash
docker-compose up
```


## Deployment

When deploying the app, make sure to set the following environment variables:

| **Environment Variable** | **Description**                                                  | **Example Value**             |
|--------------------------|------------------------------------------------------------------|-------------------------------|
| `DJANGO_ENV`             | Specifies the Django environment (`production`, `development`).  | `production`                  |
| `DB_USER`                | Database username for Django to connect to the database.         | `django`                      |
| `DB_PASSWORD`            | Password for the database user.                                  | `password`                    |
| `DB_NAME`                | The name of the database Django should use.                      | `baddy`                       |
| `DB_HOST`                | Hostname or IP address of the database server.                   | `postgres`                    |
| `DB_PORT`                | Port number for connecting to the database.                      | `5432`                        |
| `DEBUG`                  | Controls Django's debug mode (`True` for dev, `False` for prod). | `True`                        |
| `SECRET_KEY`             | Secret key for cryptographic signing in Django.                  | `django-insecure-1nze18c1...` |
| `CSRF_HOSTS`             | Allowed hosts for CSRF protection.                               | `http://localhost:8000`       |
| `ADMIN_USERNAME`         | Username for the initial superuser account.                      | `admin`                       |
| `ADMIN_EMAIL`            | Email address for the initial superuser.                         | `admin@example.com`           |
| `ADMIN_PASSWORD`         | Password for the initial superuser.                              | `password`                    |

## Linting

Ensure poetry dependencies are installed ...

```
poetry install
```


To run black ...

```
poetry run black .
```

To run autoflake and remove unused imports ...

```
poetry run autoflake --remove-all-unused-imports --recursive --in-place .
```
