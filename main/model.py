from flask_restful import Resource, Api
from instance import app

api = Api(app)
products = []
sales = []

class Sales(Resource):
    def get(self):
        return {'sales':sales}
