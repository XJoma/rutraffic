from django import forms

from fee.models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ['title', 'text']
