-- Exercise 3: Items and Customers

-- Part I: Create purchases table
CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    item_id INT REFERENCES items(id),
    quantity_purchased INT
);

-- Insert purchases with subqueries
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE firstname = 'Scott' AND lastname = 'Scott'),
    (SELECT id FROM items WHERE name = 'fan'),
    1
);

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE firstname = 'Melanie' AND lastname = 'Johnson'),
    (SELECT id FROM items WHERE name = 'large desk'),
    10
);

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE firstname = 'Greg' AND lastname = 'Jones'),
    (SELECT id FROM items WHERE name = 'small desk'),
    2
);

-- Part II

-- 1. Get all purchases
SELECT * FROM purchases;

-- 2. Get all purchases joining with customers table
SELECT p.*, c.firstname, c.lastname
FROM purchases p
JOIN customers c ON p.customer_id = c.id;

-- 3. Purchases of customer with ID 5
SELECT * FROM purchases
WHERE customer_id = 5;

-- 4. Purchases for a large desk AND a small desk
SELECT p.*, i.name
FROM purchases p
JOIN items i ON p.item_id = i.id
WHERE i.name IN ('large desk', 'small desk');

-- 5. Show all customers who have made a purchase (firstname, lastname, item name)
SELECT c.firstname, c.lastname, i.name AS item_name
FROM purchases p
JOIN customers c ON p.customer_id = c.id
JOIN items i ON p.item_id = i.id;

-- 6. Add a row referencing a customer but not an item
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (1, NULL, 1);