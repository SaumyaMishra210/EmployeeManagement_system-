# forms.py
from django import forms
from .models import Request_app_model

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request_app_model
        fields = ['title', 'description']
