import psycopg2
from passlib.hash import pbkdf2_sha256 as sha256

# products = []
# sales = []

# users = [{'Id':1,'username':'Lia','password':'pwd', 'isadmin':'true'},

#          {'Id':2, 'username':'Jane','password':'web','isadmin':'false'}
# ]

# def auth(usrname,password):
#     for usr in users:
#         if usr['username']==username and usr['password']==password and usr['isadmin']=="true":
            
class User:

    conn = psycopg2.connect(database="testdb", user = "postgres", password = "password", host = "localhost", port = "5433")

    print ("Opened database successfully")

    cur = conn.cursor()
    cur.execute('''CREATE TABLE users
        (id INT PRIMARY KEY     NOT NULL,
        name           TEXT    NOT NULL,
        username            TEXT     NOT NULL,
        password        CHAR(100)
      );''')
    print ("Table created successfully")

    conn.commit()
    conn.close()
    
    @staticmethod   
    def get_user_by_username(username):
        conn = DataBaseConnection()
        cursor = conn.dict_cursor
        query_string = "SELECT * FROM users WHERE username = %s "
        cursor.execute(query_string, [username])
        row = cursor.fetchone()
        return row

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)    

    @staticmethod
    def verify_hash(password,hash):
        return sha256.verify(password,hash)    
    