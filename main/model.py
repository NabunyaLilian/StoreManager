from flask_restful import Resource, Api
from instance import app

api = Api(app)
products = []
sales = []

class Product(Resource):
    def get(self, name):
        for product in products:
            if product['name'] == name:
                return product
        return {'product': None}, 404       
    