from .base import *

SECRET_KEY = "verysecret"


DJANGO_ENV="production"


ALLOWED_HOSTS = ['*']


DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': "postgres" ,
       'USER': "admin_agathe" ,
       'PASSWORD': "Maison1234" ,
       'HOST': "djangopostgrebecquart.postgres.database.azure.com",
       'PORT': '5432',
       'OPTIONS': {
           'sslmode': 'require',
       },
   }
}
