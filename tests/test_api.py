"""A module for testing"""
from unittest import TestCase
from flask import json
from storeapi.config import app_configuration 
from storeapi import app
from storeapi.database_file import DatabaseConnection
from tests.base_test import BaseTestCase


class Tests(BaseTestCase):
    """
       Class to test api
    """ 
    
    def test_get_specific_item(self):
        """
           method to get a specific item
        """
        admin_status = self.admin_login()
        response = self.client().post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_status['access_token']),
                                 data=json.dumps(dict(name="Hp", quantity=15,price=2000,min_quantity =33,category="laptop"),)   
                             )
        get_result = self.client().get('/api/v2/product/1', content_type = 'application/json', headers=dict(Authorization='Bearer '+admin_status['access_token']), )
        self.assertEqual(get_result.status_code, 200)


    def test_get_non_existant_item(self) :  
        """
           method to test an item that does not exist
        """
        get_result = self.client().get('/api/v2/product/10000')
        self.assertEqual(get_result.status_code, 404)

    def test_get_all_products(self):
        """
           method to get all products
        """
        get_result = self.client().get('/api/v2/products')
        response = json.loads(get_result.data.decode("utf8"))
        self.assertEqual(get_result.status_code, 200)
        self.assertIsInstance(response, dict)

    def test_add_product(self):
        """
           method to add a specific product
        """  
        post_result = self.client().post('/api/v2/products', content_type='application/json',
                                         data=json.dumps(dict(name="HP", quantity=30, price=2000000, min_quantity=10, category="laptop")))
 
        self.assertEqual(post_result.status_code, 201)   
        json_data = json.loads(post_result.data)      
        assert json_data['name'] == "HP"
        assert json_data['quantity'] == 30
        assert json_data['price'] == 2000000
        assert json_data['min_quantity'] == 10
        assert json_data['category'] == "laptop"
    
    def test_add_product_with_empty_name(self):
        """
           method to add a product with empty name
        """  
        post_result = self.client().post('api/v2/products', content_type = 'application/json',
                                         data=json.dumps(dict(name="", quantity=30, price=5000000, min_quantity=10, category="laptop")))
        self.assertEqual(post_result.status_code, 400)     

    def test_get_specific_sale(self):
        """
           method to get a specific sale
        """
        get_result = self.client().get('/api/v2/sale/1')
        self.assertEqual(get_result.status_code, 200)
        
    def test_get_non_existant_sale(self) :  
        """
           method to test an item that does not exist
        """
        get_result = self.client().get('/api/v2/sale/TOSHIBA')
        self.assertEqual(get_result.status_code, 404)

    def test_get_all_sales(self):
        """
           method to get all sales
        """
        get_result = self.client().get('/api/v2/sales')
        self.assertEqual(get_result.status_code, 200)

    def test_add_sale(self):
        """
           method to add specific sale
        """  
        post_result = self.client().post('/api/v2/sales', content_type='application/json',
                                         data=json.dumps(dict(name="HP", quantity=30, price=500000, date='16/10/2018', store_attendant='John')))
        self.assertEqual(post_result.status_code, 201)                    
        json_data = json.loads(post_result.data)      
        assert json_data['name'] == "HP"
        assert json_data['quantity'] == 30
        assert json_data['price'] == 500000
        assert json_data['date'] == "16/10/2018"
        assert json_data['store_attendant'] == "John"
