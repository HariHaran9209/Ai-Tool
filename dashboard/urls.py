from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='testing'),
    path('og/', og, name='og'),
    path('add_activity/', add_activity, name='add_activity'),
    path('add_title/', add_title, name='add_title'),
    path('add_section/', add_heading, name='add_section'),
]