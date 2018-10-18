from flask import request
from flask_restful import Resource
from storeapi.models.model import products

class Product(Resource):
    def get(self, product_id):
        product = next(filter(lambda x: x['product_id'] == product_id , products), None) 
        return {'product': product}, 200 if product else 404        
    