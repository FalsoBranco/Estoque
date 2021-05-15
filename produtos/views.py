from typing import Any, Dict

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from produtos.forms import ProdutoForm
from produtos.models import Produto

# Create your views here.


class ProdutosView(TemplateView):
    template_name = "produtos/index.html"


class ProdutosListView(ListView):
    model = Produto
    template_name = "produtos/produtos_list.html"
    context_object_name = "produtos"


class ProdutoCreateView(CreateView):
    model = Produto
    template_name = "produtos/produto_new.html"
    form_class = ProdutoForm
    success_url = reverse_lazy("produtos:lista_produtos")


# * Deleta produto sem presisar de comfirmação
class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy("produtos:lista_produtos")

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = "produtos/produto_update.html"
    form_class = ProdutoForm
    success_url = reverse_lazy("produtos:lista_produtos")

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context["produto"] = self.object
    #     return context
