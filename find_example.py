import pymongo

client = pymongo.MongoClient('mongodb+srv://tom:parole123@banking-app-python.zfwkg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE')

db = client['test-database'] #a database
collection = db['test-collection']

x = collection.find_one()
print(x)
