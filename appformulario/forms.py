from django import forms
from django.forms import TextInput
from .models import FormularioConcurso

class TuFormulario(forms.ModelForm):
    class Meta:
        model = FormularioConcurso
        fields = '__all__'
        labels = {
            'nombres': '',
            'apellidos': '',
            'ci': '',
            'telefono': '',
            'correo': '',
            'nrocomprobante': '',
            'imagen': ''
        }
        

        widgets = {
            'nombres': TextInput(attrs={'placeholder': 'Nombres:'}),
            'apellidos': TextInput(attrs={'placeholder': 'Apellidos:'}),
            'ci': TextInput(attrs={'placeholder': 'C.I:'}),
            #'telefono': TextInput(attrs={'placeholder': 'Teléfono:'}),
            'telefono': forms.TextInput(attrs={'type': 'tel', 'placeholder': 'Teléfono:'}),
            'correo': TextInput(attrs={'placeholder': 'Correo:'}),
            'nrocomprobante': TextInput(attrs={'type': 'tel', 'placeholder': 'Número de comprobante:'}),
            
        }

