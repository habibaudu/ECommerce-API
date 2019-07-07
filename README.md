# ECommerce-API
This is an ecommerce API, That operates accordinglys :)

## Installing

```sh
    $ git clone https://github.com/habibaudu/ECommerce-API.git
    $ cd ECommerce-API
    $ pip install virtualenv
    $ virtualenv venv
    $ source venv/bin/activate
    $ git checkout dev
    $ pip install -r requirements.txt
```

* Create a `.env` file and copy/paste the environment variables from the `.env_example` file that's already existent in the root project directory.
* Create a postgreSQL database called `ecommerceapi` using the default `postgres` user and change the value of variable `DB_PASSWORD` in your `.env` file to your `postgres` user's password.
* Run the following commands to make the database migrations.

```sh
    $ python manage.py makemigrations
    $ python manage.py migrate
```

## Running the application

Run the command below to run the application locally.
```sh
  $ python manage.py runserver
  ```



## Built With

The project has been built with the following technologies so far:

* [Django](https://www.djangoproject.com/) - web framework for building websites using Python
* [Django-rest-framework](https://www.django-rest-framework.org/) - To creat rest APIs.
* [Virtual environment](https://virtualenv.pypa.io/en/stable/) - tool used to create isolated python environments
* [pip](https://pip.pypa.io/en/stable/) - package installer for Python
* [PostgreSQL](https://www.postgresql.org/) - database management system used to persists the application's data.