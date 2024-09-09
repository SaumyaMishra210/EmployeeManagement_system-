"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Base import views
from django.urls import include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from Base.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("Base.urls")),
    path('attendance',include('attendance.urls')),
    path('dashboard',include('dashboard.urls')),
    path('accounts', include('accounts.urls')),
    path('myWork',include('myWork.urls')),
    path('notices',include('notices.urls')),
    path('requests',include('requests.urls')),
    path('tasks',include('tasks.urls')),
]
# for Media Storage
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
