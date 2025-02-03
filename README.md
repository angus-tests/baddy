
<picture style="text-align: center;">
  <source media="(prefers-color-scheme: dark)" srcset="static/images/logo.png">
  <img alt="Baddy Logo" src="static/images/logo.png" width="300">
</picture>

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

## Testing when `DEBUG=False`

When `DEBUG=False` static files are not served correctly. To overcome this, run the app with the following command:

```bash
python manage.py runserver --insecure
```
