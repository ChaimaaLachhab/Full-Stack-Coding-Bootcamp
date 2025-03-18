-- 🌟 Exercise 1: DVD Rental

-- 1. Get a list of all the languages from the language table
SELECT * FROM language;

-- 2. Get a list of all films joined with their languages
SELECT 
    f.title AS film_title,
    f.description,
    l.name AS language_name
FROM 
    film f
JOIN 
    language l ON f.language_id = l.language_id;

-- 3. Get all languages, even if there are no films in those languages
SELECT 
    f.title AS film_title,
    f.description,
    l.name AS language_name
FROM 
    language l
LEFT JOIN 
    film f ON f.language_id = l.language_id;

-- 4. Create a new table called new_film with id and name
CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- 5. Add some new films to the new_film table
INSERT INTO new_film (name) VALUES 
('Hunter X Hunter'),
('The Demon Slayer'),
('One Piece');

-- 6. Create customer_review table
CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT NOT NULL,
    language_id INT NOT NULL,
    title VARCHAR(255),
    score INT CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT NOW(),
    CONSTRAINT fk_film
        FOREIGN KEY (film_id) REFERENCES new_film (id)
        ON DELETE CASCADE,
    CONSTRAINT fk_language
        FOREIGN KEY (language_id) REFERENCES language (language_id)
);

-- 7. Add 2 movie reviews (make sure they reference existing films and languages)
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES 
(1, 1, 'Amazing Adventure', 9, 'A thrilling journey from start to finish!'),
(2, 2, 'Deep Sea Mystery', 8, 'Intriguing plot with stunning visuals.');

-- 8. Delete a film that has a review, and observe cascading delete
DELETE FROM new_film WHERE id = 1;
