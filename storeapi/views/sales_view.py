"""
   A file for defining sales view resource
"""
from flask import request
from flask_restful import Resource
from storeapi.models.model import sales
from storeapi.views.validation import validate

class Sales(Resource):
    """
       class for the sale resource
    """
    def get(self):
        """
           get all sales method
        """
        return {'sales':sales}
    def post(self):
        """
           method to create a sale
        """
        if request.content_type == 'application/json':
            data = request.get_json()
            name = data.get('name')
            quantity = data.get('quantity')
            price = data.get('price')
            date = data.get('date')
            store_attendant = data.get('store_attendant')
            string_data = [name, store_attendant, date]
            int_data = [quantity, price]

            if validate(string_data,int_data) == True :
                    sale = {'sale_id':len(sales) +1, 'name': name, 'quantity':quantity, 'price':price, 'date':date, 'store_attendant':store_attendant}
                    sales.append(sale)
                    return sale, 201
            return {"message":"Enter valid values please"}
