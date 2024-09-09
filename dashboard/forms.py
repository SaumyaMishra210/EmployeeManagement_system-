from django import forms
from .models import UserDetails

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['first_name', 'middle_name', 'last_name', 'phone_number', 'email', 'dob', 'aadhar_number', 'designation', 'salary']
