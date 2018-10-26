products = []
sales = []

users = [{'Id':1,'username':'Lia','password':'pwd', 'isadmin':'true'},

         {'Id':2, 'username':'Jane','password':'web','isadmin':'false'}
]

def auth(usrname,password):
    for usr in users:
        if usr['username']==username and usr['password']==password and usr['isadmin']=="true":
            

