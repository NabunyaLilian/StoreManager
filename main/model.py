from flask_restful import Resource, Api
from instance import app

api = Api(app)
products = []
sales = []

class ProductList(Resource):
    def get(self):
        return {'products': products}    
    