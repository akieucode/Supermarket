-- Insert into Products Table
INSERT INTO Products (product_id, name, price, category_id) VALUES
    ('1', 'Celery (1 bunch)', '1.79', '1'),
    ('2', 'Orange (1 each)', '0.65', '2'),
    ('3', 'Dining chair (set of 4)', '150.00', '4'),
    ('4', 'Mascara', '9.99', '5'),
    ('5', 'Broccoli (1 crown)', '1.75', '1'
);



-- Insert into Categories Table
INSERT INTO Categories (category_id, name, description, department) VALUES
    ('1', 'Vegetables', 'edible plant such as carrots, broccoli, lettuce, and more', 'Produce'),
    ('2', 'Fruits', 'edible plant such as tropical fruits and berries', 'Produce'),
    ('3', 'Shampoo', 'soap for washing hair', 'Personal care'),
    ('4', 'Chair', 'piece of furniture for sitting', 'Furniture'),
    ('5', 'Makeup', 'beauty products applied to the face for enhancing appearance', 'Cosmetics'
);



-- Insert into Suppliers Table
INSERT INTO Suppliers (supplier_id, name, phone, email) VALUES
    ('1', 'Sunshinee Farm', '555-324-1453', 'support@sunshineefarm.com'),
    ('2', 'Glamorous Soothes', '555-423-2491', 'support@glamoroussoothes.com'),
    ('3', 'Comfort Livin', '555-252-5632', 'support@comfortlivin.com'),
    ('4', 'Luscious Beauty', '523-234-6735', 'info@lusciousbeauty.com'),
    ('5', 'CreativeStyles', '745-234-6623', 'info@creativestyles.com'
);


-- Insert into Inventory Table
INSERT INTO Inventory (inventory_id, product_id, supplier_id, quantity) VALUES
    ('1', '1', '1', '100' ),
    ('2', '2', '1', '100' ),
    ('3', '3', '3', '25' ),
    ('4', '4', '4', '50' ),
    ('5', '5', '1', '100'
);


-- Insert into Customers Table
INSERT INTO Customers (customer_id, name, phone, email) VALUES 
    ('1', 'Shayla Galleria', '153-524-6234', 'sgalleria@gmail.com'),
    ('2', 'Tom Michaels', '512-532-6643', 'tmichaels@gmail.com' ),
    ('3', 'Jerry Daniels', '675-234-7453', 'jdaniels@gmail.com'),
    ('4', 'Mary Nguyen', '742-134-1465', 'mnguyen@gmail.com'),
    ('5', 'Kenny Lam', '523-324-5322', 'klam@gmail.com'
);

-- Insert into Transactions Table
INSERT INTO Transactions (transaction_id, customer_id, created_at) VALUES 
    ('1', '1', '2025-03-28'),
    ('2', '2', '2025-03-30'),
    ('3', '3', '2025-03-30'),
    ('4', '4', '2025-03-30'),
    ('5', '5', '2025-03-30'
);

-- Insert into Transactions_details Table
INSERT INTO Transactions_details (transaction_id, product_id, quantity, total_cost) VALUES 
    ('1', '1', '2', '3.58'),
    ('1', '2', '5', '3.25'),
    ('1', '5', '2', '3.50'),
    ('2', '3', '1', '150.00'),
    ('3', '2', '12', '7.80'),
    ('4', '4', '1', '9.99'),
    ('5', '2', '20', '13.00'
);