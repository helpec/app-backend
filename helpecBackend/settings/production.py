"""  """
import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DATABASE_NAME", "helpec"),
        "USER": os.getenv("DATABASE_USER", "root"),	
        "PASSWORD": os.getenv("DATABASE_PASSWORD", "root"),
        "HOST": os.getenv("DATABASE_HOST", "127.0.0.1"),	
        "PORT": os.getenv("DATABASE_PORT", 3306),
    }
}



# sentry_sdk.init(
#     dsn=os.getenv("SENTRY_DJANGO_DSN"),
#     integrations=[DjangoIntegration()]
# )


EMAIL_HOST = "email-smtp.us-east-1.amazonaws.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True

