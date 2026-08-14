from django import forms
from .models import Transacao

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['descricao', 'valor', 'tipo', 'categoria', 'data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Salário, Aluguel'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Alimentação, Transporte'}),
        }
        labels = {  # noqa: RUF012
            'descricao': 'Descrição',
            'valor': 'Valor (R$)',
            'tipo': 'Tipo',
            'categoria': 'Categoria',
            'data': 'Data',
        }