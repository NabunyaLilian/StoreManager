from flask import request
from flask_restful import Resource
from storeapi.models.model import sales
 

class Sales(Resource):
    def get(self):
        return {'sales':sales}

    def post(self):
        data = request.get_json()
        sale = {'sale_id':len(sales) +1,'name':data['name'],'quantity':data['quantity'],'price':data['price'],'date':data['date'],'store_attendant': data['store_attendant']}
        sales.append(sale)
        return sale ,201  
