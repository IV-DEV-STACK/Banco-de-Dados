import os
import sys
from getpass import getpass

from django.core.management import execute_from_command_line


DATABASE_COMMANDS = {
    "changepassword",
    "createsuperuser",
    "dbshell",
    "demonstrar",
    "dumpdata",
    "flush",
    "loaddata",
    "migrate",
    "runserver",
    "shell",
}


def _selected_settings() -> str:
    for index, argument in enumerate(sys.argv[1:], start=1):
        if argument.startswith("--settings="):
            return argument.partition("=")[2]
        if argument == "--settings" and index + 1 < len(sys.argv):
            return sys.argv[index + 1]
    return os.getenv("DJANGO_SETTINGS_MODULE", "")


def _selected_command() -> str:
    arguments = iter(sys.argv[1:])
    for argument in arguments:
        if argument == "--settings":
            next(arguments, "")
        elif not argument.startswith("-"):
            return argument
    return ""


def main() -> None:
    """Executa comandos Django solicitando a senha do banco sem exibi-la."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    command = _selected_command()
    if (
        command in DATABASE_COMMANDS
        and not os.getenv("DB_PASSWORD")
        and _selected_settings() != "project.test_settings"
    ):
        os.environ["DB_PASSWORD"] = getpass("Senha do PostgreSQL (entrada oculta): ")

    execute_from_command_line(sys.argv)
