# should run on any other computer than Mac
from pymongo import MongoClient
import random
import pyinputplus as pyip
from getpass import getpass

client = MongoClient(
    'mongodb+srv://admin:admin@cluster0.diqaz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE')
# was missing SSL certificate for y computer, that's why the addition at the end of the MngoDB connection URI

db = client['test-database']  # a database
collection = db['test-collection']  # like a folder for more documents

class Account:
    def register(self):
        cpr = pyip.inputNum("CPR to register\n", min=999999999, max=9999999999)
        password_db = getpass(prompt="Password?\n") # fix password, only allows int
        full_name = pyip.inputStr(prompt="Full Name?\n", blank=True)
        bank_account_number = random.randint(1000000, 99999999)  # need to make so user gets assigned one after registering
        balance = random.rand
        user = {"CPR": cpr,
                "password": password_db,
                "full_name": full_name,
                "bank_account_number": bank_account_number
                "balance": balance} # can add more things like balance, email, gender. phone nr, remember to dd variables asking for them
        collection.insert_one(user)

    def login(self):
        login_name = input('What is your login CPR?\n')
        user = collection.find_one({'CPR': int(login_name)})#connect to CPR collection in mongo, already found user, no need to test if CPR is correct
        if not user:
            print('User not found')
            return False
        user_password = getpass('What is your login password?\n')

        if user["password"] == user_password:
            return True
        return False
