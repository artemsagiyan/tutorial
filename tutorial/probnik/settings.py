import os

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',

    'rest_framework',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'usersdb',
        'USER': 'kmk',
        'PASSWORD': 'cat007',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
