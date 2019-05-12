--Nome: Produtos Importados
--Resultado: Wrong answer (20%)
--Data: 12/05/19 18:09:49
--Linguagem: PostgreSQL
SELECT p.name, p2.name from products as p
join providers as p2 on(p.id_providers = p2.id)
where p2.name = 'Sansul SA'
and p.id_categories in (
	select id from categories
	where name = 'Imported');