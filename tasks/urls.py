# urls.py
from django.urls import path
from .views import assign_work, task_list_employee, task_list_hr, edit_task, delete_task, mark_task_done

urlpatterns = [
    path('/assign-work/', assign_work, name='assign_work'),
    path('/tasks/', task_list_employee, name='task_list_employee'),
    path('/tasks/hr/', task_list_hr, name='task_list_hr'),
    path('tasks/edit/<int:pk>/', edit_task, name='edit_task'),
    path('tasks/delete/<int:pk>/', delete_task, name='delete_task'),
    path('tasks/done/<int:pk>/', mark_task_done, name='mark_task_done'),
]
