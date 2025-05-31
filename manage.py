#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


# import os
# from django.core.wsgi import get_wsgi_application
# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Todo_App.settings')

# # Add this line to expose the app
# app = get_wsgi_application()  # for WSGI
# # or
# app = get_asgi_application()  # for ASGI if using Django channels


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Todo_App.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
