from django.urls import path
from . import views

urlpatterns = [
    path('base_temp',views.base,name = 'base_temp'),
    path('', views.home, name='home'),
    path('recordNotFound/',views.recordNotFound,name='recordNotFound'),
]
