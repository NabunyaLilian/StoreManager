import psycopg2
from flask_restful import reqparse
import re
import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
import database_file
from passlib.hash import pbkdf2_sha256 as sha256

class Sale:

    def __init__(self,name,quantiy,price,date):
        self.name = name
        self.quantity = quantiy
        self.price = price
        self.date = date
        self.db = database_file.DatabaseConnection()
        self.dict_cursor = self.db.dict_cursor
        self.cursor = self.db.cursor
          
    def get_sale_by_id(self,user_id):

        query = "SELECT * FROM sales WHERE user_id = %d "
        self.dict_cursor.execute(query, [user_id])
        row = self.dict_cursor.fetchone()
        return row

    def create_sale(self):
        query = "INSERT INTO sales (name,quantity,price,date) VALUES ('{}', '{}','{}','{}')".format(self.name,self.quantity,self.price,self.date)
        self.cursor.execute(query)
        return True

    def get_all_sales(self):
        query = "SELECT * FROM sales"
        self.dict_cursor.execute(query)
        all = self.dict_cursor.fetchall()
        return all

    @staticmethod
    def parse():
        parser = reqparse.RequestParser()
        parser.add_argument('name', help ='This field cannot be left blank', required = True)
        parser.add_argument('quantity', help ='This field cannot be left blank', required = True)
        parser.add_argument('price', help ='This field cannot be left blank', required = True) 
        parser.add_argument('date', help ='This field cannot be left blank', required = True)   
        data = parser.parse_args() 
        return data
    
    def validate_data_type(self):
        a = [self.name,self.date]
        b = [self.quantity, self.price]
        if all(isinstance(x, str) for x in a) and all(isinstance(x, int) for x in b) : 
           return True
    
    def search_special_characters(self):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') #creates a regular expression object to be used in matching
        if(regex.search(self.name) == None): 
            print("name is accepted")     
        else:  
            print("name not accepted.") 

    def check_empty_fields(self):
        if self.name != "" and  self.quantity != "" and  self.price != "" and self.date != "":
            return True    

    def check_field_numeric(self):
        if self.name.isnumeric:
            return True      

    