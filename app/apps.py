"""
Django AppConfig for the 'app' app.
"""

from django.apps import AppConfig


class AppNameConfig(AppConfig):
    """
    Configuration class for the 'app' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
