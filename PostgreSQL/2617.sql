--Nome: Fornecedor Ajax SA
--Resultado: Accepted
--Data: 12/05/19 18:08:08
--Linguagem: PostgreSQL
SELECT p.name, p2.name from products as p
join providers as p2 on(p.id_providers = p2.id)
where p2.name = 'Ajax SA';