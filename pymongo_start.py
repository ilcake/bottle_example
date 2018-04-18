import pymongo
from pymongo import MongoClient

# connect to database
connection = MongoClient('localhost', 27017)

db = connection.test

#handle to names collection

item = db.names.find_one()

print(item)
print(item['name'])
