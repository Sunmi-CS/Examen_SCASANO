from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'publicacion', 'genero']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input'}),
            'publicacion': forms.Select(attrs={'class': 'input'}),
            'genero': forms.TextInput(attrs={'class': 'input'}),
        }

        