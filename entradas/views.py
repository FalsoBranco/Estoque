from django.forms.models import BaseModelForm
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from entradas.forms import EntradaForm
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
    template_name = "entradas/entrada_new.html"
    form_class = EntradaForm
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


class EntradaUpdateView(UpdateView):
    model = Entrada
    form_class = EntradaForm
    template_name = "entradas/entrada_update.html"
    success_url = reverse_lazy("entradas:lista_entradas")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:

        form.instance.produto.quantidade = (
            form.instance.produto.quantidade - form.initial.get("quantidade")
        ) + form.instance.quantidade
        form.instance.produto.save_base()
        return super().form_valid(form)
