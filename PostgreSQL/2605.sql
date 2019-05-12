--Nome: Representantes Executivos
--Resultado: Accepted
--Data: 12/05/19 17:18:01
--Linguagem: PostgreSQL
select p1.name, p2.name from products as p1
join providers as p2 on p1.id_providers = p2.id
where p1.id_categories = 6;