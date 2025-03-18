-- Exercise 1 : DVD Rentals

-- 1️ Get a list of all rentals which are out (have not been returned)
SELECT *
FROM rental
WHERE return_date IS NULL;

-- 2️ Get a list of all customers who have not returned their rentals.
-- Group by customer and count their rentals.
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(r.rental_id) AS unreturned_rentals
FROM rental r
JOIN customer c ON r.customer_id = c.customer_id
WHERE r.return_date IS NULL
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY unreturned_rentals DESC;


-- 3️ Get a list of all Action films with Joe Swank.
SELECT
    f.film_id,
    f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE
    a.first_name = 'Joe'
    AND a.last_name = 'Swank'
    AND c.name = 'Action';

-- Create a VIEW for films with Joe Swank to simplify future queries:
CREATE OR REPLACE VIEW joe_swank_films AS
SELECT
    f.film_id,
    f.title,
    c.name AS category
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE
    a.first_name = 'Joe'
    AND a.last_name = 'Swank';

SELECT * FROM joe_swank_films WHERE category = 'Action';