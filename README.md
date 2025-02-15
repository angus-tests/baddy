

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
### Seeding

To seed the groups, run the following command:
```bash
python manage.py seed_groups
```

Next we need to seed the dashboards...
```bash
python manage.py seed_dashboards
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
