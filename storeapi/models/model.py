from flask_restful import reqparse
import re
import sys
import os.path
import database_file
from passlib.hash import pbkdf2_sha256 as sha256
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")


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
    def get_user_by_username(username):
        dict_cursor.execute("SELECT * FROM store_users WHERE \
        username = %s ", (username, ))
        return dict_cursor.fetchone()

    def create_user(self):
        return cursor.execute("INSERT INTO store_users (name, username, password, isAdmin) \
         VALUES (%s, %s, %s, %s)", (self.name, self.username, User.generate_hash(self.password), self.isAdmin))
     
    def get_all_users(self):
        dict_cursor.execute("SELECT * FROM store_users")
        return dict_cursor.fetchall()

    @staticmethod
    def parse():
        parser = reqparse.RequestParser()
        parser.add_argument('FirstName', help='This field cannot be left blank', required=True)
        parser.add_argument('Username', help='This field cannot be left blank', required=True)
        parser.add_argument('Password', help='This field cannot be left blank', required=True) 
        parser.add_argument('isAdmin', help='This field cannot be left blank', required=True)
        data=parser.parse_args()
        return data

    def validate_data_type(self):
        return  isinstance(self.name, str) or isinstance(self.username, str)
    
    def search_special_characters(self):
        regex = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')  
        return (regex.search(self.username)) or (regex.search(self.name))

    def check_empty_fields(self):
        if self.name == "" or self.username == "" or not self.password or self.isAdmin == "":
            return True  

    def check_field_numeric(self):
        regex = re.compile(r'[0-9]')
        return regex.search(self.name) 
           
    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password,hash):
        return sha256.verify(password,hash)

    def check_empty_space(self):
       if re.search(r'[\s]', self.name) or re.search(r'[\s]', self.username) or re.search(r'[\s]', self.password)  or re.search(r'[\s]', self.isAdmin):
          return True
