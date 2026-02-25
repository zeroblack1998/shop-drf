# Django REST Shop API

A minimal Django REST Framework project providing APIs for product management and user handling. Designed for learning, testing, and extending into a production-ready backend.

## Features

* Product CRUD API
* User model & endpoints
* SQLite database (default)
* Django REST Framework serializers & views
* Modular apps: `shop` and `users`

## Project Structure

```
drf/            # Django project settings
shop/           # Product API app
users/          # User API app
manage.py
requirements.txt
db.sqlite3
```

## Requirements

* Python 3.10+
* pip
* virtualenv (recommended)
* BSD / Linux / macOS supported

## Installation

### 1. Clone or extract

```sh
unzip shop-drf.zip
cd drf
```

### 2. Create virtual environment

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

## Database Setup

```sh
python manage.py migrate
```

(Optional) create admin user:

```sh
python manage.py createsuperuser
```

## Run Development Server

```sh
python manage.py runserver
```

Server:

```
http://127.0.0.1:8000/
```

## API Endpoints

### Products

```
GET     /products/
POST    /products/
GET     /products/<id>/
```

### Users

```
GET     /users/
POST    /users/
GET     /users/<id>/
```

## Example Request

Create product:

```bash
curl -X POST http://127.0.0.1:8000/products/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Laptop","price":1200,"stack":10}'
```

## Development Notes

* Uses SQLite by default (`db.sqlite3`)
* Edit models in `shop/models.py` and `users/models.py`
* Run migrations after model changes:

```sh
python manage.py makemigrations
python manage.py migrate
```

## Running on BSD (GhostBSD / FreeBSD)

Install Python and pip:

```sh
pkg install python py39-pip
```

Then follow installation steps normally.

## Future Improvements

* JWT Authentication
* Permissions & roles
* Pagination & filtering
* PostgreSQL support
* Docker deployment
