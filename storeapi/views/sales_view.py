"""
   A file for defining sales view resource
"""
from flask import request
from flask_restful import Resource
from storeapi.models.sale import Sale
from flask_jwt_extended import jwt_required, get_jwt_identity


class Sales(Resource):
    """
       class for the sale resource
    """
    @jwt_required
    def get(self):
        """
           get all sales method
        """
        user_identity = get_jwt_identity()
        if user_identity['admin_status'] == 'True' :
           sales = Sale.get_all_sales()
           return sales
        return {"Error":"You have no prior access to this resource"}
    @jwt_required    
    def post(self):
        """
           method to create a sale
        """
        data = Sale.parse()
        sale_obj = Sale(data['name'],data['quantity'],data['price'],data['date'])
        user_identity = get_jwt_identity()
        if user_identity['admin_status'] == 'True':
           return {"Error":"Access denied"}
        if sale_obj.check_empty_fields() == True:
            return {"Error":"Field empty field detected, make sure all fields have values"}, 400    
        if sale_obj.search_special_characters() == False:
            return {"Error":"No string should contain special characters"},400                  
        if sale_obj.check_field_numeric() == False :
                return {"Error":"name should not contain numbers"},400 
        if sale_obj.check_empty_space():
                return {"Error":"space detected in one of the fields"},400 
                
        sale = sale_obj.create_sale()
        if sale:
            response =  {
                                "message": "sale record made successfully",
                                "user": {
                                    "name": data['name'],
                                    "price": data['price'] }
                            }, 201
            return response
        else:
            return {'error':'something went wrong'} 

