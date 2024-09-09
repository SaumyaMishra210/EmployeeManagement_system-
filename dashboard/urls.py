from django.urls import path
from . import views

urlpatterns = [
    # path('/index/', views.index, name='index'),
    path('/user/details/', views.user_details_view, name='user_details_view'),
    path('user/details/edit/', views.user_details_edit_self, name='user_details_edit_self'),
    path('user/details/list/', views.user_details_list, name='user_details_list'),
    path('user/details/create/', views.user_details_create, name='user_details_create'),
    path('user/details/edit/<int:pk>/', views.user_details_edit, name='user_details_edit'),
    path('user/details/delete/<int:pk>/', views.user_details_delete, name='user_details_delete'),
]

