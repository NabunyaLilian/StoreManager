from flask_restful import reqparse
import re
import sys
import os.path
import database_file
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")


db = database_file.DatabaseConnection()
cursor = db.cursor
dict_cursor = db.dict_cursor


class Products:

    def __init__(self, name, quantity, price, min_quantity, category):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.min_quantity = min_quantity
        self.category = category

    def create_product(self):
        cursor.execute(""" INSERT INTO products (name, quantity, price, min_quantity, category)
                       VALUES (%s, %s,%s,%s,%s)""",
                       (self.name, self.quantity, self.price,
                        self.min_quantity, self.category))
        return True

    def update_products(self, product_id):
        dict_cursor.execute("UPDATE products SET name = %s, quantity = %s, price = %s, min_quantity = %s, category = %s \
        where product_id = %s", (self.name, self.quantity, self.price, self.min_quantity, self.category, product_id))
        return True

    @staticmethod
    def delete_product(product_id):
        return dict_cursor.execute("DELETE from products WHERE product_id = %s ", (product_id, ))

    @staticmethod
    def get_product_by_id(product_id):
        dict_cursor.execute(""" SELECT * FROM products WHERE product_id = %s """, (product_id, ))
        return dict_cursor.fetchone()

    @staticmethod
    def get_all_products():
        dict_cursor.execute("SELECT * FROM products")
        return dict_cursor.fetchall()

    @staticmethod
    def parse():
        parser = reqparse.RequestParser()
        parser.add_argument('name', help='This field cannot be left blank', required=True)
        parser.add_argument('price', help='This field cannot be left blank', required=True)
        parser.add_argument('quantity', help='This field cannot be left blank', required=True)
        parser.add_argument('min_quantity', help='This field cannot be left blank', required=True)
        parser.add_argument('category', help='This field cannot be left blank', required=True)
        data = parser.parse_args()
        return data

    def validate_data_type(self):
        return isinstance(self.name, str) or isinstance(self.category, str)

    def search_special_characters(self):
        regex = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
        return (regex.search(self.name)) or (regex.search(self.category))

    def check_empty_fields(self):
        if self.name == "" or not self.quantity or not self.price or not self.min_quantity or self.category == "":
            return True

    def check_field_numeric(self):
        regex = re.compile(r'[0-9]')
        return regex.search(self.name)

    def check_empty_space(self):
        if re.search(r'[\s]', self.name) or re.search(r'[\s]', self.quantity) or re.search(r'[\s]', self.price) or re.search(r'[\s]', self.min_quantity) or re.search(r'[\s]', self.category):
            return True
