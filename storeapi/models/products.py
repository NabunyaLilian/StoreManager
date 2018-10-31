import psycopg2
from flask_restful import reqparse
import re
import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
import database_file
from passlib.hash import pbkdf2_sha256 as sha256

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

    def get_all_products(self):
        query = "SELECT * FROM products"
        self.dict_cursor.execute(query)
        all = self.dict_cursor.fetchall()
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
        if(regex.search(self.name) == None): 
            print("name is accepted")     
        else:  
            print("name not accepted.") 
        if(regex.search(self.category) == None):
            print("category is accepted")  
        else:
            print("category not accepted")      
        return True    

    def check_empty_fields(self):
        if self.name != "" and  self.quantity != "" and  self.price != "" and self.min_quantity != "" and self.category != "":
            return True    

    def check_field_numeric(self):
        if self.name.isnumeric:
            return True      

   