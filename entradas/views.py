from typing import Any, Dict

from django.forms.models import BaseModelForm
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from entradas.models import Entrada

# Create your views here.


class EntradaView(TemplateView):
    template_name = "entradas/index.html"


class EntradaListView(ListView):
    model = Entrada
    template_name = "entradas/entradas_list.html"
    context_object_name = "entradas"
    paginate_by = 10


# ! TODO Procurar formas melhores de fazer esse update no foreing key
class EntradaCreateView(CreateView):
    model = Entrada
    template_name = "entradas/entradas_new.html"
    fields = ["produto", "preco", "quantidade"]
    success_url = reverse_lazy("entradas:lista_entradas")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.produto.quantidade += form.instance.quantidade
        form.instance.produto.save_base()
        return super(EntradaCreateView, self).form_valid(form)


# ! TODO Procurar formas melhores de fazer esse update no foreing key
class EntradaDeleteView(DeleteView):
    model = Entrada
    success_url = reverse_lazy("entradas:lista_entradas")

    def get(self, *args, **kwargs):
        entrada = Entrada.objects.get(pk=self.kwargs.get("pk"))
        entrada.produto.quantidade -= entrada.quantidade
        entrada.produto.save_base()
        return self.post(*args, **kwargs)


# ? TODO FAZER O UPDATE
# ? PEGAR A QUANTIDADE TOTAL DOS PRODUTO
# ? SUBTRAIR DA ENTRADA ANTIGA
# ? ADICIONAR A ENTRADA NOVA
class EntradaUpdateView(UpdateView):
    model = Entrada
    fields = ["produto", "preco", "quantidade"]
    template_name = "entradas/entrada_update.html"
    success_url = reverse_lazy("entradas:lista_entradas")
