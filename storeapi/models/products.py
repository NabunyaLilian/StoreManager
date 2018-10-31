import psycopg2
from flask_restful import reqparse
import re
import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
import database_file
from passlib.hash import pbkdf2_sha256 as sha256


db = database_file.DatabaseConnection()
cursor = db.cursor
dict_cursor = db.dict_cursor

class Products:

    def __init__(self,name,quantity,price,min_quantity,category):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.min_quantity = min_quantity
        self.category = category
        self.db = database_file.DatabaseConnection()
        self.dict_cursor = self.db.dict_cursor
        self.cursor = self.db.cursor
          
    def create_product(self):
        query = """ INSERT INTO products (name,quantity,price,min_quantity,category) VALUES ('{}','{}','{}','{}','{}')""".format(self.name,self.quantity,self.price,self.min_quantity,self.category) 
        self.dict_cursor.execute(query)
        return True
      
    def get_product_by_username(self,product_id):

        query = "SELECT * FROM products WHERE product = %d "
        self.dict_cursor.execute(query, [product_id])
        row = self.dict_cursor.fetchone()
        return row
    
    def update_products(self,product_id):
        query = "UPDATE products SET name ='{}', quantity = '{}', price ='{}', min_quantity ='{}', category = '{}' where product_id ='{}'".format(self.name,self.quantity,self.price,self.min_quantity,self.category,product_id) 
        dict_cursor.execute(query)
        return True

    @staticmethod
    def delete_product(product_id):
        query = "DELETE from products WHERE product_id = '{}'".format(product_id)
        dict_cursor.execute(query)
        return True
        
    @staticmethod    
    def get_product_by_id(product_id):
        query = """ SELECT * FROM products WHERE product_id = {} """ .format(product_id)
        dict_cursor.execute(query)
        row = dict_cursor.fetchone()
        return row

    @staticmethod
    def get_all_products():
        query = "SELECT * FROM products"
        dict_cursor.execute(query)
        all = dict_cursor.fetchall()
        return all

    @staticmethod
    def parse():
        parser = reqparse.RequestParser()
        parser.add_argument('name', help ='This field cannot be left blank', required = True)
        parser.add_argument('price', help ='This field cannot be left blank', required = True)
        parser.add_argument('quantity', help ='This field cannot be left blank', required = True) 
        parser.add_argument('min_quantity', help ='This field cannot be left blank', required = True)   
        parser.add_argument('category', help ='This field cannot be left blank', required = True)   
        data = parser.parse_args() 
        return data
    
    def validate_data_type(self):
        a = [self.name, self.price, self.quantity, self.min_quantity, self.category]
        if all(isinstance(x, str) for x in a): 
           return True
    
    def search_special_characters(self):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') #creates a regular expression object to be used in matching
        if (regex.search(self.name) == None) and (regex.search(self.category) == None):       
            return True  
        else:
            return False  

    def check_empty_fields(self):
        if self.name == "" or  self.quantity == "" or  self.price == "" or self.min_quantity == "" or self.category == "":
            return True    

    def check_field_numeric(self):
        regex = re.compile('[0-9]')
        if (regex.search(self.name) == None):
            return True   
        else:
            return False   
    def check_empty_space(self):
        if  (re.search['\s'],self.name != None) or (re.search['\s'],self.quantity != None) or (re.search['\s'],self.price != None) or (re.search['\s'],self.min_quantity != None) or (re.search['\s'],self.category != None) :
            return 