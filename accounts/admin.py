from django.contrib import admin
from .models import *
# Register your models here.

def get_all_field_names(model):
    return [field.name for field in model._meta.fields]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = get_all_field_names(UserProfile)


@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = get_all_field_names(AdminProfile)


@admin.register(HRProfile)
class HRProfileAdmin(admin.ModelAdmin):
    list_display = get_all_field_names(HRProfile)

@admin.register(ManagerProfile)
class ManagerProfileAdmin(admin.ModelAdmin):
    list_display = get_all_field_names(ManagerProfile)


@admin.register(EmployeeProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = get_all_field_names(EmployeeProfile)
