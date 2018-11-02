"""A module for testing"""
from unittest import TestCase
from flask import json
from storeapi.config import app_configuration 
from storeapi import app
from storeapi.models.model import User
from storeapi.database_file import DatabaseConnection

class ApiTests(TestCase):
    """
       Class to test api
    """ 
    
    def setUp(self):
        db = DatabaseConnection()
        db.drop_table('store_users')
        db.drop_table('products')
        db.drop_table('sales')
        self.create_user_table = db.create_table_store_users()
        self.create_products_table = db.create_products_table()
        self.create_sales_table = db.create_sales_table()
        self.app = app
        self.client = app.test_client()
        self.register_users()

        self.admin_login_response = self.client.post(
           "/api/v2/auth/login",
           content_type='application/json',
           data=json.dumps(dict(username='lia', password='1234'))
        )
    
    def register_users(self):
        admin = User("lia","lilian","1234","true")
        attendant = User("john","john","pwd","false")
        admin.create_user()
        attendant.create_user()

    def test_admin_login(self):
        
        reply = json.loads(self.admin_login_response.data)
        
        self.assertEqual(self.admin_login_response.status_code, 200)

    def test_user_registered(self):
        token=(json.loads(self.admin_login_response.data))['access_token']
        response = self.client.post("/api/v2/auth/signup",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+ token),
                                 data=json.dumps(dict(Username="goerge", FirstName="joe",Password="1234",isAdmin="True"),)   
                             )
        self.assertEqual(response.status_code,201)   

        self.assertEqual((json.loads(response.data))['message'],"account created" ) 
        self.assertEqual((json.loads(response.data))['user'],{ "username": "goerge", "firstname": "joe" }) 
                                           
        
    def test_get_specific_item(self):
        """
           method to get a specific item
        """
        token=(json.loads(self.admin_login_response.data))['access_token']
        response = self.client.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+ token),
                                 data=json.dumps(dict(name="Hp", quantity=15,price=2000,min_quantity =33,category="laptop"))   
                             )   
                             
        self.assertEqual(response.status_code, 201) 

        get_result = self.client.get('/api/v2/product/1', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token))
        self.assertEqual(get_result.status_code, 200)


    def test_get_non_existant_item(self) :  
        """
           method to test an item that does not exist
        """
        token=(json.loads(self.admin_login_response.data))['access_token']
        get_result = self.client.get('/api/v2/product/10000', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token))
        self.assertEqual(get_result.status_code, 404)

    def test_get_all_products(self):
        """
           method to get all products
        """
        get_result = self.client.get('/api/v2/products')
        response = json.loads(get_result.data.decode("utf8"))
        self.assertEqual(get_result.status_code, 200)
        self.assertIsInstance(response, dict)

    def test_add_product(self):
        """
           method to add a specific product
        """  
        token=(json.loads(self.admin_login_response.data))['access_token']
        response = self.client.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+ token),
                                 data=json.dumps(dict(name="Hp", quantity=15,price=2000,min_quantity =33,category="laptop"))   
                             )                     
        self.assertEqual(response.status_code, 201)

        self.assertEqual((json.loads(response.data))['message'],"product created successfully" )
        self.assertEqual((json.loads(response.data))['user'],{ "name": "Hp", "price": "2000" })
                                   
                                     
    def test_add_product_with_empty_name(self):

        """
           method to add a product with empty name
        """  
        token=(json.loads(self.admin_login_response.data))['access_token']
        post_result = self.client.post('api/v2/products', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token),
                                         data=json.dumps(dict(name="", quantity=30, price=5000000, min_quantity=10, category="laptop")))
        self.assertEqual(post_result.status_code, 400)    
        self.assertEqual((json.loads(post_result.data))["Error"],"Field empty field detected, make sure all fields have values")
        
    def test_add_product_with_special_characters(self):
        """
           method to add a product with empty name
        """  
        token=(json.loads(self.admin_login_response.data))['access_token']
        post_result = self.client.post('api/v2/products', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token),
                                         data=json.dumps(dict(name="#hp", quantity=30, price=5000000, min_quantity=10, category="laptop")))
        self.assertEqual(post_result.status_code, 400)         
        self.assertEqual((json.loads(post_result.data))["Error"],"No string should contain special characters")

    def test_get_specific_sale(self):
        """
           method to get a specific sale
        """
        token=(json.loads(self.admin_login_response.data))['access_token']
        get_result = self.client.get('/api/v2/sale/1', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token))
        self.assertEqual(get_result.status_code, 200)
   
    def test_get_all_sales(self):
        """
           method to get all sales
        """
        token=(json.loads(self.admin_login_response.data))['access_token']
        get_result = self.client.get('/api/v2/sales', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token))
        self.assertEqual(get_result.status_code, 200)

    def test_add_sale(self):
        """
           method to add specific sale
        """  
        token=(json.loads(self.admin_login_response.data))['access_token']
        post_result = self.client.post('/api/v2/sales', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token),
                                         data=json.dumps(dict(name="HP", quantity=30, price=500000, date='16/10/2018', store_attendant='John')))

        self.assertEqual((json.loads(post_result.data))['message'],"sale record made successfully")
        (json.loads(post_result.data))['product'] == { "name": "Hp", "price": "500000" }
        
    
    def test_empty_sale(self):
        """
           method to add specific sale
        """  
        token=(json.loads(self.admin_login_response.data))['access_token']
        post_result = self.client.post('/api/v2/sales', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token),
                                         data=json.dumps(dict(name="", quantity=30, price=500000, date='16/10/2018', store_attendant='John')))

        self.assertEqual((json.loads(post_result.data))['Error'],"Field empty field detected, make sure all fields have values")
        self.assertEqual(post_result.status_code,400)
        
            
def tearDown(self):
        db = DatabaseConnection()
        db.drop_table('store_users')
        db.drop_table('products')
        db.drop_table('sales')
