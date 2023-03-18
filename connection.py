from pymongo import MongoClient

client = MongoClient("mongodb+srv://<user>:<567234>@mongodb.x4pxdoh.mongodb.net/?retryWrites=true&w=majority")
db = client.web9

if __name__ == '__main__':
    r = db.quotes.find()
    print(r)