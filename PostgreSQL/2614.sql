--Nome: Locações de Setembro
--Resultado: Wrong answer (35%)
--Data: 12/05/19 18:00:00
--Linguagem: PostgreSQL
select c.name, r.rentals_date from customers as c, rentals as r
where r.id in(select r.id from rentals as r
where EXTRACT(MONTH FROM r.rentals_date) = 9) and 
c.id in(select r.id_customers from rentals as r
where EXTRACT(MONTH FROM r.rentals_date) = 9);