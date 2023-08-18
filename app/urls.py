"""
This code is defining the URL patterns for a Django web application.
"""

from django.urls import path
from app import views

urlpatterns = [
    path('',views.details,name='details'),
    path('add/',views.addnew,name='add'),
    path('edit/<int:req_id>',views.edit,name='edit'),
    path('delete/<int:req_id>',views.delete,name='delete'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('export/',views.export_excel,name='export'),
]
