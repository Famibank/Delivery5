import collections
import pymongo

client = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0.diqaz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE')

db = client['test-database'] #a database
collection = db['test-collection']

# we check if the customer is in our collection

CPR_input = input('Write down the CPR: ')

find_query = { "CPR" : (CPR_input) }
mydoc = collection.find(find_query)

for x in mydoc:
    print(x)



'''
# prints first one
x = collection.find_one()
print(x)


# print all

for x in collection.find():
  print(x)

'''
