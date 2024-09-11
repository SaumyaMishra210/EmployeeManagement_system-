# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('/request_dashboard/', views.request_dashboard, name='request_dashboard'),
    path('/request_list/', views.request_list, name='request_list'),
    path('/create/', views.create_request, name='create_request'),
    path('/edit/<int:pk>/', views.edit_request, name='edit_request'),
    path('/manage/<int:pk>/<str:action>/', views.manage_request, name='manage_request'),
    path('/request_list_HR/',views.request_list_HR,name = 'request_list_HR'),
]
