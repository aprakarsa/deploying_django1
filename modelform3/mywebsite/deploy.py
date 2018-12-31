"""
WSGI config for mywebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

from whitenoise.django import DjangoWhiteNoise


path = "/home/aprakarsa1/deploying_django1/modelform3/"
if path not in sys.path:
	sys.path.append(path)

os.environ["SECRET_KEY"] = "syla2@)%z&w4tt*+lq$t207=9)k%3z3-i5k)6ly%^$4lr!=x-m"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mywebsite.deploy_settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
