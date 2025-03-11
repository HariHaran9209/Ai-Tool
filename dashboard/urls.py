from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='testing'),
    path('main/', og, name='og'),
    path('add-activity/', add_activity, name='add_activity'),
    path('add-title/', add_title, name='add_title'),
    path('add-section/', add_heading, name='add_section'),
    path('delete/titles/<int:record_id>/', delete_titles, name='delete_titles'),
    path('delete/headings/<int:record_id>/', delete_headings, name='delete_headings'),
    path('delete/activities/<int:record_id>/', delete_activities, name='delete_activities'),
    path('delete/records/', delete_records, name='delete_records'),
]
