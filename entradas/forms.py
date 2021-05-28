from django import forms
from django.forms import widgets

from .models import Entrada


class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ["produto", "preco", "quantidade"]
        help_texts = {
            "produto": "Escolha o produto de entrada",
            "preco": "Preço da nota de entrada",
            "quantidade": "Quantidade da entrada",
        }
        widgets = {
            "produto": widgets.Select(),
            "preco": widgets.NumberInput(
                attrs={
                    "class": "input",
                    "min": "0",
                    "placeholder": "Preço do produto",
                    "step": "0.01",
                }
            ),
            "quantidade": widgets.NumberInput(attrs={"class": "input"}),
        }
