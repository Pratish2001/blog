from django import forms
from .models import Blogsite

class Blogsite_form(forms.ModelForm):
    class Meta:
        model = Blogsite
        fields ="__all__"