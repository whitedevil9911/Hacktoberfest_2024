CREATE DATABASE flat_sales_db;

USE flat_sales_db;

CREATE TABLE inquiries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    message TEXT,
    submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
