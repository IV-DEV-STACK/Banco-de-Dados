-- Todos os livros e suas categorias (JOIN).
SELECT l.id, l.isbn, l.titulo, l.autor, c.nome AS categoria,
       l.preco, l.data_publicacao, l.disponivel
FROM livraria_livros AS l
JOIN livraria_categorias AS c ON c.id = l.categoria_id
ORDER BY l.id;

-- Filtro (WHERE): livros com preco abaixo de R$ 50.
SELECT id, titulo, preco
FROM livraria_livros
WHERE preco < 50;

-- Ordenacao (ORDER BY).
SELECT id, titulo, preco
FROM livraria_livros
ORDER BY titulo ASC;

-- Conferir o livro alterado pelo UPDATE.
SELECT id, titulo, preco
FROM livraria_livros
WHERE isbn = '9788535902778';

-- Deve retornar zero linhas: o registro temporario foi removido.
SELECT id, titulo
FROM livraria_livros
WHERE isbn = '9999999999999';

-- JOIN entre livros e categorias.
SELECT l.titulo, l.autor, c.nome AS categoria
FROM livraria_livros AS l
JOIN livraria_categorias AS c ON c.id = l.categoria_id
ORDER BY c.nome, l.titulo;
