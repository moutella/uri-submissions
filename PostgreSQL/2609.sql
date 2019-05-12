--Nome: Produtos por Categorias
--Resultado: Accepted
--Data: 12/05/19 17:36:16
--Linguagem: PostgreSQL
select c.name, sum(amount) from products as p, categories c
where p.id_categories = c.id
GROUP BY c.name;