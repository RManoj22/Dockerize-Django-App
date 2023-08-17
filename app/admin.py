"""
This module contains the Django admin configuration for the MyTable model.
"""

from django.contrib import admin
from .models import MyTable

admin.site.register(MyTable)
