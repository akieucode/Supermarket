import sqlite3
import tkinter as tk
from tkinter import ttk # for displaying table
from tkinter import messagebox  # displaying error messages

con = sqlite3.connect("Supermarket.db")
cursor = con.cursor()

# TK window and title
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Supermarket Inventory Management")  # title of window
        self.geometry("1050x500")   # size of window
        
# Create the page frames
        self.homePage = HomePage(self)

        self.productsPage = ProductsPage(self)
        self.productsTable = tk.Frame(self)
        
        self.inventoryPage = InventoryPage(self)
        self.inventoryTable = tk.Frame(self)

# Display homePage first
        self.homePage.grid(row=0, column=0, sticky="nsew")  
    
    def show_homePage(self):
        self.homePage.grid(row=0, column=0, sticky="nsew")
        self.productsPage.grid_forget()
        self.inventoryPage.grid_forget()
        
    def show_productsPage(self):
        self.productsPage.grid(row=0, column=0, sticky="nsew")
        self.homePage.grid_forget()
        
    def show_inventoryPage(self):
        self.inventoryPage.grid(row=0, column=0, sticky="nsew")
        self.homePage.grid_forget()

# function to refresh inventory after adding a product from ProductsPage and it updates inventory
    def refresh_inventory(self):
        self.inventoryPage.displayInventory("Supermarket.db")

class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = tk.Label (self, text= "Home", font=("Helvetica", 24, "bold"))  
        label.grid(row=0, column=0, pady=10, padx=460, sticky="nsew")
        
    # Buttons to navigate to another page    
        button = tk.Button(self, text="Products", command=master.show_productsPage)
        button.grid(row=1, column=0, pady=0, padx=460, sticky="nsew")

        button = tk.Button(self, text="Inventory", command=master.show_inventoryPage)
        button.grid(row=2, column=0, pady=0, padx=460, sticky="nsew")

class ProductsPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = tk.Label (self, text= "Products", font=("Helvetica", 24, "bold"))  
        label.grid(row=1, column=1, pady=10, padx=450, sticky="nsew")
        
        button = tk.Button(self, text="Main Menu", command=master.show_homePage)
        button.grid(row=2, column=1, pady=0, padx=450, sticky="nsew")

        self.productsTable=tk.Frame(self)
        self.productsTable.grid(row=6, column=1, sticky="nsew", padx=10, pady=10)
        self.DisplayProducts("Supermarket.db")

        button_add_product = tk.Button(self, text="Add Product", command=self.addProductsWindow)
        button_add_product.grid(row=3, column=1, pady=0, padx=80, sticky="e")

        button_delete_product = tk.Button(self, text="Delete Product", fg="red", command=self.deleteProduct)
        button_delete_product.grid(row=4, column=1, pady=5, padx=80, sticky="e")

        self.input_field_search_bar = tk.Entry(self)
        self.input_field_search_bar.bind("<Return>", self.search_product)
        self.input_field_search_bar.grid(row=5, column=1, pady=0, padx=80, sticky="ns")

# Function to display the Products
    def DisplayProducts(self, db_file):
    # clear old content for any changes in database
        for widget in self.productsTable.winfo_children():
            widget.destroy()

    # connect to database and create pointer to call SQL queries
        con = sqlite3.connect(db_file)  
        cursor = con.cursor()

    # get all column names from Products and Categories table (join)
        cursor.execute("""
            SELECT 
                Products.product_id, 
                Products.product_name, 
                Products.price, 
                Categories.category_name, 
                Categories.department
            FROM Products
            JOIN Categories 
                ON Products.category_id = Categories.category_id
        """)

    # get rows from the Products table, store data into list of tuples
        rows = cursor.fetchall()

    # cursor.description is a list of tuples: (columns = ['product_id', 'name', 'price'])
        columns = [description[0] for description in cursor.description]
        
    # create treeview widget
        self.tree = ttk.Treeview(self.productsTable, columns=columns, show="headings")
        self.tree.column("product_id", width=175, anchor="center")
        self.tree.column("product_name", width=175, anchor="center")
        self.tree.column("price", width=175, anchor="center")
        self.tree.column("category_name", width=175, anchor="center")
        self.tree.column("department", width=175, anchor="center")

    # column headers
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
    # insert rows, data from database
        for row in rows:
            self.tree.insert("", "end", values=row)

        con.close() # close connection

    # display the table
        self.tree.pack(pady=0, padx=0)

    def addProductsWindow(self):
    # open separate window on top of current    
        add_product_window = tk.Toplevel(self)
        add_product_window.title("Add New Product")
        add_product_window.geometry("400x300")

        tk.Label(add_product_window, text="product_name").pack(pady=5)
        pname_input = tk.Entry(add_product_window)
        pname_input.pack()

        tk.Label(add_product_window, text="price").pack(pady=5)
        pprice_input = tk.Entry(add_product_window)
        pprice_input.pack()

        tk.Label(add_product_window, text="category_name").pack(pady=5)
        cname_input = tk.Entry(add_product_window)
        cname_input.pack()

        tk.Label(add_product_window, text="department").pack(pady=5)
        department_input = tk.Entry(add_product_window)
        department_input.pack()

    # inserting new data into the db
        def confirmAddProduct():
            # getter function to receive user input
            product_name = pname_input.get()
            price = pprice_input.get()
            category_name = cname_input.get()
            department = department_input.get()

            # condition to check if all fields are filled out
            if product_name and price and category_name and department:
                try:
                    con = sqlite3.connect("Supermarket.db")
                    cursor = con.cursor()

                # look for the category to see if it exists
                    cursor.execute("SELECT category_id FROM Categories WHERE category_name = ?", (category_name,))
                    result = cursor.fetchone() # fetch first matching result
                    if result:
                        category_id = result[0] # get the existing category_id because category is found
                    else: # insert new category because it doesn't exist                                     
                        cursor.execute(
                            "INSERT INTO Categories (category_name, department) VALUES (?,?)",
                            (category_name, department))
                        con.commit()

                # fetch new category id
                    cursor.execute("SELECT category_id FROM Categories WHERE category_name = ?", (category_name,))
                    category_id = cursor.fetchone()[0]  # get the only result, extract tuple and hold the actual category_id value
                # insert new product into Products table that links with the category_id        
                    cursor.execute(
                        "INSERT INTO Products (product_name, price, category_id) VALUES (?,?,?)",
                        (product_name, float(price), category_id)
                    )
                    con.commit()

                # fetch product_id
                    cursor.execute(
                        "SELECT product_id FROM Products WHERE product_name = ?", (product_name,))
                    result_product_id = cursor.fetchone()
                    if result_product_id:
                        product_id = result_product_id[0]

                    # insert the product_id and set quantity at 0 in the Inventory Table    
                        cursor.execute(
                            "INSERT INTO Inventory (product_id, quantity) VALUES (?, ?)",
                            (product_id, 0)
                        )
                        con.commit()
                    con.close()
                    add_product_window.destroy()
                    app.refresh_inventory()

        # destroy current windows and reopen to refresh pages
                    self.productsTable.destroy()
                    self.productsTable=tk.Frame(self)           
                    self.productsTable.grid(row=6, column=1, sticky="nsew", padx=10, pady=10)
                    self.DisplayProducts("Supermarket.db")

                except Exception as e:
                    tk.messagebox.showerror("Error", str(e))
            else:
                messagebox.showerror("Error")

        tk.Button(add_product_window, text="Add", command=confirmAddProduct).pack(pady=20)

    # delete selected product
    def deleteProduct(self):
        selected = self.tree.selection()    # selected items from the table
        if not selected:
            return
        
        item = self.tree.item(selected[0])  # get the data values from the first selected item
        product_id = item['values'][0]      # get the tuple of the data values in the first column (where product_id is stored)

        confirm = messagebox.askyesno("Delete Product", f"Are you sure you want to delete this product?") # display message box for confirmation
        if not confirm: # do nothing and close the message box
            return

    # delete data from the db
        con = sqlite3.connect("Supermarket.db")
        cursor = con.cursor()
    # delete product from product table
        cursor.execute("DELETE FROM Products WHERE product_id = ?", (product_id,))
    # delete product from inventory table
        cursor.execute("DELETE FROM Inventory WHERE product_id = ?", (product_id,))
        con.commit()
        con.close()

        self.DisplayProducts("Supermarket.db")  # refresh the table
        app.refresh_inventory() # refresh InventoryPage table

    def search_product(self, event=None):
        search_input = self.input_field_search_bar.get().strip().lower()
        
        # if search field is empty return the current table in db
        if search_input == "":
            self.DisplayProducts("Supermarket.db")
        else:
            cursor.execute("""
            SELECT 
                Products.product_id, 
                Products.product_name, 
                Products.price, 
                Categories.category_name, 
                Categories.department
            FROM Products
            JOIN Categories 
                ON Products.category_id = Categories.category_id
            WHERE Products.product_name LIKE ? COLLATE NOCASE
                OR Categories.category_name LIKE ? COLLATE NOCASE
                OR Categories.department LIKE ? COLLATE NOCASE
            """,
            ('%' + search_input + '%','%' + search_input + '%', '%' + search_input + '%'))
            rows = cursor.fetchall()
            self.displaySearchResults(rows)

    # display the filtered table
    def displaySearchResults(self, rows):
        for widget in self.productsTable.winfo_children():
            widget.destroy()
            
        columns = [description[0] for description in cursor.description]
        self.tree = ttk.Treeview(self.productsTable, columns=columns, show="headings")
        self.tree.column("product_id", width=175, anchor="center")
        self.tree.column("product_name", width=175, anchor="center")
        self.tree.column("price", width=175, anchor="center")
        self.tree.column("category_name", width=175, anchor="center")
        self.tree.column("department", width=175, anchor="center")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
            
        for row in rows:
            self.tree.insert("", "end", values=row)
        self.tree.pack(pady=0, padx=0)

class InventoryPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = tk.Label (self, text= "Inventory", font=("Helvetica", 24, "bold"))
        label.grid(row=1, column=1, pady=10, padx=460, sticky="nsew")
        
        button = tk.Button(self, text="Main Menu", command=master.show_homePage)
        button.grid(row=2, column=1, pady=0, padx=460, sticky="nsew")

        self.inventoryTable=tk.Frame(self)
        self.inventoryTable.grid(row=6, column=1, sticky="n", padx=10, pady=60)

        self.displayInventory("Supermarket.db")

        button_update_quantity = tk.Button(self, text="Update Quantity", command=self.updateQuantityWindow)
        button_update_quantity.grid(row=5, column=1, pady=0, padx=80, sticky="e")

    def displayInventory(self, db_file):
    # clear old content for any changes in database
        for widget in self.inventoryTable.winfo_children():
            widget.destroy()

    # connect to database and create pointer to call SQL queries
        con = sqlite3.connect(db_file)  
        cursor = con.cursor()

    # get all column names from Inventory and Products table (join)
        cursor.execute("""
            SELECT
                Inventory.inventory_id,
                Inventory.product_id,
                Products.product_name,
                Products.price,
                Inventory.quantity
            FROM Inventory
            JOIN Products
                ON Inventory.product_id = Products.product_id
        """)

    # get rows from the Products table, store data into list of tuples
        rows = cursor.fetchall()

    # cursor.description is a list of tuples:
        columns = ['inventory_id', 'product_id', 'product_name', 'price', 'quantity']
        
    # create treeview widget
        self.tree = ttk.Treeview(self.inventoryTable, columns=columns, show="headings")
        self.tree.column("inventory_id", width=175, anchor="center")
        self.tree.column("product_id", width=175, anchor="center")
        self.tree.column("product_name", width=175, anchor="center")
        self.tree.column("price", width=175, anchor="center")
        self.tree.column("quantity", width=175, anchor="center")

        for col in columns:
            self.tree.heading(col, text=col)

    # column headers
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
    # insert rows, data from database
        for row in rows:
            self.tree.insert("", "end", values=row)

        con.close() # close connection

    # display the table
        self.tree.pack(pady=0, padx=0)

    def updateQuantityWindow(self):
    # open separate window on top of current    
        update_quantity_window = tk.Toplevel(self)
        update_quantity_window.title("Update Quantity")
        update_quantity_window.geometry("200x100")

        tk.Label(update_quantity_window, text="Update Quantity").pack(pady=5)
        quantity_input = tk.Entry(update_quantity_window)
        quantity_input.pack()


        def updateQuantity():
            selected_item = self.tree.selection()
            if not selected_item:
                return
            
            item = self.tree.item(selected_item[0])  # get the data values from the first selected item
            inventory_id = item['values'][0]      # get the tuple of the data values in the first column (where inventory_id is stored)

            new_quantity = quantity_input.get()
            if not new_quantity.isdigit():  # check if input is a number
                messagebox.showerror("Invalid", "Please enter a number.")
                return
            else:
                con = sqlite3.connect("Supermarket.db")
                cursor = con.cursor()
                cursor.execute("""
                    UPDATE Inventory
                    SET quantity = ?
                    WHERE inventory_id = ?
                """, ((new_quantity), inventory_id))
                con.commit()
                con.close()

                update_quantity_window.destroy()

            # destroy current windows and reopen to refresh pages
                self.inventoryTable.destroy()
                self.inventoryTable=tk.Frame(self)
                self.inventoryTable.grid(row=6, column=1, columnspan=2, sticky="nsew", padx=10, pady=10)
                self.displayInventory("Supermarket.db")  
        tk.Button(update_quantity_window, text="Update", command=updateQuantity).pack(pady=10)
                


#run the Tkinter app    
if __name__ == "__main__":
    app = App() # app is the root
    app.mainloop()