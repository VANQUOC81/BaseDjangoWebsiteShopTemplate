# Base Django Website Shop Template
This repository contains a base Django website template that can be used to quickly kickstart your own projects. The template comes with basic functionality and structure, including user authentication, database models, and templates.

## Installation
To use this template, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running pip install -r requirements.txt.
3. Create a new Django project using the command django-admin startproject projectname.
4. Copy the contents of the django-template directory to the new project's root directory.
5. Update the settings.py file with your own settings, including database configuration and secret key.
6. Run the command python manage.py migrate to apply the database migrations.
7. Create a superuser account by running python manage.py createsuperuser.
8. Start the development server using python manage.py runserver.

You should now have a working Django website template that you can customize to fit your needs.

## Features
The template comes with the following features:

* Admin user authentication and login/logout functionality.
* Bootstrap components like NavBar, Cards, etc. 
* Basic database models for users, products and offers.
* Basic templates for the home page, admin login page, and products admin list/detail pages.

## Usage
To use this template, simply modify the existing code to fit your needs. Add new database models, modify existing templates, or add new functionality to the views. This template is meant to serve as a starting point for your own Django projects, so feel free to make any changes you like.

## Contributing
Contributions to this repository are welcome. If you find any bugs or have suggestions for new features, please open an issue on the repository or submit a pull request.

## License
This Django website template is licensed under the MIT License. Feel free to use it for your own projects or modify it to fit your needs.


## Django commands

### Install Django
pip install django

### Apps within Django 
In Django, an app is a web application that does something - e.g. a blog system, a database of public records, or a small poll app. An app can be used in multiple projects, and a project can contain multiple apps. An app is essentially a module that contains models, views, templates, and other components that provide a specific functionality. Django apps are designed to be reusable and can be easily plugged into any Django project. Apps are stored in a directory and can be created using the **'startapp'** management command.

### Django manage.py file
In Django, python manage.py is a command-line utility used to interact with a Django project. It is used to perform a variety of tasks, such as:

* Creating a new Django project: python manage.py startproject project_name
* Running the development server: python manage.py runserver
* Creating a new app within a Django project: python manage.py startapp app_name
* Creating database tables: python manage.py migrate
* Creating a new superuser: python manage.py createsuperuser
* Running tests: python manage.py test
* Generating database schema: python manage.py makemigrations

Essentially, python manage.py serves as a tool to execute various Django commands and manage a Django project.
