 -- Write a script that inserts multiple rows in the table customer (database alx_book_store) in your MySQL server.

-- 4 rows to be inserted

--Data insertion

--    - `customer_id` = `2`
--   - `customer_name` = `Blessing Malik`
--    - `email` = `bmalik@sandtech.com`
--    - `address` = `124 Happiness  Ave.`
--    - `customer_id` = `3`
--    - `customer_name` = `Obed Ehoneah`
--    - `email` = `eobed@sandtech.com`
--    - `address` = `125 Happiness  Ave.`
--    - `customer_id` = `4`
--    - `customer_name` = `Nehemial Kamolu`
--   - `email` = `nkamolu@sandtech.com`
--    - `address` = `126 Happiness  Ave.`

INSERT INTO customer (customer_id, customer_name, email, address)
VALUES (2, 'Blessing Malik', bmalik@sandtech.com`, '124 Happiness  Ave.'),
(3, 'Obed Ehoneah', 'eboded@sandtech.com', '125 Happiness  Ave.'),
(4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness  Ave.');

-- Ensure to commit your changes
COMMIT; 
