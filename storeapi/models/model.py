products = []
sales = []


class ProductModel:
    def __init__(self,name,quantity,price,min_quantity,category):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.min_quantity = min_quantity
        self.category = category
