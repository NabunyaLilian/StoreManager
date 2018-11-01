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


class Sale:
    def __init__(self,name,quantiy,price,date) :
        self.name = name
        self.quantity = quantiy
        self.price = price
        self.date = date
        self.db = database_file.DatabaseConnection()
        self.dict_cursor = self.db.dict_cursor
        self.cursor = self.db.cursor

    def create_sale(self) :
        query = "INSERT INTO sales (name, quantity, price, date) VALUES ('{}', '{}','{}','{}')".format(self.name,self.quantity,self.price,self.date)
        self.cursor.execute(query)
        return True

    @staticmethod
    def get_all_sales() :
        query = "SELECT * FROM sales"
        dict_cursor.execute(query)
        all = dict_cursor.fetchall()
        return all

    @staticmethod
    def parse() :
        parser = reqparse.RequestParser()
        parser.add_argument('name', help ='This field cannot be left blank', required = True)
        parser.add_argument('quantity', help ='This field cannot be left blank', required = True)
        parser.add_argument('price', help ='This field cannot be left blank', required = True)
        parser.add_argument('date', help ='This field cannot be left blank', required = True)
        data = parser.parse_args()
        return data

    @staticmethod  
    def get_sale_by_id(sale_id) :
        query_string = "SELECT * FROM sales WHERE sale_id = '{}'".format(sale_id)
        dict_cursor.execute(query_string)
        row = dict_cursor.fetchone()
        return row

    def validate_data_type(self) :
        a = [self.name,self.date]
        b = [self.quantity, self.price]
        if all(isinstance(x, str) for x in a) and all(isinstance(x, int) for x in b) :
           return True
    
    def search_special_characters(self):
        regex = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]') #creates a regular expression object to be used in matching
        if (regex.search(self.name) == None):       
            return True  
        else:
            return False          

    def check_empty_fields(self):
        if self.name == "" or  self.quantity == "" or  self.price == "" or self.date == "" :
            return True

    def check_field_numeric(self):
        regex = re.compile(r'[0-9]')
        if (regex.search(self.name) == None) :
            return True 
        else:
            return False

    def check_empty_space(self) :
        if  re.search(r'[\s]',self.name) or re.search(r'[\s]',self.quantity) or re.search(r'[\s]',self.price)  or re.search(r'[\s]',self.date) :
            return True

    