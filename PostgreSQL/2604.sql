--Nome: Menores que 10 ou Maiores que 100
--Resultado: Accepted
--Data: 12/05/19 17:13:11
--Linguagem: PostgreSQL
select id, name from products 
where price < 10 or price > 100;