"""
   A file for running the server
"""
from storeapi import app
from storeapi.models.products import Products


if __name__ == "__main__":
    product_dict = Products.get_product_by_name('Toshiba')
    # pdt_id = product_dict['product_id']
    print (product_dict)
    app.run(debug = True)
    
