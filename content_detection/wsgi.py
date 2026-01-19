"""
WSGI config for content_detection project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'content_detection.settings')

application = get_wsgi_application()
