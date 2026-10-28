# Projeto Django: Livraria

Aplicação Django com PostgreSQL. O ORM cria e consulta as tabelas
`livraria_categorias` e `livraria_livros`; o SQLTools é usado para conferir os
dados e executar as consultas de verificação.

## Requisitos

- Python 3.10 ou superior
- Acesso ao PostgreSQL da conexão SQLTools `01` (banco `equipe01`)

## Instalação e configuração

```powershell
python -m pip install -e .
```

Configure `DB_HOST` com o endereço do PostgreSQL da turma, além de
`DB_PORT`, `DB_NAME` e `DB_USER` se forem diferentes dos valores padrão. O
host padrão é `127.0.0.1`; o endereço do servidor da turma é específico do
ambiente e não é incluído no repositório. A senha é solicitada de forma oculta
quando um comando Django precisa acessar o banco. Também é possível defini-la
na variável de ambiente `DB_PASSWORD`. Nunca inclua a senha no código, neste
documento ou em capturas de tela.

Opcionalmente, configure `DJANGO_SECRET_KEY` para substituir a chave local de
desenvolvimento antes de publicar a aplicação. O modo de desenvolvimento está
ativado por padrão para que o Django sirva os arquivos estáticos do Admin.
Em produção, defina `DJANGO_DEBUG=False` e sirva os arquivos estáticos por um
servidor web configurado para isso.

## Criar as tabelas e executar o CRUD

```powershell
python manage.py migrate
python manage.py demonstrar
```

O comando `demonstrar` cadastra cinco livros e suas categorias, lista todos os
livros, consulta livros abaixo de R$ 50, lista títulos em ordem alfabética,
altera o preço de um livro, insere e exclui um registro temporário com filtros
por ISBN e demonstra o `JOIN` entre livros e categorias. Pode ser executado
novamente sem duplicar os livros de exemplo.

O comando também pode ser executado com `python -m project demonstrar`.

## Conferir pelo SQLTools

1. Execute as migrações e o comando CRUD acima.
2. No VS Code, conecte ao PostgreSQL pela conexão SQLTools `01`.
3. Abra [sql/verificacao.sql](./sql/verificacao.sql) e execute as consultas
   para conferir todos os livros, o filtro, a ordenação, o `UPDATE`, o `DELETE`
   e o `JOIN`.
4. Faça as capturas de tela diretamente do SQLTools, sem exibir a senha.

As tabelas criadas pelo Django têm os nomes `livraria_categorias` e
`livraria_livros`. A estrutura é mantida pelas migrações da aplicação
[livraria](./livraria).

## Testes

Os testes usam um banco SQLite em memória e não precisam de conexão ao
PostgreSQL:

```powershell
python manage.py test --settings=project.test_settings
```
