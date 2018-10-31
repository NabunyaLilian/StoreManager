"""
   A file for defining sales view resource
"""
from flask import request
from flask_restful import Resource
from storeapi.models.sale import Sale

class Sales(Resource):
    """
       class for the sale resource
    """
    def get(self):
        """
           get all sales method
        """
        pass
    def post(self):
        """
           method to create a sale
        """
        pass