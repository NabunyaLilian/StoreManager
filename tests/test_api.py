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
        reply = json.loads(response.data)
        print(reply)
        self.assertEqual(response.status_code,201)   
                      
        
    def test_get_specific_item(self):
        """
           method to get a specific item
        """
        token=(json.loads(self.admin_login_response.data))['access_token']
        response = self.client.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+ token),
                                 data=json.dumps(dict(name="Hp", quantity=15,price=2000,min_quantity =33,category="laptop"))   
                             )   
             
        print (response.data)                 
        self.assertEqual(response.status_code, 201) 

        # get_result = self.client.get('/api/v2/product/1', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token))
        # self.assertEqual(get_result.status_code, 200)


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
        print(response.data)                     
        self.assertEqual(response.status_code, 201)   
        # json_data = json.loads(response.data)      
        # assert json_data (user['name']) == "Hp"
        # assert json_data['quantity'] == 15
        # assert json_data['price'] == 2000
        # assert json_data['min_quantity'] == 33
        # assert json_data['category'] == "laptop"
    
    def test_add_product_with_empty_name(self):
        """
           method to add a product with empty name
        """  
        token=(json.loads(self.admin_login_response.data))['access_token']
        post_result = self.client.post('api/v2/products', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token),
                                         data=json.dumps(dict(name="", quantity=30, price=5000000, min_quantity=10, category="laptop")))
        self.assertEqual(post_result.status_code, 400)     

    def test_get_specific_sale(self):
        """
           method to get a specific sale
        """
        token=(json.loads(self.admin_login_response.data))['access_token']
        get_result = self.client.get('/api/v2/sale/1', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token))
        self.assertEqual(get_result.status_code, 200)
        
    # def test_get_non_existant_sale(self) :  
    #     """
    #        method to test an item that does not exist
    #     """
    #     token=(json.loads(self.admin_login_response.data))['access_token']
    #     get_result = self.client.get('/api/v2/sale/100' , content_type = 'application/json', headers=dict(Authorization='Bearer '+ token))
    #     self.assertEqual(get_result.status_code, 404)

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
        self.assertEqual(post_result.status_code, 201)                    
    #     json_data = json.loads(post_result.data)      
    #     assert json_data['name'] == "HP"
    #     assert json_data['quantity'] == 30
    #     assert json_data['price'] == 500000
    #     assert json_data['date'] == "16/10/2018"
    #     assert json_data['store_attendant'] == "John"
def tearDown(self):
        db = DatabaseConnection()
        db.drop_table('store_users')
        db.drop_table('products')
        db.drop_table('sales')
