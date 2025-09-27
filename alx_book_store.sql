-- Create Database
CREATE DATABASE IF NOT EXISTS alx_book_store;

-- Use the Database
USE alx_book_store;

-- Create Authors table
CREATE TABLE Authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);

-- Create Books table
CREATE TABLE Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT,
    price DOUBLE NOT NULL,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

-- Create Customers table
CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) UNIQUE NOT NULL,
    address TEXT
);

-- Create Orders table
CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Create Order_Details table
CREATE TABLE Order_Details (
    orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity DOUBLE NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

INSERT INTO Authors (author_name) VALUES
('J.K. Rowling'),
('George R.R. Martin'),
('J.R.R. Tolkien');

INSERT INTO Books (title, author_id, price, publication_date) VALUES
('Harry Potter and the Philosopher''s Stone', 1, 19.99, '1997-06-26'),
('A Game of Thrones', 2, 22.99, '1996-08-06'),
('The Hobbit', 3, 15.99, '1937-09-21');

INSERT INTO Customers (customer_name, email, address) VALUES
('Alice Johnson', 'alicejohnson@deontest.com', '123 Maple Street, Springfield'),
('Bob Smith', 'bobsmith@deontest.com', '456 Oak Avenue, Metropolis');

INSERT INTO Orders (customer_id, order_date) VALUES
(1, '2023-10-01'),
(2, '2023-10-02');

INSERT INTO Order_Details (order_id, book_id, quantity) VALUES
(1, 1, 2),
(1, 3, 1),
(2, 2, 1);

-- Query to join tables and get order details
SELECT 
    o.order_id,
    c.customer_name,
    b.title AS book_title,
    od.quantity,
    (b.price * od.quantity) AS total_price,
    o.order_date
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
JOIN Order_Details od ON o.order_id = od.order_id
JOIN Books b ON od.book_id = b.book_id
ORDER BY o.order_id;    
-- Query to find total sales per book
SELECT 
    b.title AS book_title,
    SUM(od.quantity) AS total_quantity_sold,
    SUM(b.price * od.quantity) AS total_sales
FROM Order_Details od
JOIN Books b ON od.book_id = b.book_id
GROUP BY b.book_id
ORDER BY total_sales DESC;          
-- Query to find top customers by total spending
SELECT 
    c.customer_name,                
    SUM(b.price * od.quantity) AS total_spent
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
JOIN Order_Details od ON o.order_id = od.order_id
JOIN Books b ON od.book_id = b.book_id
GROUP BY c.customer_id
ORDER BY total_spent DESC
LIMIT 5;
-- Query to find authors with the most books sold
SELECT 
    a.author_name,
    SUM(od.quantity) AS total_books_sold
FROM Order_Details od
JOIN Books b ON od.book_id = b.book_id
JOIN Authors a ON b.author_id = a.author_id
GROUP BY a.author_id
ORDER BY total_books_sold DESC 
LIMIT 5;

-- Query to find monthly sales trends
SELECT 
    DATE_FORMAT(o.order_date, '%Y-%m') AS order_month,
    SUM(b.price * od.quantity) AS total_sales
FROM Orders o
JOIN Order_Details od ON o.order_id = od.order_id
JOIN Books b ON od.book_id = b.book_id
GROUP BY order_month
ORDER BY order_month;   
