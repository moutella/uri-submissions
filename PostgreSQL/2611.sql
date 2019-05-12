--Nome: Filmes de Ação
--Resultado: Accepted
--Data: 12/05/19 17:43:28
--Linguagem: PostgreSQL
SELECT m.id, m.name from movies as m
where m.id_genres in(
select g.id from genres as g
where g.description = 'Action');