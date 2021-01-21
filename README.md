# Diary_Management

<h2> Steps to use this repo </h2>
<ol>
  <li>Clone</li>
  <li>Make migration</li>
  <li>Runserver</li>
</ol>

<h2> Important Django commands and files </h2>
<h4> Creating Django project: <i>django-admin startproject diary </i></h4>
<h4> Checking Migration : <i>python manage.py makemigrations </i></h4>
<h4> Making Migration to create database : <i>python manage.py migrate </i></h4>
<h4> Runnung app : <i>python manage.py runserver </i></h4>
<h4> Creating admin user : <i>python manage.py createsuperuser </i></h4>


<h4>models.py: to create a class model that directly creates database queries</h4>
<h4>views.py: store business logic in form of python functions</h4>
<h4>urls.py: store path of functions present in views.py</h4>
<h4>templates: stores frontend logic, uses jinja tags to communicate with backend</h4>
