# Jihusishe
Jihusishe is a SMS-based (text message) framework that manages data collection, complex workflows, and group coordination using basic mobile phones -- and can present information on the internet as soon as it is received.






## Features

* Create and manage multiple contact lists;
* Import lists from other providers (csv files or paste phone numbers);
* Default double opt-in for sign ups;
* Schedule sms campaign to send on a specific date and time;
* Track sms deivery


## Quickstart

If you want to have a quick look or just run the project locally, you can get started by either forking this repository
or just cloning it directly:

```commandline
git clone 
```

Ideally, create a [virtualenv](https://docs.python-guide.org/dev/virtualenvs/) and install the projects dependencies:

```commandline
pip install -r requirements/development.txt
```

Create a local database:

```commandline
python manage.py migrate
```

Start development server:

```commandline
python manage.py runserver
```

Open your browser and access the setup page to create an admin account:

```commandline
http://127.0.0.1:8000/setup/
```

PS: Campaign scheduling will not work out-of-the-box. You need to install a message broker and [setup Celery](https://simpleisbetterthancomplex.com/tutorial/2017/08/20/how-to-use-celery-with-django.html) properly.

## Tech Specs

* Python 3.6
* Django 2.1
* PostgreSQL 10
* Celery 4.2
* RabbitMQ 3.7
* Bootstrap 4 
* jQuery 3.3

PostgreSQL and RabbitMQ are soft dependencies. Other databases (supported by Django) can easily be used as well as other 
message broker compatible with Celery.

The jQuery library is more of a Bootstrap dependency. There is very little JavaScript code in the project. For the most 
part the code base is just plain Django and HTML templates. 

Complete list of Python dependencies can be found in the requirements files.

## Documentation

This is just a pre-release of the project and I still have to work on a proper documentation and user guides.

For now you will only find documentation of the internal APIs in the source code.

[

## Who's using Jihusishe?

Right now just myself Still under development 


## License

The source code is released under the [MIT License]
