from django.urls import path
from . import views

urlpatterns = [
    path('/search/', views.attendance_search, name='attendance_search'),
    path('/AIndex/', views.attendance_view, name='attendance'),
    path('/attendanceList/', views.attendance_list, name='attendanceList'),
    path('/modify/', views.modify_attendance, name='modify_attendance'),
    path('/get_yearly_attendance_status/',views.get_yearly_attendance_status,name='get_yearly_attendance_status'),
]
