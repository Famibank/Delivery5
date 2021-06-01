#should run on any other computer than Mac
from pymongo import MongoClient

client = MongoClient('mongodb+srv://admin:admin@cluster0.diqaz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE')
#was missing SSL certificate for y computer, that's why the addition at the end of the MngoDB connection URI

db = client['test-database'] #a database
collection = db['test-collection']  #like a folder for more documents

cursor = collection.find({})
for document in cursor:
    print(document)



def register():
    cpr = input("CPR?")
    password_db = input("Password?")
    full_name = input("Full Name?")
    bank_account_number = input("Bank Account Number?") #need to make so user gets assigned one after registering

    user = {"CPR": cpr,
    "password": password_db,
    "full_name": full_name,
    "bank_account_number": bank_account_number}

    collection.insert_one(user)
register()


#client["test-database"]["test-collection"].insert_one(user)
