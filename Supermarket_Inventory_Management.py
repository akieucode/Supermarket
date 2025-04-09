import sqlite3
import tkinter as tk
con = sqlite3.connect("Supermarket.db")
cursor = con.cursor()

# TK window and title
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Supermarket Inventory Management")  # title of window
        self.geometry("1300x800")   # size of window
        
        self.homePage = HomePage(self)
        self.productsPage = ProductsPage(self)
        self.inventoryPage = InventoryPage(self)
        
        self.homePage.grid(row=0, column=0, sticky="nsew")  # display homepage
    
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
        label = tk.Label (self, text= "Home")  
        label.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
        
    # Buttons to navigate to another page    
        button = tk.Button(self, text="Products", command=master.show_productsPage)
        button.grid(row=1, column=0, pady=0, padx=10, sticky="nsew")

        button = tk.Button(self, text="Inventory", command=master.show_inventoryPage)
        button.grid(row=2, column=0, pady=0, padx=10, sticky="nsew")

class ProductsPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = tk.Label (self, text= "Products")   
        label.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
        
        button = tk.Button(self, text="Main Menu", command=master.show_homePage)
        button.grid(row=1, column=0, pady=0, padx=10, sticky="nsew")
        
class InventoryPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = tk.Label (self, text= "Inventory")
        label.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
        
        button = tk.Button(self, text="Main Menu", command=master.show_homePage)
        button.grid(row=1, column=0, pady=0, padx=10, sticky="nsew")
        
        

#run the Tkinter app    
if __name__ == "__main__":
    app = App() 
    app.mainloop()