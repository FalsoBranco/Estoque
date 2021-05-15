from django import forms

from .models import Cor, Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "cor", "descricao", "preco", "quantidade"]
