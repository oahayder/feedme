"""
WSGI config for feedme project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

pwd = os.path.dirname(os.path.abspath(__file__))
sys.path += [pwd]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "feedme.settings")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())

