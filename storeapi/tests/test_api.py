from unittest import TestCase
from flask import json
from storeapi import app

class Tests(TestCase):
  def setUp(self):
        self.app = app
        self.client = self.app.test_client
 
  def test_get_specific_item(self):
        get_result = self.client().get('/api/v1/product/1')
        self.assertEqual(get_result.status_code, 200)
        get_result1 = self.client().get('/api/v1/product/TOSHIBA')
        self.assertEqual(get_result1.status_code, 404)
  def test_get_all_products(self):
        get_result = self.client().get('/api/v1/products')
        self.assertEqual(get_result.status_code, 200)

  def test_add_product(self):
        post_result = self.client().post('/api/v1/products', content_type='application/json',
                                    data=json.dumps(dict(name="HP",
                                    quantity=30,price = 2000000, min_quantity = 10, category = "laptop")))
        self.assertEqual(post_result.status_code, 201)   

        json_data = json.loads(post_result.data)      
        assert json_data['name'] == "HP"
        assert json_data['quantity'] == 30
        assert json_data['price'] == 2000000
        assert json_data['min_quantity'] == 10
        assert json_data['category'] == "laptop"

  def test_get_specific_sale(self):
        get_result = self.client().get('/api/v1/sale/1')
        self.assertEqual(get_result.status_code, 200)
        get_result1 = self.client().get('/api/v1/sale/TOSHIBA')
        self.assertEqual(get_result1.status_code, 404)
  def test_get_all_sales(self):
        get_result = self.client().get('/api/v1/sales')
        self.assertEqual(get_result.status_code, 200)

  def test_add_sale(self):
        post_result = self.client().post('/api/v1/sales', content_type='application/json',
                                    data=json.dumps(dict(name = "HP",quantity = 30, price = 500000,date = '16/10/2018',store_attendant = 'John')))
        self.assertEqual(post_result.status_code, 201)                 
        
        json_data = json.loads(post_result.data)      
        assert json_data['name'] == "HP"
        assert json_data['quantity'] == 30
        assert json_data['price'] == 500000
        assert json_data['date'] == "16/10/2018"
        assert json_data['store_attendant'] == "John"