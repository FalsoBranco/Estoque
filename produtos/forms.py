from django import forms

from .models import Cor, Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "cor", "descricao", "preco", "quantidade"]
        labels = {"nome": "Produto"}
        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class": "input",
                    "type": "text",
                    "placeholder": "Nome do produto",
                },
            ),
            "cor": forms.Select(attrs={"class": "select"}),
            "descricao": forms.Textarea(attrs={"class": "textarea"}),
            "preco": forms.NumberInput(
                attrs={
                    "class": "input",
                    "min": "0",
                    "placeholder": "Preço do Produto",
                    "step": "0.01",
                }
            ),
            "quantidade": forms.NumberInput(attrs={"class": "input"}),
        }
