--Nome: Locações de Setembro
--Resultado: Accepted
--Data: 12/05/19 18:01:48
--Linguagem: PostgreSQL
select c.name, r.rentals_date from customers as c
join rentals r on(c.id = r.id_customers)
where EXTRACT(YEAR FROM r.rentals_date) = 2016
and EXTRACT(MONTH FROM r.rentals_date) = 9;