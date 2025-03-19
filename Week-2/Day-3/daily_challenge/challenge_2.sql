-- 1. Table USERS
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- 2. Table PRODUCT_ORDERS
CREATE TABLE product_orders (
    id SERIAL PRIMARY KEY,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INT,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- 3. Table ITEMS
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    quantity INT DEFAULT 1,
    order_id INT,
    CONSTRAINT fk_order FOREIGN KEY (order_id) REFERENCES product_orders(id) ON DELETE CASCADE
);

-- =================================================

-- Insérer des utilisateurs
INSERT INTO users (username, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Charlie', 'charlie@example.com');

-- Insérer des commandes (product_orders)
INSERT INTO product_orders (user_id, order_date) VALUES
(1, '2024-03-18 10:00:00'), -- Commande 1 : Alice
(1, '2024-03-19 15:30:00'), -- Commande 2 : Alice
(2, '2024-03-20 09:45:00'); -- Commande 3 : Bob

-- Insérer des items (items)
INSERT INTO items (name, price, quantity, order_id) VALUES
('Laptop', 1200.00, 1, 1),
('Mouse', 25.50, 2, 1),
('Keyboard', 45.00, 1, 1),

('Monitor', 300.00, 2, 2),
('HDMI Cable', 15.00, 3, 2),

('Printer', 150.00, 1, 3),
('Ink Cartridge', 35.00, 4, 3);

-- my function

CREATE OR REPLACE FUNCTION get_all_d (order_id_param INT) RETURNS NUMERIC AS $total$ 
declare
    total NUMERIC;
BEGIN 
total := (select sum(i.price * i.quantity) from items i inner join product_orders po on i.order_id = po.id where i.order_id = order_id_param);
RETURN total;
END;
$total$ LANGUAGE plpgsql;

select get_all_d(1);

-- other function 

CREATE OR REPLACE FUNCTION get_order_totals(order_id_param INT)
RETURNS NUMERIC AS $$
DECLARE
    total NUMERIC;
BEGIN
    SELECT COALESCE(SUM(price * quantity), 0)
    INTO total
    FROM items
    WHERE order_id = order_id_param;

    RETURN total;
END;
$$ LANGUAGE plpgsql;
SELECT get_order_totals(1);