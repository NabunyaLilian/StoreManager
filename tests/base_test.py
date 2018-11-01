from unittest import TestCase
from flask import json
from storeapi.config import app_configuration 
from storeapi import app
from storeapi.database_file import DatabaseConnection
from storeapi.models.model import User
from flask_jwt_extended import create_access_token
import datetime


class BaseTestCase(TestCase):
    """
       Class to test api
    """ 
    
    def setUp(self):
        app.config = ["testing"]
        db = DatabaseConnection()
        self.create_user_table = db.create_table_store_users()
        self.create_products_table = db.create_products_table()
        self.create_sales_table = db.create_sales_table()
        self.app = app
        self.client = self.app.test_client
        self.register_users()

    def tearDown(self):
        pass

    def register_users(self):
        admin = User("lia","lilian","1234","true")
        attendant = User("john","john","pwd","false")
        admin.create_user()
        attendant.create_user()
    
    def admin_login(self):
        response = self.client().post(
            "/api/v2/auth/login",
            content_type='application/json',
            data=json.dumps(dict(user_name='lia', password='1234'))
        )
        reply = json.loads(response.data)
        return reply
        
    def attendant_login(self):
        response = self.client().post(
            "/api/v2/auth/login",
            content_type='application/json',
            data=json.dumps(dict(user_name='john', password='pwd'))
        )
        reply = json.loads(response.data)
        return reply
        