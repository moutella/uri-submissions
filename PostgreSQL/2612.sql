--Nome: Os Atores Silva
--Resultado: Accepted
--Data: 12/05/19 17:47:26
--Linguagem: PostgreSQL
SELECT m.id, m.name from movies as m
where m.id_genres in(
	select g.id from genres as g
	where g.description = 'Action')
	and m.id in(
		select ma.id_movies from movies_actors as ma
		where ma.id_actors in(
		select a.id from actors as a
		where a.name = 'Marcelo Silva' or a.name = 'Miguel Silva'));