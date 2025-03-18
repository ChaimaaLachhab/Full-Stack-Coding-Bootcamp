-- Exercise 1: DVD Rental

-- 1. Find out how many films there are for each rating.
SELECT rating, COUNT(*) AS film_count
FROM film
GROUP BY rating;

-- 2. Get a list of all the movies that have a rating of G or PG-13.
SELECT *
FROM film
WHERE rating IN ('G', 'PG-13');

-- 3. Filter this list further: 
-- Movies under 2 hours long, rental price under 3.00, sorted alphabetically.
SELECT *
FROM film
WHERE rating IN ('G', 'PG-13')
AND length < 120
AND rental_rate < 3.00
ORDER BY title ASC;

-- 4. Find a customer and update their details.
UPDATE customer
SET first_name = 'Chaimaa',
    last_name = 'El Idrissi',
    email = 'chaimaa@email.com'
WHERE customer_id = 1;

-- 5. Find the customer's address and update it.
UPDATE address
SET address = '123 Boulevard Zerktouni',
    district = 'Casablanca',
    postal_code = '20000',
    phone = '0600000000'
WHERE address_id = (
    SELECT address_id FROM customer WHERE customer_id = 1
);
