import sqlite3
import tkinter as tk
from tkinter import ttk # for displaying table

con = sqlite3.connect("Supermarket.db")
cursor = con.cursor()

# TK window and title
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Supermarket Inventory Management")  # title of window
        self.geometry("1300x800")   # size of window
        
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
        
# Function to display the Products
    def DisplayProducts(self, db_file):
    # connect to database and create pointer to call SQL queries
        con = sqlite3.connect(db_file)  
        cursor = con.cursor()

    # get all column names from Products table
        cursor.execute("""
            SELECT 
                Products.product_id, 
                Products.name AS product_name, 
                Products.price AS price, 
                Categories.name AS category_name, 
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
        tree.pack(expand=True, fill="both")
    

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