CREATE DATABASE IF NOT EXISTS shopflow;

USE shopflow;


CREATE TABLE products (

    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    description VARCHAR(255),

    price DECIMAL(10,2) NOT NULL

);


INSERT INTO products
(name, description, price)
VALUES

(
    'Laptop',
    'High performance laptop',
    65000
),

(
    'Smartphone',
    'Latest Android smartphone',
    30000
),

(
    'Headphones',
    'Wireless noise cancelling headphones',
    5000
),

(
    'Keyboard',
    'Mechanical gaming keyboard',
    2500
),

(
    'Mouse',
    'Wireless gaming mouse',
    1800
);
