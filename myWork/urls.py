# urls.py
from django.urls import path
from .views import technical_profile_view, technical_profile_edit, employee_details_list

urlpatterns = [
    path('technical/profile/', technical_profile_view, name='technical_profile_view'),
    path('technical-profile/edit/<int:id>/', technical_profile_edit, name='technical_profile_edit'),
    path('employees/', employee_details_list, name='employee_details_list'),
]
