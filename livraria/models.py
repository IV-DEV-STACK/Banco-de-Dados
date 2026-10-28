from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "livraria_categorias"
        ordering = ["nome"]
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self) -> str:
        return self.nome


class Livro(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="livros",
    )
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_publicacao = models.DateField()
    disponivel = models.BooleanField(default=True)

    class Meta:
        db_table = "livraria_livros"
        ordering = ["titulo"]
        verbose_name = "livro"
        verbose_name_plural = "livros"

    def __str__(self) -> str:
        return f"{self.titulo} - {self.autor}"
