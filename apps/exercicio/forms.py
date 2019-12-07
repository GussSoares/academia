from django import forms

from ..exercicio.models import Exercicio


class ExercicioForm(forms.ModelForm):
    class Meta:
        model = Exercicio
        fields = ['nome', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            })
        }