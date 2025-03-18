-- 🌟 EXERCISE 2 : dvdrental database 🌟

-- 1. Select all columns from the customer table
SELECT * FROM customer;

-- 2. Display the names (first_name, last_name) using an alias named “full_name”
SELECT first_name || ' ' || last_name AS full_name
FROM customer;

-- 3. Get all the dates that accounts were created (no duplicates)
SELECT DISTINCT create_date
FROM customer;

-- 4. Get all customer details ordered by first name descending
SELECT * 
FROM customer
ORDER BY first_name DESC;

-- 5. Get the film ID, title, description, year of release, and rental rate in ascending order by rental rate
SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;

-- 6. Get the address and phone number of all customers living in the Texas district
SELECT address, phone
FROM address
WHERE district = 'Texas';

-- 7. Retrieve all movie details where the movie id is either 15 or 150
SELECT * 
FROM film
WHERE film_id IN (15, 150);

-- 8. Check if your favorite movie exists
-- Replace 'My Favorite Movie' with your actual favorite movie title
SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title = 'My Favorite Movie';

-- 9. Find all movies starting with the first two letters of your favorite movie
-- Replace 'My' with the first two letters of your favorite movie
SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title ILIKE 'My%';

-- 10. Find the 10 cheapest movies
SELECT film_id, title, rental_rate
FROM film
ORDER BY rental_rate ASC
LIMIT 10;

-- 11. Find the next 10 cheapest movies (offset skips the first 10 results)
SELECT film_id, title, rental_rate
FROM film
ORDER BY rental_rate ASC
OFFSET 10
LIMIT 10;

-- Option 2: Using a subquery and NOT IN (pure SQL without LIMIT/OFFSET)
SELECT film_id, title, rental_rate
FROM film
WHERE rental_rate NOT IN (
    SELECT DISTINCT rental_rate
    FROM film
    ORDER BY rental_rate ASC
    LIMIT 10
)
ORDER BY rental_rate ASC
LIMIT 10;

-- 12. Join customer table and payment table: Get first name, last name, amount, and date of every payment made, ordered by customer id
SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY c.customer_id ASC;

-- 13. Get all the movies which are not in inventory
SELECT f.film_id, f.title
FROM film f
WHERE f.film_id NOT IN (
    SELECT DISTINCT inventory.film_id
    FROM inventory
);

-- 14. Find which city is in which country
SELECT ci.city_id, ci.city, co.country
FROM city ci
JOIN country co ON ci.country_id = co.country_id
ORDER BY co.country, ci.city;

-- BONUS: See how your sellers have been doing
-- Get customer id, names, amount, and payment date ordered by staff_id (seller)
SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.staff_id
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY p.staff_id ASC, c.customer_id;
