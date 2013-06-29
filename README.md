Django Template Project with Bootstrap
======================================

This is my default project starter, includes all my default apps plus bootstrap.

git clone git+https://github.com/mmcardle/django_templates

# Django 1.4
django-admin.py startproject --template=./django_templates/project_template_1.4 YOUR_APP_NAME

# Django 1.5
django-admin.py startproject --template=./django_templates/project_template_1.5 YOUR_APP_NAME

cd YOUR_APP_NAME

# Development
pip install -r ./requirements/dev.txt
# Production
pip install -r ./requirements/base.txt

cp YOUR_APP_NAME/local_settings_example.py YOUR_APP_NAME/local_settings.py
python ./manage.py syncdb
python ./manage.py migrate
python ./manage.py runserver
