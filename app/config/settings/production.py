from .base import *
from .base import env_var

DEBUG = False

SECRET_KEY = env_var("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = [env_var("DJANGO_ALLOWED_HOSTS")]

ADMIN_URL = env_var("DJANGO_ADMIN_URL")
