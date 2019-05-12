--Nome: Nenhuma Locação
--Resultado: Accepted
--Data: 12/05/19 18:05:25
--Linguagem: PostgreSQL
SELECT c.id, c.name from customers as c
where c.id not in(select id_customers from locations);