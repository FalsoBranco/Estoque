# from django.shortcuts import render
from typing import Any

from django.forms.models import BaseModelForm
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

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

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        print(request.POST)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        print(form.instance.quantidade)
        print(form.instance.produto.quantidade)
        form.instance.preco = 1
        return super().form_valid(form)
