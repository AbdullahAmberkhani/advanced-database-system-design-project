# myapp/urls.py
from django.urls import path
from .views import add_data, modify_data, delete_data, view_data

urlpatterns = [
    path('add/', add_data, name='add_data'),
    path('modify/<int:employee_id>/', modify_data, name='modify_data'),
    path('delete/<int:employee_id>/', delete_data, name='delete_data'),
    path('view/', view_data, name='view_data'),
]
