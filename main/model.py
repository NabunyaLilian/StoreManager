from flask_restful import Resource, Api
from instance import app

api = Api(app)
products = []
sales = []

class Sale(Resource):
    def get(self, name):
        for sale in sales:
            if sale['name'] == name:
                return sale
        return {'sale': None}, 404       
    