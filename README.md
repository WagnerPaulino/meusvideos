# meusvideos

## Run
```
$ cd meusvideos-service
$ python3.7 -m venv venv
$ . venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## Used frameworks
* Django
* Django Rest Framework

## How to use

* Registration
```bash
curl --location --request POST 'http://127.0.0.1:8000/dj-rest-auth/registration/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "admin",
    "password1": "admin",
    "password2": "admin",
    "email": "admin@teste.com"
}'
```

* Login
```bash
curl --location --request POST 'http://127.0.0.1:8000/dj-rest-auth/login/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"admin",
    "password":"admin"
}'
```

* Request to some protected endpoint
```
curl --location --request GET 'http://127.0.0.1:8000/videos' \
--header 'Authorization: Bearer <token>'
```
