from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import transaction

from livraria.models import Categoria, Livro


BOOKS = (
    ("9788535902778", "O Hobbit", "J. R. R. Tolkien", "Fantasia", "59.90", "1937-09-21", True),
    ("9788532530783", "Duna", "Frank Herbert", "Ficcao cientifica", "69.90", "1965-08-01", True),
    ("9786555320354", "Torto Arado", "Itamar Vieira Junior", "Literatura brasileira", "49.90", "2019-08-01", True),
    ("9788535914849", "1984", "George Orwell", "Ficcao cientifica", "39.90", "1949-06-08", True),
    ("9788535910663", "Dom Casmurro", "Machado de Assis", "Literatura brasileira", "29.90", "1899-01-01", False),
)


class Command(BaseCommand):
    help = "Insere livros de exemplo e demonstra consultas e operacoes CRUD."

    @transaction.atomic
    def handle(self, *args: object, **options: object) -> None:
        categories: dict[str, Categoria] = {}
        for name in sorted({book[3] for book in BOOKS}):
            category, _ = Categoria.objects.get_or_create(nome=name)
            categories[name] = category

        for isbn, title, author, category_name, price, publication_date, available in BOOKS:
            Livro.objects.update_or_create(
                isbn=isbn,
                defaults={
                    "titulo": title,
                    "autor": author,
                    "categoria": categories[category_name],
                    "preco": Decimal(price),
                    "data_publicacao": publication_date,
                    "disponivel": available,
                },
            )
        self.stdout.write(f"CREATE: {len(BOOKS)} livros inseridos ou atualizados.")

        self.stdout.write("\nREAD: todos os livros")
        for book in Livro.objects.select_related("categoria").values_list(
            "id", "isbn", "titulo", "autor", "categoria__nome",
            "preco", "data_publicacao", "disponivel",
        ):
            self.stdout.write(" | ".join(str(value) for value in book))

        self.stdout.write("\nREAD: livros com preco abaixo de R$ 50")
        for book in Livro.objects.filter(preco__lt=Decimal("50.00")).values_list(
            "id", "titulo", "preco",
        ):
            self.stdout.write(" | ".join(str(value) for value in book))

        self.stdout.write("\nREAD: livros em ordem alfabetica")
        for book in Livro.objects.order_by("titulo").values_list("id", "titulo", "preco"):
            self.stdout.write(" | ".join(str(value) for value in book))

        updated_count = Livro.objects.filter(isbn="9788535902778").update(
            preco=Decimal("54.90"),
        )
        if updated_count != 1:
            raise RuntimeError("UPDATE não encontrou o livro esperado.")
        updated = Livro.objects.get(isbn="9788535902778")
        self.stdout.write(
            f"\nUPDATE: livro alterado: {updated.id} | {updated.titulo} | {updated.preco}"
        )

        Livro.objects.update_or_create(
            isbn="9999999999999",
            defaults={
                "titulo": "Registro temporario para exclusao",
                "autor": "Projeto",
                "categoria": categories["Fantasia"],
                "preco": Decimal("1.00"),
                "data_publicacao": "2026-01-01",
                "disponivel": False,
            },
        )
        deleted_count, _ = Livro.objects.filter(isbn="9999999999999").delete()
        if deleted_count != 1:
            raise RuntimeError("DELETE não removeu o registro temporário esperado.")
        self.stdout.write("\nDELETE: registro temporario removido.")

        self.stdout.write("\nJOIN: livros e categorias")
        for book in Livro.objects.select_related("categoria").order_by(
            "categoria__nome", "titulo",
        ).values_list("titulo", "autor", "categoria__nome"):
            self.stdout.write(" | ".join(str(value) for value in book))
