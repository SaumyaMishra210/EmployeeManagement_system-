from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_salary_slip, name='generate_salary_slip'),
    path('list/', views.salary_slip_list, name='salary_slip_list'),
    path('download/<int:pk>/', views.download_salary_slip, name='download_salary_slip'),
    path('generate-pdf/<int:slip_id>/', views.generate_salary_slip_pdf, name='generate_salary_slip_pdf'),
    # path('pdf/', views.pdf_view, name='pdf_view'),
]
