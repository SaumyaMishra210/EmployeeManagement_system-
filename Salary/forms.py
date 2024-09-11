from django import forms
from .models import SalarySlip

class SalarySlipForm(forms.ModelForm):
    class Meta:
        model = SalarySlip
        fields = ['employee', 'month', 'year', 'base_salary', 'allowances', 'deductions']
        widgets = {
            'month': forms.NumberInput(attrs={'placeholder': 'Enter month (1-12)'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Enter year'}),
        }
