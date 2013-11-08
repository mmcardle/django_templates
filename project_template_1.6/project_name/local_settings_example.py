DEBUG = True
DJANGO_STATIC = not DEBUG

DEBUG_APPS = ("debug_toolbar",)

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': '{{ project_name }}.sqlite3',
    }
}
