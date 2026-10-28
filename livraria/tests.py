from decimal import Decimal
from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from .models import Categoria, Livro


class DemonstrarCommandTests(TestCase):
    def test_command_demonstrates_crud_and_join(self) -> None:
        output = StringIO()

        call_command("demonstrar", stdout=output)

        self.assertEqual(Livro.objects.count(), 5)
        self.assertEqual(Categoria.objects.count(), 3)
        self.assertEqual(
            Livro.objects.get(isbn="9788535902778").preco,
            Decimal("54.90"),
        )
        self.assertFalse(Livro.objects.filter(isbn="9999999999999").exists())

        text = output.getvalue()
        self.assertIn("CREATE: 5 livros inseridos ou atualizados.", text)
        self.assertIn("READ: todos os livros", text)
        self.assertIn("READ: livros com preco abaixo de R$ 50", text)
        self.assertIn("READ: livros em ordem alfabetica", text)
        self.assertIn("UPDATE: livro alterado", text)
        self.assertIn("DELETE: registro temporario removido.", text)
        self.assertIn("JOIN: livros e categorias", text)
        self.assertIn("O Hobbit | J. R. R. Tolkien | Fantasia", text)

    def test_command_is_safe_to_run_more_than_once(self) -> None:
        call_command("demonstrar", stdout=StringIO())
        call_command("demonstrar", stdout=StringIO())

        self.assertEqual(Livro.objects.count(), 5)
        self.assertEqual(Categoria.objects.count(), 3)
