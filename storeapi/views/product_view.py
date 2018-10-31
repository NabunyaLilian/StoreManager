"""
   A file for defining product_view resource
"""
from flask_restful import Resource
from storeapi.models.products import Products

class Product(Resource):
    """
       class for product resource
    """
    def get(self, product_id):
        """
           method to get a specific product
        """
        pass