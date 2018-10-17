from flask_restful import Resource, Api
from instance import app

api = Api(app)
products = []
sales = []

class Sale(Resource):
    def post(self, name):
        sale = {'name':name,'quantity':30,'price':500000,'date':'16/10/2018','store_attendant':'John'}
        sales.append(sale)
        return sale ,201    