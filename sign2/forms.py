from django import forms

from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post2
        fields = ['title', 'text']
