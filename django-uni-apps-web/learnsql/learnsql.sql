USE sql_store;

SELECT *
	FROM customers;
SELECT *
	from orders;
-- 	WHERE customer_id < 5 and points>1000 
	-- ORDER BY state;

-- SELECT first_name, last_name, points, points*2, MOD(points, 10) as Alias
-- 	FROM customers;

-- INSERT INTO customers 
-- 	VALUES ('11', 'John', 'Smith', '2000-01-01', '647-000-0000', '1 main street', 'Austin','TX', '100');
    
-- SELECT *
-- 	FROM customers;

-- SELECT state
-- 	FROM customers;
--     
-- SELECT distinct state
-- 	FROM customers;


-- select * 
-- from customers
-- where first_name LIKE '%';


-- select *
-- 	from customers
--     where first_name regexp 'elka|ambur' OR
-- 		last_name regexp '^(MY|SE).*(B[RU])*.*(tt|ON)$';
--     
-- select *
-- 	from customers
--     order by points desc
--     LIMIT 3;


-- select * -- order_id, o.customer_id, first_name, last_name
-- 	from orders as o
--     JOIN customers as c ON o.customer_id = c.customer_id;-- has implied INNER JOIN

-- select order_id, p.product_id, quantity, p.unit_price
-- 	from products as p
-- 		join order_items as o ON o.product_id = p.product_id;
	


-- select o.order_id, o.customer_id, c.first_name, c.last_name, os.name as status
-- 	from orders as o
--     join customers as c
-- 		ON o.customer_id = c.customer_id
-- 	join order_statuses as os
-- 		ON o.status = os.order_status_id;



-- select * 
-- 	from order_items as oi
--     join order_item_notes as oin
-- 		on oi.order_id = oin.order_id or oi.product_id = oin.product_id
-- 	order by oi.order_id;

-- implicit join syntax, probably shouldnt do this or you might get a crossjoin 
-- select *
-- from orders as o, customers as c
-- where o.customer_id = c.customer_id;


-- left join returns everything from the from
-- right join returns everything from the join
-- right join wouldnt change anything here as order_id is a subset of customer_id
-- select c.customer_id, c.first_name, o.order_id
-- 	from customers as c
--     left join orders as o 
-- 		on o.customer_id = c.customer_id
--     order by c.customer_id;


-- select p.product_id, p.name, oi.quantity
-- 	from products as p
--     left join order_items as oi
-- 		on p.product_id = oi.product_id
-- 	order by p.product_id



-- select c.first_name, o.order_id, sh.name as shipper
-- 	from orders o
--     join customers c
--     -- on o.customer_id = c.customer_id
-- 		using (customer_id)
-- 	left join shippers sh
-- 		using(shipper_id);

-- natural joins guess how to join, probably shouldnt do it, gets rid of duplicate columns tho
-- select *
-- 	from orders as o
--     natural join customers as c;

    
-- cross joins select everything ffrom both tables
-- select c.first_name as customer, p.name as product
-- 	from customers c
--     cross join products p;


-- make sure to have the same number of columns when unioning
-- select order_id, order_date, 'ACTIVE' as status
-- 	from orders
--     where order_date >= '2019-01-01'

-- Union

-- select order_id, order_date, 'ARCHIVED' as status
-- 	from orders
--     where order_date < '2019-01-01';


-- select customer_id, first_name, points, 'Bronze' as type
-- 	from customers
--     where points < 2000

-- union
-- select customer_id, first_name, points, 'Silver' as type
-- 	from customers
--     where points between 2000 and 3000
-- union
-- select customer_id, first_name, points, 'Gold' as type
-- 	from customers
--     where points > 3000
-- 	order by first_name;


-- INSERT INTO table (*optional columns) VALUES (val1, ...)

-- insert into customers
-- 	values 
--     (DEFAULT, 
--     'John', 
--     'Doe', 
--     '1987-02-24', 
--     DEFAULT,
--     '1 First Street',
--     'Los angeles',
--     'CA',
--     DEFAULT);


-- insert into shippers (name)
-- values ('Shipper1'),
-- 		('Shipper2'),
--         ('Shipper3');



-- insert into orders (customer_id, order_date, status)
-- values (1, '2019-01-02', 1);


-- insert into order_items 
-- values (last_insert_id(), 1, 1, 2.95),
-- 		(last_insert_id(), 2, 1, 3.95);


-- create table order_archived as 
-- select * from orders;


-- insert into order_archived
-- select *
-- from orders
-- where order_date < '2019-01-01';


-- use sql_invoicing;
-- create table invoices_archived as
-- 	select i.invoice_id, i.number, c.name, i.invoice_total, payment_total, i.invoice_date, i.due_date, payment_date
-- 	from invoices as i
-- 	right join clients as c
--     on i.client_id = c.client_id
--     where payment_date is not null;


-- update invoices
-- set payment_total = 10, payment_date = '2019-03-01'
-- where invoice_id = 1;


-- update customers
-- set points = points + 50
-- where birth_date < '1990-01-01'; 


use sql_invoicing;

-- update invoices
-- set 
-- 		payment_total = invoice_total * 0.5,
--         payment_date = due_date
-- where client_id in
-- 	(select client_id
--     from clients
--     where state in ('CA', 'NY'));

    
delete from invoices
where invoice_id = 1