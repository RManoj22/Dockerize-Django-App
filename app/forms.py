"""
This module is used to define forms for the app.
"""

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import MyTable


class LoginForm(forms.Form):
    """
    The LoginForm class is a form used for user login.
    """
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    """
    The class `SignUpForm` is a subclass of `UserCreationForm` for creating user sign up forms.
    """
    class Meta:
        """
        The above code snippet defines a class named "Meta".
        """
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        }


class MyTableForm(forms.ModelForm):
    """
    The class MyTableForm is a subclass of forms.ModelForm in Python.
    """
    class Meta:
        """
        The code snippet defines a class named "Meta".
        """
        model = MyTable
        fields = ['client_name', 'contact_number', 'vendor_name', 'vendor_company',
                  'rate', 'currency', 'contract_type', 'status', 'comments']
        exclude = ['user']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Client Name'}),
            'contact_number': forms.TextInput(attrs={'id': 'contactForm',
                                                     'class': 'form-control',
                                                     'placeholder': 'Contact Number'}),
            'vendor_name': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Vendor Name'}),
            'vendor_company': forms.TextInput(attrs={'class': 'form-control',
                                                     'placeholder': 'Vendor Company'}),
            'rate': forms.NumberInput(attrs={'class': 'form-control',
                                             'placeholder': 'Rate'}),
            'currency': forms.Select(
                choices=MyTable.currency_choices,
                attrs={'class': 'form-control', 'placeholder': 'Currency'}
            ),
            'contract_type': forms.Select(choices=MyTable.contract_choices, 
                                          attrs={'class': 'form-control', 
                                                 'placeholder': 'Contract Type'}),
            'status': forms.Select(choices=MyTable.status_choices, 
                                   attrs={'class': 'form-control', 
                                          'placeholder': 'Status'}),
            'comments': forms.TextInput(attrs={'class': 'form-control', 
                                               'placeholder': 'Comments'}),
        }
