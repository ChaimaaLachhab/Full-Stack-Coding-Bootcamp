-- Part I : Customer and CustomerProfile (One-to-One)

-- Drop tables if they already exist (optional for clean slate)
DROP TABLE IF EXISTS customer_profile;
DROP TABLE IF EXISTS customer;

-- 1. Create Customer table
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

-- 2. Create Customer Profile table
CREATE TABLE customer_profile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT FALSE,
    customer_id INTEGER UNIQUE, -- one-to-one, unique reference
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);

-- 3. Insert customers
INSERT INTO customer (first_name, last_name)
VALUES 
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');

-- 4. Insert customer profiles (using subqueries to get the customer id)
INSERT INTO customer_profile (isLoggedIn, customer_id)
VALUES
(TRUE, (SELECT id FROM customer WHERE first_name = 'John')),
(FALSE, (SELECT id FROM customer WHERE first_name = 'Jerome'));

-- ============================================

-- 1. Get the first_name of the LoggedIn customers
SELECT c.first_name
FROM customer c
JOIN customer_profile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = TRUE;

-- 2. Get all customers' first_name and isLoggedIn status, even if they don't have a profile (LEFT JOIN)
SELECT 
    c.first_name,
    cp.isLoggedIn
FROM customer c
LEFT JOIN customer_profile cp ON c.id = cp.customer_id;

-- 3. Get the number of customers that are not logged in (isLoggedIn = FALSE OR profile doesn't exist)
SELECT 
    COUNT(*) AS not_logged_in_customers
FROM customer c
LEFT JOIN customer_profile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = FALSE OR cp.isLoggedIn IS NULL;

-- Part II : Books - Students - Library (Many-to-Many)

-- Drop tables if they exist (optional)
DROP TABLE IF EXISTS library;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS book;

-- 1. Create Book table
CREATE TABLE book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL
);

-- 2. Insert books
INSERT INTO book (title, author)
VALUES 
('Alice In Wonderland', 'Lewis Carroll'),
('Harry Potter', 'J.K Rowling'),
('To kill a mockingbird', 'Harper Lee');

-- 3. Create Student table with age constraint (CHECK)
CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    age INTEGER CHECK (age <= 15)
);

-- 4. Insert students
INSERT INTO student (name, age)
VALUES 
('John', 12),
('Lera', 11),
('Patrick', 10),
('Bob', 14);

-- 5. Create Library table (junction table)
CREATE TABLE library (
    book_fk_id INTEGER,
    student_fk_id INTEGER,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id),
    FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (student_fk_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- 6. Add records in the junction table using subqueries
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date)
VALUES
(
    (SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM student WHERE name = 'John'),
    '2022-02-15'
),
(
    (SELECT book_id FROM book WHERE title = 'To kill a mockingbird'),
    (SELECT student_id FROM student WHERE name = 'Bob'),
    '2021-03-03'
),
(
    (SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM student WHERE name = 'Lera'),
    '2021-05-23'
),
(
    (SELECT book_id FROM book WHERE title = 'Harry Potter'),
    (SELECT student_id FROM student WHERE name = 'Bob'),
    '2021-08-12'
);

-- ============================================

-- 1. Select all columns from the library table
SELECT * FROM library;

-- 2. Select the name of the student and the title of the borrowed books
SELECT 
    s.name AS student_name,
    b.title AS book_title,
    l.borrowed_date
FROM library l
JOIN student s ON l.student_fk_id = s.student_id
JOIN book b ON l.book_fk_id = b.book_id
ORDER BY s.name;

-- 3. Select the average age of the children that borrowed the book "Alice In Wonderland"
SELECT 
    AVG(s.age) AS average_age
FROM library l
JOIN student s ON l.student_fk_id = s.student_id
JOIN book b ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland';

-- Delete student 'John'
DELETE FROM student
WHERE name = 'John';

-- Verify if the related entry in the library table has been deleted (ON DELETE CASCADE)
SELECT * FROM library;

