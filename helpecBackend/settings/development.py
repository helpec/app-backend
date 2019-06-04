import os
from .base import *
 
DEBUG = True

ALLOWED_HOSTS += ["*"]

EMAIL_HOST = os.environ.get("EMAIL_HOST", "mailhog")