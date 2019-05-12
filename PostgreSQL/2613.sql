--Nome: Filmes em Promoção
--Resultado: Accepted
--Data: 12/05/19 17:49:44
--Linguagem: PostgreSQL
SELECT m.id, m.name from movies as m
where m.id_prices in(
	select p.id from prices as p
	where p.value <2);