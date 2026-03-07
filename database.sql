CREATE DATABASE minipos;
USE minipos;

CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    quantity INT,
    total DOUBLE
);
