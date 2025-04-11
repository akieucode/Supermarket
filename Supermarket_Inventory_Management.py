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
        self.geometry("1100x500")   # size of window
        
# Create the page frames
        self.homePage = HomePage(self)

        self.productsPage = ProductsPage(self)
        self.productsTable = tk.Frame(self)
        
        self.inventoryPage = InventoryPage(self)

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

    
     
class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = tk.Label (self, text= "Home", font=("Helvetica", 24, "bold"))  
        label.grid(row=0, column=0, pady=10, padx=400, sticky="nsew")
        
    # Buttons to navigate to another page    
        button = tk.Button(self, text="Products", command=master.show_productsPage)
        button.grid(row=1, column=0, pady=0, padx=400, sticky="nsew")

        button = tk.Button(self, text="Inventory", command=master.show_inventoryPage)
        button.grid(row=2, column=0, pady=0, padx=400, sticky="nsew")

class ProductsPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)


        label = tk.Label (self, text= "Products", font=("Helvetica", 24, "bold"))  
        label.grid(row=0, column=0, pady=0, padx=400, sticky="nsew")
        
        button = tk.Button(self, text="Main Menu", command=master.show_homePage)
        button.grid(row=1, column=0, pady=0, padx=400, sticky="nsew")

        self.productsTable=tk.Frame(self)
        self.productsTable.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        self.DisplayProducts("Supermarket.db")

        button_add_product = tk.Button(self, text="Add Product", command=self.addProductsWindow)
        button_add_product.grid(row=1, column=1, pady=0, padx=10, sticky="nsew")

# Function to display the Products
    def DisplayProducts(self, db_file):
    # connect to database and create pointer to call SQL queries
        con = sqlite3.connect(db_file)  
        cursor = con.cursor()

    # get all column names from Products table
        cursor.execute("""
            SELECT 
                Products.product_id, 
                Products.product_name, 
                Products.price AS price, 
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
        tree = ttk.Treeview(self.productsTable, columns=columns, show="headings")
    # column headers
    
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")
    # insert rows, data from database
        for row in rows:
            tree.insert("", "end", values=row)

        con.close() # close connection

    # display the table
        tree.pack(pady=0, padx=0, expand=True, fill="both")

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
                    con.close()

                    add_product_window.destroy()

        # destroy current windows and reopen to refresh pages
                    self.productsTable.destroy()
                    self.productsTable=tk.Frame(self)
                    self.productsTable.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
                    self.DisplayProducts("Supermarket.db")
                except Exception as e:
                    tk.messagebox.showerror("Error", str(e))
            else:
                messagebox.showerror("Error")

        tk.Button(add_product_window, text="Add", command=confirmAddProduct).pack(pady=20)
                                


class InventoryPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = tk.Label (self, text= "Inventory", font=("Helvetica", 24, "bold"))
        label.grid(row=0, column=0, pady=10, padx=400, sticky="nsew")
        
        button = tk.Button(self, text="Main Menu", command=master.show_homePage)
        button.grid(row=1, column=0, pady=0, padx=400, sticky="nsew")
        
        

#run the Tkinter app    
if __name__ == "__main__":
    app = App() 
    app.mainloop()