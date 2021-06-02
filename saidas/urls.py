from django.urls import path

from . import views

app_name = "saidas"

urlpatterns = [
    path("", views.SaidaView.as_view(), name="index"),
    path("lista/", views.SaidaListView.as_view(), name="lista_saidas"),
    path("nova/", views.SaidaCreateView.as_view(), name="nova_saida"),
    # path("lista/", views.SaidaListView.as_view(), name="lista_saidas"),
    # path("lista/", views.SaidaListView.as_view(), name="lista_saidas"),
]
