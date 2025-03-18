-- Exercise 1 :

-- 1. Fetch the last 2 customers in alphabetical order (A-Z), excluding 'id'
SELECT firstname, lastname
FROM customers
ORDER BY firstname ASC
OFFSET (
    SELECT COUNT(*) - 2
    FROM customers
)
LIMIT 2;

-- 2. Delete all purchases made by Scott
DELETE FROM purchases
WHERE customer_id = (
    SELECT id FROM customers
    WHERE firstname = 'Scott' AND lastname = 'Scott'
);

-- 3. Does Scott still exist in the customers table?
SELECT *
FROM customers
WHERE firstname = 'Scott' AND lastname = 'Scott';

-- 4. Find all purchases
-- Join purchases with customers table, so that Scott’s order will appear,
-- but instead of his firstname and lastname, you only see NULL.
-- -> Use LEFT JOIN (keep all purchases, even those without a matching customer)
SELECT p.id AS purchase_id,
       p.quantity_purchased,
       c.firstname,
       c.lastname
FROM purchases p
LEFT JOIN customers c
ON p.customer_id = c.id;

-- 5. Find all purchases
-- Join purchases with customers table, so that Scott’s order will NOT appear.
-- -> Use INNER JOIN (only purchases with existing customers will appear)
SELECT p.id AS purchase_id,
       p.quantity_purchased,
       c.firstname,
       c.lastname
FROM purchases p
INNER JOIN customers c
ON p.customer_id = c.id;
