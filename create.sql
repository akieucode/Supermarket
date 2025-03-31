-- Categories Table
CREATE TABLE Categories (
	category_id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL UNIQUE,
	description TEXT,
	department TEXT NOT NULL
);
-- Functional Dependency:
-- category_id --> name, description, department
-- name --> description, department (assuming name is unique for each category)


-- Suppliers Table
CREATE TABLE Suppliers (
	supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL UNIQUE,
	phone VARCHAR (15),
	email VARCHAR (50)
);
-- Functional Dependency:
-- supplier_id --> name, phone, email
-- name --> phone, email (assuming name is unique for each supplier)


-- Products Table
CREATE TABLE Products (
	product_id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL UNIQUE,
	price DECIMAL (10,2),
	category_id INT,
	FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE SET NULL
	);
-- Functional Dependency:
-- product_id --> name, price, category_id
-- name --> price, category_id (assuming name is unique for each product)
	
	
-- Inventory Table
CREATE TABLE Inventory (
	inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
	product_id INT,
	supplier_id INT,
	quantity INT,
	FOREIGN KEY (product_id) REFERENCES Products (product_id),
	FOREIGN KEY (supplier_id) REFERENCES Suppliers (supplier_id)
);
-- Functional Dependency:
-- inventory_id --> product_id, supplier_id, quantity


-- Customers Table
CREATE TABLE Customers (
	customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	phone VARCHAR(15),
	email VARCHAR(50)
);
-- Functional Dependency:
-- customer_id --> name, phone, email


-- Transactions Table
CREATE TABLE Transactions (
	transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
	customer_id INT,
	created_at DATE,
	FOREIGN KEY (customer_id) REFERENCES Customers (customer_id)
);
-- Functional Dependency:
-- transaction_id --> customer_id, created_at
	
	
-- Transactions_details Table
CREATE TABLE Transactions_details (
	transaction_id INTEGER,
	product_id INT,
	quantity INT,
	total_cost decimal (10,2),
	FOREIGN KEY (transaction_id) REFERENCES Transactions (transaction_id),
	FOREIGN KEY (product_id) REFERENCES Products (product_id)
);
-- Functional Dependency:
-- (transaction_id, product_id) --> quantity, total_cost
	
	
	
	
	