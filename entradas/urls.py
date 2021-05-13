from django.urls import path

from . import views

app_name = "entradas"

urlpatterns = [
    path("", views.EntradaView.as_view(), name="index"),
    path("lista/", views.EntradaListView.as_view(), name="lista_entradas"),
    path("nova/", views.EntradaCreateView.as_view(), name="nova_entrada"),
    path("delete/<int:pk>", views.EntradaDeleteView.as_view(), name="deleta_entrada"),
]
