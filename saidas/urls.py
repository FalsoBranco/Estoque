from django.urls import path

from . import views

app_name = "saidas"

urlpatterns = [
    path("", views.SaidaView.as_view(), name="index"),
    path("lista/", views.SaidaListView.as_view(), name="lista_saidas"),
    path("nova/", views.SaidaCreateView.as_view(), name="nova_saida"),
    path("delete/<int:pk>", views.SaidaDeleteView.as_view(), name="deleta_saida"),
    path("alterar/<int:pk>", views.SaidaUpdateView.as_view(), name="alterar_saida"),
    path("get-produto-ajax/", views.get_produto_ajax, name="get_produto_ajax"),
]
