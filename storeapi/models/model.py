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

    @staticmethod   
    def get_user_by_username(username) :
        dict_cursor.execute("SELECT * FROM store_users WHERE username = %s ", (username,))
        return  dict_cursor.fetchone()

    def create_user(self) :
        cursor.execute("INSERT INTO store_users (name,username,password,isadmin) VALUES (%s,%s,%s,%s)", (self.name, self.username, User.generate_hash(self.password), self.isAdmin))
        return True

    @staticmethod
    def parse() :
        parser = reqparse.RequestParser()
        parser.add_argument('name', help = 'This field cannot be left blank', required = True)
        parser.add_argument('username', help = 'This field cannot be left blank', required = True)
        parser.add_argument('password', help = 'This field cannot be left blank', required = True) 
        parser.add_argument('isAdmin', help = 'This field cannot be left blank', required = True)
        return parser.parse_args()
    
    def validate_data_type(self) :
        return isinstance(self.name, str) or  not isinstance(self.username, str)
            
    def search_special_characters(self) :
        regex = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]') 
        return regex.search(self.username) or regex.search(self.name) 
            
    def check_empty_fields(self):
        if self.name == "" or self.username == "" or not self.password or self.isAdmin == "" :
            return True  

    def check_field_numeric(self) :
        regex = re.compile(r'[0-9]')
        return  regex.search(self.name)
            
    @staticmethod
    def generate_hash(password) :
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password,hash) :
        return sha256.verify(password, hash)

    def check_empty_space(self) :
        return re.search(r'[\s]', self.name) or re.search(r'[\s]', self.username) or re.search(r'[\s]', self.password)  or re.search(r'[\s]', self.isAdmin) 
             
