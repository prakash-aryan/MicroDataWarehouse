import sqlite3

conn = sqlite3.connect('microdatawarehouse.db')

conn.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        PRODUCT_ID TEXT PRIMARY KEY,
        PRODUCT_NAME TEXT,
        CATEGORY TEXT,
        PRICE REAL,
        QUANTITY INTEGER
    )
''')

conn.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        CUSTOMER_ID TEXT PRIMARY KEY,
        CUSTOMER_NAME TEXT,
        REGION TEXT,
        TOTAL_PURCHASES REAL
    )
''')

conn.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        EMPLOYEE_ID TEXT PRIMARY KEY,
        EMPLOYEE_NAME TEXT,
        DEPARTMENT TEXT,
        SALARY REAL
    )
''')

sales_data = [
    ('P001', 'iPhone 12', 'Electronics', 999.99, 100),
    ('P002', 'Samsung Galaxy S21', 'Electronics', 899.99, 80),
    ('P003', 'Nike Air Max', 'Footwear', 129.99, 200),
    ('P004', 'Adidas Ultraboost', 'Footwear', 149.99, 150),
    ('P005', 'Sony PlayStation 5', 'Electronics', 499.99, 50),
    ('P006', 'LG OLED TV', 'Electronics', 1499.99, 30),
    ('P007', 'Levi\'s 501 Jeans', 'Clothing', 79.99, 250),
    ('P008', 'Puma Running Shoes', 'Footwear', 99.99, 180),
    ('P009', 'Apple MacBook Pro', 'Electronics', 1999.99, 60),
    ('P010', 'Fossil Smartwatch', 'Accessories', 249.99, 100),
    ('P011', 'Ray-Ban Sunglasses', 'Accessories', 149.99, 120),
    ('P012', 'Nike Dri-FIT T-Shirt', 'Clothing', 29.99, 300),
    ('P013', 'Adidas Originals Hoodie', 'Clothing', 59.99, 200),
    ('P014', 'Samsung QLED TV', 'Electronics', 1299.99, 40),
    ('P015', 'Sony WH-1000XM4 Headphones', 'Electronics', 349.99, 90),
    ('P016', 'Under Armour Sports Shoes', 'Footwear', 89.99, 220),
    ('P017', 'Calvin Klein Perfume', 'Beauty', 79.99, 150),
    ('P018', 'Tommy Hilfiger Polo Shirt', 'Clothing', 49.99, 180),
    ('P019', 'Apple iPad Air', 'Electronics', 599.99, 80),
    ('P020', 'Skechers Memory Foam Shoes', 'Footwear', 69.99, 250),
    ('P021', 'Levi\'s Denim Jacket', 'Clothing', 89.99, 120),
    ('P022', 'Bose SoundLink Speaker', 'Electronics', 199.99, 100),
    ('P023', 'Puma Sports Bag', 'Accessories', 49.99, 200),
    ('P024', 'Nike Yoga Mat', 'Sports', 39.99, 150),
    ('P025', 'Adidas Training Gloves', 'Sports', 29.99, 180),
    ('P026', 'Apple AirPods Pro', 'Electronics', 249.99, 100),
    ('P027', 'Fossil Leather Watch', 'Accessories', 149.99, 90),
    ('P028', 'Ray-Ban Aviator Sunglasses', 'Accessories', 169.99, 80),
    ('P029', 'Nike Running Shorts', 'Clothing', 34.99, 220),
    ('P030', 'Adidas Soccer Ball', 'Sports', 24.99, 200)
]

customers_data = [
    ('C001', 'Rajesh Patel', 'North', 5000.00),
    ('C002', 'Priya Sharma', 'South', 7500.00),
    ('C003', 'Mohan Singh', 'East', 4200.00),
    ('C004', 'Sanjana Reddy', 'West', 6800.00),
    ('C005', 'Amit Verma', 'North', 3900.00),
    ('C006', 'Divya Gupta', 'South', 9200.00),
    ('C007', 'Rahul Mehta', 'East', 5600.00),
    ('C008', 'Neha Patel', 'West', 7100.00),
    ('C009', 'Vikram Chopra', 'North', 4800.00),
    ('C010', 'Shweta Nair', 'South', 6300.00),
    ('C011', 'Ankit Shah', 'East', 5200.00),
    ('C012', 'Pooja Desai', 'West', 8900.00),
    ('C013', 'Rohit Kulkarni', 'North', 6500.00),
    ('C014', 'Priyanka Sharma', 'South', 7800.00),
    ('C015', 'Aakash Patel', 'East', 4500.00),
    ('C016', 'Neha Gupta', 'West', 6200.00),
    ('C017', 'Siddharth Menon', 'North', 5800.00),
    ('C018', 'Aishwarya Rao', 'South', 9500.00),
    ('C019', 'Varun Mehta', 'East', 7300.00),
    ('C020', 'Sneha Verma', 'West', 5400.00),
    ('C021', 'Arjun Singh', 'North', 6900.00),
    ('C022', 'Kavya Reddy', 'South', 8200.00),
    ('C023', 'Ravi Patel', 'East', 4900.00),
    ('C024', 'Deepika Shah', 'West', 7600.00),
    ('C025', 'Nikhil Chopra', 'North', 6100.00),
    ('C026', 'Sonali Nair', 'South', 8500.00),
    ('C027', 'Gaurav Desai', 'East', 5700.00),
    ('C028', 'Manisha Kulkarni', 'West', 7200.00),
    ('C029', 'Ajay Sharma', 'North', 6700.00),
    ('C030', 'Shalini Gupta', 'South', 9100.00)
]

employees_data = [
    ('E001', 'Amit Patel', 'Sales', 65000.00),
    ('E002', 'Priya Singh', 'Marketing', 72000.00),
    ('E003', 'Rahul Sharma', 'Engineering', 85000.00),
    ('E004', 'Neha Verma', 'Sales', 68000.00),
    ('E005', 'Rajesh Gupta', 'Marketing', 75000.00),
    ('E006', 'Sneha Reddy', 'Engineering', 82000.00),
    ('E007', 'Vikram Mehta', 'Sales', 71000.00),
    ('E008', 'Sanjana Patel', 'Marketing', 69000.00),
    ('E009', 'Aakash Shah', 'Engineering', 88000.00),
    ('E010', 'Divya Chopra', 'Sales', 66000.00),
    ('E011', 'Rohit Nair', 'Marketing', 74000.00),
    ('E012', 'Shweta Kulkarni', 'Engineering', 79000.00),
    ('E013', 'Ankit Desai', 'Sales', 67000.00),
    ('E014', 'Pooja Sharma', 'Marketing', 73000.00),
    ('E015', 'Siddharth Patel', 'Engineering', 84000.00),
    ('E016', 'Aishwarya Singh', 'Sales', 70000.00),
    ('E017', 'Varun Gupta', 'Marketing', 76000.00),
    ('E018', 'Kavya Reddy', 'Engineering', 81000.00),
    ('E019', 'Ravi Mehta', 'Sales', 69000.00),
    ('E020', 'Deepika Patel', 'Marketing', 78000.00),
    ('E021', 'Nikhil Shah', 'Engineering', 86000.00),
    ('E022', 'Sonali Chopra', 'Sales', 72000.00),
    ('E023', 'Gaurav Nair', 'Marketing', 75000.00),
    ('E024', 'Manisha Kulkarni', 'Engineering', 83000.00),
    ('E025', 'Ajay Desai', 'Sales', 68000.00),
    ('E026', 'Shalini Sharma', 'Marketing', 77000.00),
    ('E027', 'Arjun Patel', 'Engineering', 80000.00),
    ('E028', 'Priyanka Singh', 'Sales', 71000.00),
    ('E029', 'Mohan Gupta', 'Marketing', 74000.00),
    ('E030', 'Neha Reddy', 'Engineering', 87000.00)
]

conn.executemany('INSERT INTO sales VALUES (?, ?, ?, ?, ?)', sales_data)
conn.executemany('INSERT INTO customers VALUES (?, ?, ?, ?)', customers_data)
conn.executemany('INSERT INTO employees VALUES (?, ?, ?, ?)', employees_data)

conn.commit()
conn.close()