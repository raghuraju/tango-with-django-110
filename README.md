# tango-with-django-110

Companion repository for the book tango-with-django adopted to django 1.10.1

## Installation instructions

Create a directory to house the project and move into it
```
$ mkdir tangowithdjango && cd tangowithdjango
```

Create a new virtual environment to install dependencies and activate it
```
$ virtualenv .
$ . bin/activate
```

Clone the repository
```
$ git clone https://github.com/raghuraju/tango-with-django-110.git
$ mv tango-with-django src
$ cd src
```
Install requirements
```
$ pip install -r requirements/base.txt
```

Create database (this repo uses PostgreSQL), user and define the following environment variables
```
$ DB_NAME
$ DB_USER
$ DB_PASSWORD
$ DB_HOST
$ DB_PORT
```

Apply migrations
```
$ python manage.py migrate --settings=tango_with_django.settings.base
```

Run populate_rango.py to load some data into the database
```
$ python populate_rango.py
```

Create a super user
```
$ python manage.py createsuperuser --settings=tango_with_django.settings.base
```

Run server
```	
$ python manage.py runserver --settings=tango_with_django.settings.base
```
