import psycopg2
from passlib.hash import pbkdf2_sha256 as sha256
from flask_restful import reqparse
import re
import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
import database_file
from passlib.hash import pbkdf2_sha256 as sha256
from psycopg2.extras import RealDictCursor


db = database_file.DatabaseConnection()
cursor = db.cursor
dict_cursor = db.dict_cursor


class User:                                                                                                                                                                                                                                                                                                                                              

    def __init__(self, username, name, password, isAdmin):
        self.name = name
        self.username = username
        self.password = password
        self.isAdmin = isAdmin
        self.db = database_file.DatabaseConnection()
        self.dict_cursor = self.db.dict_cursor
        self.cursor = self.db.cursor

    @staticmethod   
    def get_user_by_username(username):

        query = "SELECT * FROM store_users WHERE username = %s "
        dict_cursor.execute(query, [username])
        row = dict_cursor.fetchone()
        return row

    def create_user(self):
        query = "INSERT INTO store_users (name, username, password, isAdmin) VALUES ('{}', '{}','{}','{}')".format(self.name,self.username,User.generate_hash(self.password),self.isAdmin)
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
        parser.add_argument('name', help = 'This field cannot be left blank', required = True)
        parser.add_argument('username', help = 'This field cannot be left blank', required = True)
        parser.add_argument('password', help = 'This field cannot be left blank', required = True) 
        parser.add_argument('isAdmin', help = 'This field cannot be left blank', required = True)
        data = parser.parse_args()
        return data
    
    def validate_data_type(self):
        if not isinstance(self.name, str) or  not isinstance(self.username, str):
           return True
       
    def search_special_characters(self):
        regex = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')  #creates a regular expression object to be used in matching
        if (regex.search(self.username) is None) and (regex.search(self.name) is None):
            return True
        else:
            return False

    def check_empty_fields(self):
        if self.name == "" or self.username == "" or not self.password or self.isAdmin == "":
            return True  

    def check_field_numeric(self):
        regex = re.compile(r'[0-9]')
        if (regex.search(self.name) == None):
            return True 
        else:
            return False 

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password,hash):
        return sha256.verify(password,hash)

    def check_empty_space(self):
        if  re.search(r'[\s]',self.name) or re.search(r'[\s]',self.username) or re.search(r'[\s]',self.password)  or re.search(r'[\s]',self.isAdmin) :
            return True
