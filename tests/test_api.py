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
           data=json.dumps(dict(Username='lia', Password='1234'))
        )

        self.store_attendant_login_response = self.client.post(
           "/api/v2/auth/login",
           content_type='application/json',
           data=json.dumps(dict(Username='john', Password='pwd'))
        )
        
    def register_users(self):
        admin = User("lia","lilian","1234","True")
        attendant = User("john","john","pwd","False")
        admin.create_user()
        attendant.create_user()

    def test_admin_login(self):
        self.assertEqual(self.admin_login_response.status_code, 200)
    
    def test_store_attendant_login(self):
        self.assertEqual(self.store_attendant_login_response.status_code, 200)

    def test_user_registered(self):
        token=(json.loads(self.admin_login_response.data))['Access_token']
        response = self.client.post("/api/v2/auth/signup",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+ token),
                                 data=json.dumps(dict(Username="goerge", FirstName="joe",Password="1234",isAdmin="True"),)   
                             )
        self.assertEqual(response.status_code,201)   

        self.assertEqual((json.loads(response.data))['Message'],"New account created" ) 
        self.assertEqual((json.loads(response.data))['User'],{ "Username": "goerge", "FirstName": "joe" }) 
                                           
    def test_get_specific_item(self):
        """
           method to get a specific item
        """
        token=(json.loads(self.admin_login_response.data))['Access_token']
        response = self.client.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+ token),
                                 data=json.dumps(dict(Name="Hp", Quantity=15,Price=2000,Min_quantity =33,Category="laptop"))   
                             )   
                             
        self.assertEqual(response.status_code, 201) 

        get_result = self.client.get('/api/v2/product/1', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token))
        self.assertEqual(get_result.status_code, 200)


    def test_get_non_existant_item(self) :  
        """
           method to test an item that does not exist
        """
        token=(json.loads(self.admin_login_response.data))['Access_token']
        get_result = self.client.get('/api/v2/product/10000', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token))
        self.assertEqual(get_result.status_code, 404)

    def test_get_all_products(self):
        """
           method to get all products
        """
        token=(json.loads(self.admin_login_response.data))['Access_token']
        response = self.client.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+ token),
                                 data=json.dumps(dict(Name="Hp", Quantity=15,Price=2000,Min_quantity =33,Category="laptop"))   
                             )   
                             
        self.assertEqual(response.status_code, 201) 

        get_result = self.client.get('/api/v2/products')
        response = json.loads(get_result.data.decode("utf8"))
        self.assertEqual(get_result.status_code, 200)
        self.assertIsInstance(response, dict)

    def test_add_product(self):
        """
           method to add a specific product
        """  
        token=(json.loads(self.admin_login_response.data))['Access_token']
        response = self.client.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+ token),
                                 data=json.dumps(dict(Name="Hp", Quantity=33,Price=2000,Min_quantity =15,Category="laptop"))   
                             )                                        
        self.assertEqual(response.status_code, 201)

        self.assertEqual((json.loads(response.data))['Message'],"Product added to stock" )
        self.assertEqual((json.loads(response.data))['Product'],{ "Name": "Hp", "Price": "2000" })
    
    def test_add_product_with_empty_name(self):
        """
           method to add a product with empty name
        """  
        token=(json.loads(self.admin_login_response.data))['Access_token']
        post_result = self.client.post('api/v2/products', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token),
                                         data=json.dumps(dict(Name="", Quantity=30, Price=5000000, Min_quantity=10, Category="laptop")))
        self.assertEqual(post_result.status_code, 400)    
        self.assertEqual((json.loads(post_result.data))["Error"],"Field empty field detected, make sure all fields have values")

    def test_add_product_with_special_characters(self):
        """
           method to add a product with empty name
        """  
        token=(json.loads(self.admin_login_response.data))['Access_token']
        post_result = self.client.post('api/v2/products', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token),
                                         data=json.dumps(dict(Name="#hp", Quantity=30, Price=5000000, Min_quantity=10, Category="laptop")))
        self.assertEqual(post_result.status_code, 400)         
        self.assertEqual((json.loads(post_result.data))["Error"],"No string should contain special characters")

    def test_get_specific_sale(self):
        """
           method to get a specific sale
        """
        token=(json.loads(self.admin_login_response.data))['Access_token']
        response = self.client.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+ token),
                                 data=json.dumps(dict(Name="Hp", Quantity=33,Price=2000,Min_quantity =15,Category="laptop"))   
                             )                                        
        self.assertEqual(response.status_code, 201)
        self.assertEqual((json.loads(response.data))['Message'],"Product added to stock" )
        self.assertEqual((json.loads(response.data))['Product'],{ "Name": "Hp", "Price": "2000" })

        token=(json.loads(self.store_attendant_login_response.data))['Access_token']
        post_result = self.client.post('/api/v2/sales', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token),
                                         data=json.dumps(dict(Name="Hp", Quantity=10, Date='16/10/2018')))
        self.assertEqual(post_result.status_code, 201)
        self.assertEqual((json.loads(post_result.data))['Message'], "Sale record created")
        self.assertEqual((json.loads(post_result.data))['Product'], { "Name": "Hp", "Price": 20000})

        token=(json.loads(self.admin_login_response.data))['Access_token']
        get_result = self.client.get('/api/v2/sale/1', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token))
        self.assertEqual(get_result.status_code, 200)
   
    def test_get_all_sales(self):
        """
           method to get all sales
        """
        token=(json.loads(self.admin_login_response.data))['Access_token']
        get_result = self.client.get('/api/v2/sales', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token))
        self.assertEqual(get_result.status_code, 200)

    def test_add_sale(self):
        """
           method to add specific sale
        """  
        token=(json.loads(self.admin_login_response.data))['Access_token']
        response = self.client.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+ token),
                                 data=json.dumps(dict(Name="Hp", Quantity=33,Price=2000,Min_quantity =15,Category="laptop"))   
                             )                                        
        self.assertEqual(response.status_code, 201)
        self.assertEqual((json.loads(response.data))['Message'],"Product added to stock" )
        self.assertEqual((json.loads(response.data))['Product'],{ "Name": "Hp", "Price": "2000" })

        token=(json.loads(self.store_attendant_login_response.data))['Access_token']
        post_result = self.client.post('/api/v2/sales', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token),
                                         data=json.dumps(dict(Name="Hp", Quantity=10, Date='16/10/2018')))
        self.assertEqual(post_result.status_code, 201)
        self.assertEqual((json.loads(post_result.data))['Message'], "Sale record created")
        self.assertEqual((json.loads(post_result.data))['Product'], { "Name": "Hp", "Price": 20000})

    def test_empty_sale(self):
        """
           method to add specific sale
        """  
        token=(json.loads(self.store_attendant_login_response.data))['Access_token']
        post_result = self.client.post('/api/v2/sales', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token),
                                         data=json.dumps(dict(Name="", Quantity=30, Date='16/10/2018')))

        self.assertEqual((json.loads(post_result.data))['Error'],"Field empty field detected, make sure all fields have values")
        self.assertEqual(post_result.status_code,400)

    def test_add_sale_with_special_characters(self):
        """
           method to add a product with empty name
        """  
        token=(json.loads(self.store_attendant_login_response.data))['Access_token']
        post_result = self.client.post('api/v2/sales', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token),
                                         data=json.dumps(dict(Name="#hp", Quantity=30, Date='16/10/2018')))
        self.assertEqual(post_result.status_code, 400)         
        self.assertEqual((json.loads(post_result.data))["Error"],"No string should contain special characters")  
  
    def test_modify_product(self):
        """
           method to modify specific sale
        """  
        token=(json.loads(self.admin_login_response.data))['Access_token']
        response = self.client.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+ token),
                                 data=json.dumps(dict(Name="Hp", Quantity=33,Price=2000,Min_quantity =15,Category="laptop"))   
                             )                                        
        self.assertEqual(response.status_code, 201)

        token=(json.loads(self.admin_login_response.data))['Access_token']
        response = self.client.put("/api/v2/product/1",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+ token),
                                 data=json.dumps(dict(Name="Hp", Quantity=50,Price=3000,Min_quantity =15,Category="laptop"))   
                             )                                        
        self.assertEqual(response.status_code, 202)
        self.assertEqual((json.loads(response.data))['Message'],  "Product updated")
        self.assertEqual((json.loads(response.data))['Product'], {"Name": "Hp", "Quantity": "50", "Price": "3000", "Min_Quantity": "15", "Category": "laptop"})  

    def test_update_product_with_empty_name(self):
        """
           method to add a product with empty name
        """  
        token=(json.loads(self.admin_login_response.data))['Access_token']
        post_result = self.client.put('api/v2/product/1', content_type = 'application/json', headers=dict(Authorization='Bearer '+ token),
                                         data=json.dumps(dict(Name="", Quantity=30, Price=5000000, Min_quantity=10, Category="laptop")))
        self.assertEqual(post_result.status_code, 400)    
        self.assertEqual((json.loads(post_result.data))["Error"],"Field empty field detected, make sure all fields have values")

    def test_delete_product(self):
        """
           method to delete a specific sale
        """    
        token=(json.loads(self.admin_login_response.data))['Access_token']
        response = self.client.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+ token),
                                 data=json.dumps(dict(Name="Hp", Quantity=33,Price=2000,Min_quantity =15,Category="laptop"))   
                             )                                        
        self.assertEqual(response.status_code, 201)

        delete_result = self.client.delete('/api/v2/product/1', content_type = 'application/json', headers=dict(Authorization='Bearer '))
        self.assertEqual(delete_result.status_code, 200)   

def tearDown(self):
        db = DatabaseConnection()
        db.drop_table('store_users')
        db.drop_table('products')
        db.drop_table('sales')
