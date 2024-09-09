# forms.py
from django import forms
from .models import TechnicalProfile

class TechnicalProfileForm(forms.ModelForm):
    class Meta:
        model = TechnicalProfile
        fields = [
            'position', 'experience_years', 'bio', 'profile_picture',
            'skills_name', 'project_name', 'project_description', 'technologies_used',
            'certificate_name', 'issuing_organization'
        ]
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'technologies_used': forms.Textarea(attrs={'rows': 2}),
        }
