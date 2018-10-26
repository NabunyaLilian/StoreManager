"""
   A file for defining product_view resource
"""
from flask_restful import Resource
from storeapi.models.model import products
from storeapi.views.check import check_id

class Product(Resource):
    """
       class for product resource
    """
    def get(self, product_id):
        """
           method to get a specific product
        """
        product = check_id(product_id , products ,'product_id') 
        if product:
           return product
        return {'message':'resource not found'},404
