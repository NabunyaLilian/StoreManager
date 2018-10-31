import psycopg2
from psycopg2.extras import RealDictCursor

class DatabaseConnection:
    def __init__(self):
        self.conn = psycopg2.connect(database="testdb", user="postgres", password="password", host="localhost", port="5433")
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        self.dict_cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        print("connected yesssssssssssssssss")


    def create_table_store_users(self):

        query = """ CREATE TABLE IF NOT EXISTS store_users( user_id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL ,isAdmin VARCHAR(10) NOT NULL)"""
        self.cursor.execute(query)
        return "table created successfully"


    def create_products_table(self):
        query = """ CREATE TABLE IF NOT EXISTS products (
                product_id  SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, quantity INTEGER NOT NULL,
                price INTEGER NOT NULL, min_quantity INTEGER, category VARCHAR(50) NOT NULL
                )"""
        self.cursor.execute(query)
        return "products table created"

    def create_sales_table(self):
        query = """ CREATE TABLE IF NOT EXISTS sales (
                sale_id  SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, quantity INTEGER NOT NULL,
                price INTEGER NOT NULL, date VARCHAR(30) NOT NULL, product_id INTEGER REFERENCES products ON UPDATE CASCADE ON DELETE CASCADE ,user_id INTEGER REFERENCES store_users ON UPDATE CASCADE ON DELETE CASCADE )"""
        self.cursor.execute(query)
        return "sales table created"    
db = DatabaseConnection()
db.create_table_store_users()
db.create_products_table()
db.create_sales_table()