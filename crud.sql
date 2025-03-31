
--------------------------------------------------------------------------------------------------------
-- CREATE
--------------------------------------------------------------------------------------------------------

-- only need to add name, price, and category_id, the product_id will autofill after autoincrementing from the last product_id
INSERT INTO Products (name, price, category_id) VALUES
    ('Apple', '0.75', '2'
);

INSERT INTO Products (name, price, category_id) VALUES
    ('Daisy Shampoo', '3.50', '3'
);


--------------------------------------------------------------------------------------------------------
-- READ
--------------------------------------------------------------------------------------------------------

-- Display all columns from specified table
SELECT * FROM Categories;
SELECT * FROM Customers;
SELECT * FROM Inventory;
SELECT * FROM Products;
SELECT * FROM Suppliers;
SELECT * FROM Transactions;
SELECT * FROM Transactions_details;


-- View 1 of Transactions
-- Joining Transactions and Transactions_details table to view all details at the same time
-- Only displays transaction_id column once, since they are duplicates from joining the tables
SELECT 
	Transactions.transaction_id, 
	Transactions.customer_id, 
	Transactions.created_at, 
	Transactions_details.product_id, 
	Transactions_details.quantity, 
	Transactions_details.total_cost
FROM Transactions
JOIN Transactions_details 
	ON Transactions.transaction_id = Transactions_details.transaction_id



-- View 2 of Transactions
-- Joining Transactions and Transactions_details table to view all details at the same time
-- GROUP_CONCAT: merges multiple values (product_id/quantity/total_cost) from the same transaction_id into concatenated string
-- GROUP BY: groups rows from the same transaction_id
SELECT 
    Transactions.transaction_id, 
    Transactions.customer_id, 
    Transactions.created_at, 
    GROUP_CONCAT(Transactions_details.product_id) AS product_ids, 
    GROUP_CONCAT(Transactions_details.quantity) AS quantities, 
    GROUP_CONCAT(Transactions_details.total_cost) AS total_cost
FROM Transactions
JOIN Transactions_details 
    ON Transactions.transaction_id = Transactions_details.transaction_id
GROUP BY 
    Transactions.transaction_id, 
    Transactions.customer_id, 
    Transactions.created_at;


--------------------------------------------------------------------------------------------------------
-- UPDATE
--------------------------------------------------------------------------------------------------------

-- discount $1.00 for Mascara
UPDATE Products 
SET price = 8.99
WHERE name = 'Mascara';


--------------------------------------------------------------------------------------------------------
-- DELETE
--------------------------------------------------------------------------------------------------------

-- delete product 'Apple' that was created earlier
DELETE FROM Products
WHERE name = 'Apple';