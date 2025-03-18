-- Exercise 2: Happy Halloween

-- 1️ How many stores there are, and in which city and country they are located.
SELECT
    s.store_id,
    ci.city,
    co.country
FROM store s
JOIN address a ON s.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id;


-- 2️ How many hours of viewing time there are in total in each store.
SELECT
    s.store_id,
    SUM(f.length) AS total_minutes,
    ROUND(SUM(f.length)/60.0, 2) AS total_hours,
    ROUND(SUM(f.length)/60.0/24.0, 2) AS total_days
FROM store s
JOIN inventory i ON s.store_id = i.store_id
JOIN film f ON i.film_id = f.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id AND r.return_date IS NULL
WHERE r.rental_id IS NULL
GROUP BY s.store_id
ORDER BY s.store_id;


-- 3️ A list of all customers in the cities where the stores are located.
SELECT DISTINCT
    c.customer_id,
    c.first_name,
    c.last_name,
    ci.city
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
WHERE ci.city_id IN (
    SELECT ci.city_id
    FROM store s
    JOIN address a ON s.address_id = a.address_id
    JOIN city ci ON a.city_id = ci.city_id
);


-- 4️ A list of all customers in the countries where the stores are located.
SELECT DISTINCT
    c.customer_id,
    c.first_name,
    c.last_name,
    co.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE co.country_id IN (
    SELECT DISTINCT co.country_id
    FROM store s
    JOIN address a ON s.address_id = a.address_id
    JOIN city ci ON a.city_id = ci.city_id
    JOIN country co ON ci.country_id = co.country_id
);


-- 5️ Create a 'safe list' of all movies excluding Horror and scary keywords.
SELECT
    f.film_id,
    f.title,
    f.description,
    f.length
FROM film f
WHERE f.film_id NOT IN (
    SELECT fc.film_id
    FROM film_category fc
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = 'Horror'
)
AND f.title !~* '(beast|monster|ghost|dead|zombie|undead)'
AND f.description !~* '(beast|monster|ghost|dead|zombie|undead)';


-- 6️ Get the sum of their viewing time (length) in minutes, hours, and days.
SELECT
    SUM(f.length) AS total_minutes,
    ROUND(SUM(f.length)/60.0, 2) AS total_hours,
    ROUND(SUM(f.length)/60.0/24.0, 2) AS total_days
FROM film f
WHERE f.film_id NOT IN (
    SELECT fc.film_id
    FROM film_category fc
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = 'Horror'
)
AND f.title !~* '(beast|monster|ghost|dead|zombie|undead)'
AND f.description !~* '(beast|monster|ghost|dead|zombie|undead)';


