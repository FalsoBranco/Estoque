# from django.shortcuts import render
from typing import Any, Dict

from django.forms.models import BaseModelForm
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from produtos.models import Produto

from saidas.forms import SaidaForm
from saidas.models import Saida

# Create your views here.


class SaidaView(TemplateView):
    template_name = "saidas/index.html"


class SaidaListView(ListView):
    model = Saida
    template_name = "saidas/saidas_list.html"
    context_object_name = "saidas"
    paginate_by = 10


class SaidaCreateView(CreateView):
    model = Saida
    template_name = "saidas/saida_new.html"
    form_class = SaidaForm
    success_url = reverse_lazy("saidas:lista_saidas")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.produto.quantidade -= form.instance.quantidade
        form.instance.preco = form.instance.produto.preco
        form.instance.produto.save()
        return super().form_valid(form)


# ! TODO Procurar formas melhores de fazer esse update no foreing key
class SaidaDeleteView(DeleteView):
    model = Saida
    success_url = reverse_lazy("saidas:lista_saidas")

    def get(self, *args, **kwargs):
        saida = Saida.objects.get(pk=self.kwargs.get("pk"))
        saida.produto.quantidade += saida.quantidade
        saida.produto.save_base()
        return self.post(*args, **kwargs)


class SaidaUpdateView(UpdateView):
    model = Saida
    form_class = SaidaForm
    template_name = "saidas/saida_update.html"
    success_url = reverse_lazy("saidas:lista_saidas")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:

        form.instance.produto.quantidade = (
            form.instance.produto.quantidade - form.initial.get("quantidade")
        ) + form.instance.quantidade
        form.instance.produto.save_base()
        return super().form_valid(form)


from django.http import JsonResponse


def get_produto_ajax(request):
    data = {}
    if request.method == "POST":
        produto_id = request.POST["produto_id"]

        try:
            produto = Produto.objects.filter(id=produto_id)

        except Exception:
            data["error_message"] = "error"
            return JsonResponse(data)
        return JsonResponse(list(produto.values("id", "quantidade")), safe=False)
