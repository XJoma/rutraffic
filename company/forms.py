from django import forms

from company.models import *

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['title', 'text']
