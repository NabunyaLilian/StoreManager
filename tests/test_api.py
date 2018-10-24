"""A module for testing"""
from unittest import TestCase
from flask import json
from storeapi import app

class Tests(TestCase):
    """
       Class to test api
    """  
    def setUp(self):
        self.app = app
        self.client = self.app.test_client

    def test_get_specific_item(self):
        """
           method to get a specific item
        """
        # get_result = self.client().get('/api/v1/product/1')
        # self.assertEqual(get_result.status_code, 200)

    def test_get_non_existant_item(self) :  
        """
           method to test an item that does not exist
        """
        get_result = self.client().get('/api/v1/product/TOSHIBA')
        self.assertEqual(get_result.status_code, 404)

    def test_get_all_products(self):
        """
           method to get all products
        """
        get_result = self.client().get('/api/v1/products')
        response = json.loads(get_result.data.decode("utf8"))
        self.assertEqual(get_result.status_code, 200)
        self.assertIsInstance(response, dict)

    def test_add_product(self):
        """
           method to add a specific product
        """  
        post_result = self.client().post('/api/v1/products', content_type='application/json',
                                         data=json.dumps(dict(name="HP", quantity=30, price=2000000, min_quantity=10, category="laptop")))
        self.assertEqual(post_result.status_code, 201)   
        json_data = json.loads(post_result.data)      
        assert json_data['name'] == "HP"
        assert json_data['quantity'] == 30
        assert json_data['price'] == 2000000
        assert json_data['min_quantity'] == 10
        assert json_data['category'] == "laptop"

    def test_get_specific_sale(self):
        """
           method to get a specific sale
        """
        get_result = self.client().get('/api/v1/sale/1')
        self.assertEqual(get_result.status_code, 200)
        
    def test_get_non_existant_sale(self) :  
        """
           method to test an item that does not exist
        """
        get_result = self.client().get('/api/v1/sale/TOSHIBA')
        self.assertEqual(get_result.status_code, 404)

    def test_get_all_sales(self):
        """
           method to get all sales
        """
        get_result = self.client().get('/api/v1/sales')
        self.assertEqual(get_result.status_code, 200)

    def test_add_sale(self):
        """
           method to add specific sale
        """  
        post_result = self.client().post('/api/v1/sales', content_type='application/json',
                                         data=json.dumps(dict(name="HP", quantity=30, price=500000, date='16/10/2018', store_attendant='John')))
        self.assertEqual(post_result.status_code, 201)                    
        json_data = json.loads(post_result.data)      
        assert json_data['name'] == "HP"
        assert json_data['quantity'] == 30
        assert json_data['price'] == 500000
        assert json_data['date'] == "16/10/2018"
        assert json_data['store_attendant'] == "John"
