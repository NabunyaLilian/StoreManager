"""
   A file for defining products list view resource
"""
from flask import request
from flask_restful import Resource
from storeapi.models.model import products
from storeapi.views.validation import validate
import uuid

class ProductList(Resource):
    """
       class for product list
    """
    def get(self):
        """
        method to get all products
        """
        return {'products': products}
    def post(self):
        """
        method to create a product
        """
        if request.content_type == 'application/json':
                data = request.get_json()
                name = data.get('name')
                quantity = data.get('quantity')
                price = data.get('price')
                min_quantity = data.get('min_quantity')
                category = data.get('category')
                string_data = [name, category]
                int_data = [quantity, price, min_quantity]

                if validate(string_data,int_data) == True :
                    product = {'product_id': len(products) +1 , 'name': name, 'quantity':quantity, 'price':price, 'min_quantity':min_quantity, 'category': category}
                    products.append(product)
                    return product, 201
                return {"message":"Enter valid values please"}, 400
    
    