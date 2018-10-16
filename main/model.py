from flask_restful import Resource, Api
from instance import app

api = Api(app)
products = []
sales = []

class Product(Resource):
    def post(self, name):
        product = {'name':name,'quantity':30,'price':2000000,'min_quantity':10,'category':'laptop'}
        products.append(product)
        return product ,201