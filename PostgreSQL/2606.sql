--Nome: Categorias
--Resultado: Accepted
--Data: 12/05/19 17:26:15
--Linguagem: PostgreSQL
SELECT p.id, p.name from products as p
where p.id_categories in(
SELECT c.id from categories as c
where c.name LIKE 'super%');