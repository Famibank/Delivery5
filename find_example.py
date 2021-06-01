import pymongo

client = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0.diqaz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE')

db = client['test-database'] #a database
collection = db['test-collection']

x = collection.find_one()
print(x)


'''
# print all

for x in collection.find():
  print(x)

'''
