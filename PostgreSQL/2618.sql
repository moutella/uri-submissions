--Nome: Produtos Importados
--Resultado: Accepted
--Data: 12/05/19 18:10:24
--Linguagem: PostgreSQL
SELECT p.name, p2.name, 'Imported' as name from products as p
join providers as p2 on(p.id_providers = p2.id)
where p2.name = 'Sansul SA'
and p.id_categories in (
	select id from categories
	where name = 'Imported');