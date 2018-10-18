from flask import request
from flask_restful import Resource
from storeapi.models.model import sales


class Sale(Resource):
    def get(self, sale_id):
        for sale in sales:
            if sale['sale_id'] == sale_id:
                return sale
        return {'sale': None}, 404

    