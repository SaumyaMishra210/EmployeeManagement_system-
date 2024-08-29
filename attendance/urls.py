from django.urls import path
from . import views

urlpatterns = [
    path('/AIndex/', views.attendance_view, name='attendance'),
    # path('attendanceList/', views.attendance_view, name='attendanceList'),
    path('attendance/edit/<str:pk>/', views.edit_attendance_view, name='edit_attendance'),

]
