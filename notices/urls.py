from django.urls import path
from . import views

urlpatterns = [
    path('/notice_list/', views.notice_list_view, name='notice_list'),  # View for listing notices
    path('/notice-index/', views.notice_index, name='notice_index'),
    path('/create/', views.create_notice, name='create_notice'),
    path('/delete-notice/<int:notice_id>/', views.delete_notice, name='delete_notice'),
    path('/edit-notice/<int:notice_id>/', views.edit_notice, name='edit_notice'),
]
