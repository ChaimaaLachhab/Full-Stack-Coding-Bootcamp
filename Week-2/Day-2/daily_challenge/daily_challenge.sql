-- Create FirstTab Table
CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);

-- Insert data into FirstTab
INSERT INTO FirstTab VALUES
(5, 'Pawan'),
(6, 'Sharlee'),
(7, 'Krish'),
(NULL, 'Avtaar');

-- Select all from FirstTab
SELECT * FROM FirstTab;

-- Create SecondTab Table
CREATE TABLE SecondTab (
    id integer
);

-- Insert data into SecondTab
INSERT INTO SecondTab VALUES
(5),
(NULL);

-- Select all from SecondTab
SELECT * FROM SecondTab;

-- Q1: Count rows where id in FirstTab is not in SecondTab where id is NULL
-- Answer: The query excludes rows where the id is NULL in SecondTab. The remaining ids in FirstTab are 5, 6, and 7.
-- Expected Output: 3
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( 
    SELECT id FROM SecondTab WHERE id IS NULL 
);

-- Q2: Count rows where id in FirstTab is not in SecondTab where id = 5
-- Answer: The query excludes rows where the id is 5 in SecondTab. The remaining ids in FirstTab are 6, 7, and NULL.
-- Expected Output: 3
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( 
    SELECT id FROM SecondTab WHERE id = 5 
);

-- Q3: Count rows where id in FirstTab is not in SecondTab
-- Answer: The query excludes rows where the id is 5 or NULL in SecondTab. The remaining ids in FirstTab are 6 and 7.
-- Expected Output: 2
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( 
    SELECT id FROM SecondTab 
);

-- Q4: Count rows where id in FirstTab is not in SecondTab where id is NOT NULL
-- Answer: The query excludes rows where the id is 5 in SecondTab (since only 5 is NOT NULL). The remaining ids in FirstTab are 6, 7, and NULL.
-- Expected Output: 3
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( 
    SELECT id FROM SecondTab WHERE id IS NOT NULL 
);
