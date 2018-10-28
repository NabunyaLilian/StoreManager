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

            if ('name' in data and 'quantity' in data and 'price' in data and 'date' in data and 'store_attendant' in data):
                if (name != "" and quantity != "" and price != "" and date != "" and store_attendant != ""):
                    if validate(string_data,int_data) == True :
                            sale = {'sale_id':len(sales) +1, 'name': name, 'quantity':quantity, 'price':price, 'date':date, 'store_attendant':store_attendant}
                            sales.append(sale)
                            return sale, 201
                    return {"message":"Enter the right data type values please"}, 400
                return {"Error":"Field empty, make sure all the fields have values"}, 400        
            return {'Error':'Missing field, make sure you have; name, quantity, price, min_quantity and category'}, 400     
                   