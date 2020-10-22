"""
WSGI config for poet_in_class project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poet_in_class.settings')

print("Creating wsgi application.")

application = get_wsgi_application()

print("WSGI application ready to go!")