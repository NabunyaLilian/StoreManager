import psycopg2
from psycopg2.extras import RealDictCursor
import os


class DatabaseConnection:
    def __init__(self):

        try:
            if os.getenv('APP_SETTINGS') == "testing":
                dbname = 'testdb'
                username = 'postgres'
                pwd = 'password'
                host = 'localhost'
                port = '5433'
            elif os.getenv('heroku') == "database":
                dbname = 'dao0hl0ucpa2te'
                username = 'cegdozynwqmytn'
                pwd = 'dfe0316e32339f8fc71e4b9d3b7fd3bc308fd3d89efd86c1d0d480f759e91090'
                host = 'ec2-54-225-115-234.compute-1.amazonaws.com'
                port = '5432'
            else:
                dbname = 'storedb'
                username = 'postgres'
                pwd = 'password'
                host = 'localhost'
                port = '5433'
            self.conn = psycopg2.connect(database=dbname, user= username, password=pwd, host=host, port= port)
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            self.dict_cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            # print(dbname)

        except(Exception):
            print("can not connect successfully")

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
                price INTEGER NOT NULL, date VARCHAR(30) NOT NULL, user_id INTEGER REFERENCES store_users ON UPDATE CASCADE ON DELETE CASCADE )"""
        self.cursor.execute(query)
        return "sales table created"

    def drop_table(self, table_name):
        query = "DROP TABLE IF EXISTS " + table_name + " cascade"
        self.cursor.execute(query)
        return "table"

