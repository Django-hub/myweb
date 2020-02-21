"""
WSGI config for website2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
path='/home/sure123/website2'
if path not in sys.path:
    sys.path.insert(0,path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website2/website2.settings')

application = get_wsgi_application()


"""
import os
import sys

path='/home/sure123/website2'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website2.settings')

#application = get_wsgi_application()
application = StaticFilesHandler(get_wsgi_application()) """


