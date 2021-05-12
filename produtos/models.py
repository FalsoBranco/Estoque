from django.db import models


# Create your models here.
class Produto(models.Model):
    nome = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Identificador", max_length=100, auto_created=True)
    cor = models.ForeignKey(
        "produtos.Cor", on_delete=models.PROTECT, verbose_name="Cor"
    )
    descricao = models.TextField("Descrição", blank=True)
    preco = models.DecimalField("Preço", decimal_places=2, max_digits=8)
    quantidade = models.IntegerField("Quantidade", default=0)
    criado = models.DateTimeField("Criado em", auto_now_add=True)
    modificado = models.DateTimeField("Modificado em", auto_now=True)

    class Meta:
        verbose_name = "produto"
        verbose_name_plural = "produtos"

    def __str__(self):
        return self.nome

    def preco_quantidade(self):
        return self.preco * self.quantidade


class Cor(models.Model):

    cor = models.CharField(("Cor"), max_length=200)

    class Meta:
        verbose_name = "cor"
        verbose_name_plural = "cores"

    def __str__(self):
        return self.cor
