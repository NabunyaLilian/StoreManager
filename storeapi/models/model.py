import psycopg2
from passlib.hash import pbkdf2_sha256 as sha256
from flask_restful import reqparse
import re
import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
import database_file
from passlib.hash import pbkdf2_sha256 as sha256


class User:

    def __init__(self,username,name,password,isAdmin):
        self.name = name
        self.username = username
        self.password = password
        self.isAdmin = isAdmin
        self.db = database_file.DatabaseConnection()
        self.dict_cursor = self.db.dict_cursor
        self.cursor = self.db.cursor
          
    def get_user_by_username(self):

        query = "SELECT * FROM store_users WHERE username = %s "
        self.dict_cursor.execute(query, [self.username])
        row = self.dict_cursor.fetchone()
        return row

    def create_user(self):
        query = "INSERT INTO store_users (name,username,password,isAdmin) VALUES ('{}', '{}','{}','{}')".format(self.name,self.username,self.password,self.isAdmin)
        self.cursor.execute(query)
        return True

    def get_all_users(self):
        query = "SELECT * FROM store_users"
        self.dict_cursor.execute(query)
        all = self.dict_cursor.fetchall()
        return all

    @staticmethod
    def parse():
        parser = reqparse.RequestParser()
        parser.add_argument('name', help ='This field cannot be left blank', required = True)
        parser.add_argument('username', help ='This field cannot be left blank', required = True)
        parser.add_argument('password', help ='This field cannot be left blank', required = True) 
        parser.add_argument('isAdmin', help ='This field cannot be left blank', required = True)   
        data = parser.parse_args() 
        return data
    
    def validate_data_type(self):
        a = [self.name,self.username, self.isAdmin]
        if all(isinstance(x, str) for x in a): 
           return True
    
    def search_special_characters(self):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') #creates a regular expression object to be used in matching
        if(regex.search(self.username) == None): 
            print("Username is accepted")     
        else:  
            print("Username not accepted.") 
        if(regex.search(self.name) == None):
            print("Name is accepted")  
        else:
            print("Name not accepted")      
        return True    

    def check_empty_fields(self):
        if self.name != "" and  self.username != "" and  self.password != "" and self.isAdmin != "":
            return True    

    def check_field_numeric(self):
        if self.name.isnumeric:
            return True      

    def generate_hash(self):
        return sha256.hash(self.password)


    def verify_hash(self,hash):
        return sha256.verify(self.password,hash)
       