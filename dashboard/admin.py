from django.contrib import admin
from dashboard.models import *
# Register your models here.
def get_all_field_names(model):
    return [field.name for field in model._meta.fields]


@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = get_all_field_names(UserDetails)
