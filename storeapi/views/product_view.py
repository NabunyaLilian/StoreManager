"""
   A file for defining product_view resource
"""
from flask_restful import Resource
from storeapi.models.model import products

class Product(Resource):
    """
       class for product resource
    """
    def get(self, product_id):
        """
           method to get a specific product
        """
        product = next(filter(lambda x: x['product_id'] == product_id, products), None)
        return {'product': product}, 200 if product else 404
    def put(self):
        