# Table of contents
- [Table of contents](#table-of-contents)
  - [foreign key](#foreign-key)


## foreign key
```sql
-- create a simple customers table
CREATE TABLE customers (
	customer_id INT AUTO_INCREMENT PRIMARY KEY,
	customer_name VARCHAR(100)
);

-- create orders table which will contain a foreign key
CREATE TABLE orders (
	order_id INT AUTO_INCREMENT PRIMARY KEY,
	customer_id INT,
	amount DOUBLE,
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- insert data into tables
INSERT INTO `customers` (`customer_id`, `customer_name`) VALUES
(1, 'Adam'),
(2, 'Andy'),
(3, 'Joe'),
(4, 'Sandy');

INSERT INTO `orders` (`order_id`, `customer_id`, `amount`) VALUES
(1, 1, 19.99),
(2, 1, 35.15),
(3, 3, 17.56),
(4, 4, 12.34);

-- retrieving data with a JOIN query
SELECT * FROM orders
JOIN customers USING(customer_id)
```
![foreign key](assets/foreignkey.png)