from django import forms
from . models import libros

class FormLibro(forms.ModelForm):
    class Meta:
        model = libros
        fields = ['name', 'description', 'year', 'img']
