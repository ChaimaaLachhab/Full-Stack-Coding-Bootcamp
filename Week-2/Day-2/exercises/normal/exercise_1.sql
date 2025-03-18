-- 1️ Get all items, ordered by price (lowest to highest)
SELECT *
FROM item
ORDER BY price ASC;

-- 2️ Get items with a price above or equal to 80, ordered by price (highest to lowest)
SELECT *
FROM item
WHERE price >= 80
ORDER BY price DESC;

-- 3️ Get the first 3 customers in alphabetical order by first name (A-Z)
-- Excluding the primary key column (assuming it's named "customer_id")
SELECT first_name, last_name, email
FROM customer
ORDER BY first_name ASC
LIMIT 3;

-- 4️ Get all last names only, in reverse alphabetical order (Z-A)
SELECT last_name
FROM customer
ORDER BY last_name DESC;
