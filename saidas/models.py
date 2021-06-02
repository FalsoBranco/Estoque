from django.db import models

# Create your models here.


class Saida(models.Model):
    produto = models.ForeignKey(
        "produtos.Produto",
        verbose_name="Produto",
        on_delete=models.PROTECT,
    )
    quantidade = models.IntegerField("Quantidade")
    preco = models.DecimalField("Preço", max_digits=5, decimal_places=2)

    criado = models.DateTimeField("Criado em", auto_now_add=True)
    modificado = models.DateTimeField("Modificado em", auto_now=True)

    class Meta:
        verbose_name = "saida"
        verbose_name_plural = "saidas"
        ordering = ["-criado"]

    def __str__(self):
        return self.produto.nome

    # def get_absolute_url(self):
    #     return reverse("saida_detail", kwargs={"pk": self.pk})
