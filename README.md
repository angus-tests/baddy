

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

## Testing when `DEBUG=False`

When `DEBUG=False` static files are not served correctly. To overcome this, run the app with the following command:

```bash
python manage.py runserver --insecure
```
