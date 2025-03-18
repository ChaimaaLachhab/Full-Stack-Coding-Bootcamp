-- Exercise 2: Students Table

-- Update birth_dates for Lea and Marc Benichou
UPDATE students
SET birth_date = '1998-11-02'
WHERE first_name IN ('Lea', 'Marc') AND last_name = 'Benichou';

-- Change the last name of David from Grez to Guez
UPDATE students
SET last_name = 'Guez'
WHERE first_name = 'David' AND last_name = 'Grez';

-- Delete Lea Benichou
DELETE FROM students
WHERE first_name = 'Lea' AND last_name = 'Benichou';

-- Count all students
SELECT COUNT(*) AS total_students
FROM students;

-- Count students born after 01/01/2000
SELECT COUNT(*) AS born_after_2000
FROM students
WHERE birth_date > '2000-01-01';

-- Add a column math_grade
ALTER TABLE students
ADD COLUMN math_grade INT;

-- Update math_grade
UPDATE students SET math_grade = 80 WHERE id = 1;
UPDATE students SET math_grade = 90 WHERE id IN (2, 4);
UPDATE students SET math_grade = 40 WHERE id = 6;

-- Count how many students have a grade bigger than 83
SELECT COUNT(*) AS students_with_high_grade
FROM students
WHERE math_grade > 83;

-- Add another Omer Simpson
INSERT INTO students (first_name, last_name, birth_date, math_grade)
SELECT 'Omer', 'Simpson', birth_date, 70
FROM students
WHERE first_name = 'Omer' AND last_name = 'Simpson'
LIMIT 1;

-- Count how many grades each student has
SELECT first_name, last_name, COUNT(math_grade) AS total_grade
FROM students
GROUP BY first_name, last_name;

-- Sum of all students grades
SELECT SUM(math_grade) AS sum_of_grades
FROM students;
