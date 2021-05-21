from django import forms
from django.forms import widgets

from .models import Entrada


class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ["produto", "preco", "quantidade"]

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
