from django import forms
from .models import Carro

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['marca', 'modelo', 'ano', 'preco', 'quilometragem', 'combustivel', 'cor', 'descricao', 'imagem']
        widgets = {
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'quilometragem': forms.NumberInput(attrs={'class': 'form-control'}),
            'combustivel': forms.Select(attrs={'class': 'form-control'}),
            'cor': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
        } 