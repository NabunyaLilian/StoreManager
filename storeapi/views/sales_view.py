from flask import request
from flask_restful import Resource
from storeapi.models.model import sales
 

class Sales(Resource):
    def get(self):
        return {'sales':sales}

    def post(self):
        if request.content_type == 'application/json':
           data = request.get_json()
           name = data.get('name')
           quantity = data.get('quantity')
           price = data.get('price')
           date = data.get('date')
           store_attendant = data.get('store_attendant')
           string_data = [name,store_attendant,date] 
           int_data = [quantity,price]
        if all(isinstance(x, str) for x in string_data) and all(isinstance(x, int) for x in int_data):
            sale = {'sale_id':len(sales) +1,'name': name,'quantity':quantity,'price':price,'date':date,'store_attendant':store_attendant}
            sales.append(sale)
            return sale ,201  
        else:
            return {"message":"Enter valid values please"}   