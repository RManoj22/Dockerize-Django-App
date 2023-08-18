"""
This module is used to apply filters on the models.
"""

import django_filters
from app.models import MyTable


class FormFilter(django_filters.FilterSet):
    """
    The `FormFilter` class is a Django filter class that
    filters instances of the `MyTable` model based
    on the `status`, `currency`, and `user` fields.
    """
    class Meta:
        """
        The code snippet defines a class named "Meta".
        """
        model = MyTable
        fields = ['status', 'currency', 'user']
