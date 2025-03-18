-- 🌟 Exercise 2: DVD Rental

-- 1. Use UPDATE to change the language of some films (ensure valid languages)
UPDATE film
SET language_id = 2
WHERE film_id IN (1, 2, 3);

-- 2. Which foreign keys are defined for the customer table? 
SELECT 
    tc.constraint_name, kcu.column_name, 
    ccu.table_name AS foreign_table_name, 
    ccu.column_name AS foreign_column_name 
FROM 
    information_schema.table_constraints AS tc 
JOIN 
    information_schema.key_column_usage AS kcu
  ON tc.constraint_name = kcu.constraint_name
JOIN 
    information_schema.constraint_column_usage AS ccu
  ON ccu.constraint_name = tc.constraint_name
WHERE 
    tc.constraint_type = 'FOREIGN KEY' AND 
    tc.table_name='customer';

-- 3. How does it affect INSERT?
-- I cannot insert a customer without valid address_id and store_id values that exist in address and store tables.

-- 4. Drop customer_review table
DROP TABLE customer_review;

-- 5. Find how many rentals are still outstanding (not returned yet)
SELECT COUNT(*)
FROM rental
WHERE return_date IS NULL;

-- 6. Find the 30 most expensive movies that are outstanding (not returned)
SELECT 
    f.film_id, f.title, f.replacement_cost, r.rental_id
FROM 
    rental r
JOIN 
    inventory i ON r.inventory_id = i.inventory_id
JOIN 
    film f ON i.film_id = f.film_id
WHERE 
    r.return_date IS NULL
ORDER BY 
    f.replacement_cost DESC
LIMIT 30;

-- 7. Find the 4 movies your friend wants to rent

-- 1st film: about a sumo wrestler, with Penelope Monroe
SELECT DISTINCT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE 
    a.first_name = 'Penelope' AND 
    a.last_name = 'Monroe' AND 
    (f.description ILIKE '%sumo%' OR f.title ILIKE '%sumo%');

-- 2nd film: short documentary (< 1 hour), rated "R"
SELECT title
FROM film
WHERE 
    length < 60 AND 
    rating = 'R' AND 
    description ILIKE '%documentary%';

-- 3rd film: rented by Matthew Mahan, paid over $4.00, returned between 28 July and 1 August 2005
SELECT DISTINCT f.title
FROM rental r
JOIN payment p ON r.rental_id = p.rental_id
JOIN customer c ON r.customer_id = c.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE 
    c.first_name = 'Matthew' AND
    c.last_name = 'Mahan' AND
    p.amount > 4.00 AND
    r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

-- 4th film: Matthew Mahan watched it, it has "boat" in the title or description, and is an expensive DVD to replace
SELECT DISTINCT f.title, f.replacement_cost
FROM rental r
JOIN customer c ON r.customer_id = c.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE 
    c.first_name = 'Matthew' AND
    c.last_name = 'Mahan' AND
    (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC
LIMIT 1;