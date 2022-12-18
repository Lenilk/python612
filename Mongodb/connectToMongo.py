import pymongo
import datetime
# Connect to the database
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Get a reference to the database
db = client["python"]

# Get a reference to the collection
collection = db["test"]

#insert document to mongodb
document = {"name": "John", "age": 30,"date":datetime.datetime.utcnow()}

# result = collection.insert_one(document)
print(db.list_collection_names)