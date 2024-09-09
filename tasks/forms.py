from django import forms
from django.contrib.auth.models import User

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',  # HTML5 input type for date and time
                'class': 'form-control',
                'placeholder': 'Select due date and time'
            }),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        # Limit the assigned_to field to only show users in the Employee group
        self.fields['assigned_to'].queryset = User.objects.filter(groups__name='Employee')