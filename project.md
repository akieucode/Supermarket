# Supermarket
Supermarket Inventory Management CRUD App

GitHub repo link: https://github.com/akieucode/Supermarket
YouTube demo video link: https://youtu.be/RwJREvOvj8k 

This project is a desktop application that features a simple GUI to interact with the database.
The app contains predefined buttons that can perform CRUD operations.

The CRUD Operations:
Create: Users can add a product into the Products table.
Read: Users can look up products with a filtered search.
Update: Users can update the quantity in the Inventory table.
Delete: Users can delete a product from the Products table, and it will also reflect in the Inventory table.

The buttons have pre-defined SQL statements that perform join on multiple tables.
- Add button (in the Add Product window) --> inserts data into 2 tables (Products and Categories) that are joined.
- Yes button (in the Delete Product window --> deletes data from 2 tables (Products and Inventory) that are joined.

There is also an entry box that will demonstrate joint search from multiple tables.
- Search bar --> reads data from 2 tables (Products and Categories) that are joined.
- Users can search keywords from the following columns: product_name, category_name, and department)

In the ProductsPage --> The productsTable displays columns and rows from the joined tables 'Products' and 'Categories'.
The first columns 'product_id, product_name, price' are from the Products table.
The next columns 'category_name, department' are from Categories table. 
The tables are joined with 'category_id'.

In the InventoryPage --> The inventoryTable displays columns and rows from the joined tables 'Inventory' and 'Products'.
These columns 'inventory_id, product_id, quantity' are from the Inventory table.
The other columns 'product_name, price' are from Products table.
The tables are joined with 'product_id'.

The Tech Stack:
Database: SQLite with DB Browser
Backend: Python
Frontend/GUI: Tkinter

Getting started:
Install Python. (Tkinter and sqlite3 are built-in with Python).

Open --> command prompt as admin
Type --> cd 'target directory' (location to store repository)
Type --> git clone https://github.com/akieucode/Supermarket.git

Open --> VSCode editor
Open folder --> Supermarket (in the location repository was stored).
Select --> Supermarket_Inventory_Management.py file in the explorer tab.
Run --> Start debugging (F5).
