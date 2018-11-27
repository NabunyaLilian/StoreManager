"""
   A file for defining sales view resource
"""
from flask_restful import Resource
from storeapi.models.sale import Sale
from flask_jwt_extended import jwt_required, get_jwt_identity
from storeapi.models.products import Products


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
        if user_identity['admin_status'] == 'True':
            sales = Sale.get_all_sales()
            return {'Sales': sales}
        return {"Error": "You have no prior access to this resource"}

    @jwt_required
    def post(self):
        """
           method to create a sale
        """
        data = Sale.parse()
        name = data['Name'].lower()
        quantity = data['Quantity']
        date = data['Date'].lower()
        sale_obj = Sale(name, quantity, date)
        user_identity = get_jwt_identity()
        if user_identity['admin_status'] == 'True':
            return {"Error": "Access denied"}, 401
        if sale_obj.check_empty_fields():
            return {"Error": "Field empty field detected, make sure all fields have values"}, 400
        if not sale_obj.search_special_characters():
            return {"Error": "No string should contain special characters"}, 400
        if not sale_obj.check_field_numeric():
                return {"Error": "Name should not contain numbers"}, 400
        if sale_obj.check_empty_space():
                return {"Error": "Space detected in one of the fields"}, 400

        if  int(quantity) > 0 :
            product_dict = Products.get_product_by_name(name)
            pdt_id = product_dict['product_id']
            qty_dict = Products.get_quantity_by_id(pdt_id)
            min_qty = qty_dict['min_quantity']
            qty = qty_dict['quantity']
            price = product_dict['price']
            new_price = price * int(quantity)
            if qty >= int(quantity):
                new_qty = qty - int(quantity)
                min_qty = qty_dict['min_quantity']
                if new_qty > min_qty:

                    Products.update_product(new_qty, pdt_id)
                    person_id = user_identity['user_id']
                    sale = sale_obj.create_sale(person_id, new_price)
                    if sale:
                        response = {
                                            "Message": "Sale record created",
                                            "Product": {
                                                "Name": data['Name'],
                                                "Price": new_price}
                                        }, 201
                        return response
                    else:
                        return {'Error': 'Something went wrong'}, 400
                else:
                   return {'Message':'Product out of stock'}, 400   
            else:
                return {'Messsage':'Product quantity less in stock'}, 400         
        else :
           return {'Error':'Only positive numbers allowed!'}, 400