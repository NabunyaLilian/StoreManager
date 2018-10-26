from flask_restful import Resource
def check_id(id_ , list_ ,index_label):
   for x in list_ :
        if x[index_label] == id_:
            return 'item exists'
        else:
            return False
