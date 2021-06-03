# should run on any other computer
import time # used to create a pause between prompts
from pymongo import MongoClient #for MongoDB
import random #later used to assign random bank_account_number and balance
import pyinputplus as pyip #for the inputs for register function
from getpass import getpass # for password

client = MongoClient(
    'mongodb+srv://admin:admin@cluster0.diqaz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE')
# was missing SSL certificate for Mac computer, that's why there is the addition (&ssl_cert_reqs=CERT_NONE) at the end of the MongoDB connection URI
#as well line 7&8 connect to the MongoDB through the provided URI
db = client['test-database']  # a database
collection = db['test-collection']  # like a folder for more documents

class Account:
    def register(self):
        cpr = pyip.inputNum("Enter your CPR to register:\n", min=999999999, max=9999999999) #Prompts the Client to input CPR code to register.
        password_db = getpass(prompt="Enter your password:\n") # The getpass() is used to promt the Clients for the password in a secure way.
        full_name = pyip.inputStr(prompt="Enter your Full Name:\n", blank=True) # Promts for the Client's name.
        bank_account_number = random.randint(1000000, 99999999)  # Need to make, so user gets assigned one after registering.
        balance = random.randint(1,9999) #Randomly assigns the balance for the user, not much functionality, but was made just to have something in the bank account
        user = {"CPR": cpr,  #A dictionary "user" is created to be used as a place holder... later to be filled out and inserted into MongoDB.
                "password": password_db,
                "full_name": full_name,
                "bank_account_number": bank_account_number,
                "balance": balance}
        collection.insert_one(user) #Inserts user in MongoDB.
        print("You are now registered. To continue, please log in ")
        time.sleep(4) # Creates a 4 seconds pause to the next prompt

    def login(self):
        login_name = input('What is your login CPR?\n') #Promts for the already created login_name(CPR).
        client = collection.find_one({'CPR': int(login_name)})#Connects to CPR collection in mongodb and tries to find the inputed CPR number, already found user, no need to test if CPR is correct
        if not client: #If inputed CPR cannot be found
            print('User not found')
            return False
        user_password = getpass('What is your login password?\n') #Promts for the already created password.
        if client["password"] == user_password: #Compares the password in MongoDB to the one that has been inputed.
            print('Hi,', client['full_name'], '\nYour bank account number is', client['bank_account_number'], ' \nYour balance is', client['balance'], ' DKK')
            return True
        return False