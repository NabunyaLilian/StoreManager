# from passlib.hash import pbkdf2_sha256 as sha256

# def generate_hash(password):
#     return sha256.hash(password)


# def verify_hash(password,hash):
#     return sha256.verify(password,hash)

# key = '$pbkdf2-sha256$29000$NMa4dy6F0BqDkHJuTSnF.A$ldeCnIgIn2ICWiCp/hPmMzlWv5.d63MhhzCzfq7zkyw'
# print(generate_hash('lia'))
# if verify_hash('lia',key):
#     print("you are verified")
# import re
# def search_special_characters(string):
#         regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') #creates a regular expression object to be used in matching
#         if(regex.search(string) == None): 
#             print("Username is accepted")     
#         else: 
#             print("Username not accepted.") 
# print(search_special_characters('fghhh'))   

def validate_data_type(a):
        if all(isinstance(x, str) for x in a): 
           return "all strings"
        return "validate your data"   
a = ['a','c',123]
print(validate_data_type(a))           


