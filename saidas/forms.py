from django import forms
from django.forms import widgets

from .models import Saida


class SaidaForm(forms.ModelForm):
    class Meta:
        model = Saida
        fields = ("produto", "quantidade")

        widgets = {
            "produto": widgets.Select(),
            "quantidade": widgets.NumberInput(attrs={"class": "input", "min": "0"}),
        }
