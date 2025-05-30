#Mongodb CRUD, aggregation, indexing

# from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import MongoClient

uri = "mongodb+srv://Bisma_Portfolio:Bisma123@cluster0.r1tthak.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
print("got client")
def access_mongo():
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        
        #Get DB
        db = client["Bisma_portfolio"]
        # if not db:            
        #     print("Can't fetch DB")
        #     return
        #Get collection
        chatbot_collection = db["chatbot"]

        # if not chatbot_collection:
        #     print("can't fetch collection")
        #     return
        # data = (chatbot_collection.insert_one({'prompt':"Nothing, You tell", 'response':"I am coding"}))
        # print('updated')
        data = data = chatbot_collection.update_one({'prompt':{'$regex': 'nothing', '$options':'i'}}, {'$set':{'response': "I am enjoying coding"}})
        # chatbot_collection.delete_one({'prompt':{'$regex':"nothing", '$options':'i'}})
        if not data:
            print("can't get data from collection")
            return
        print("Data", data)
    except Exception as e:
        print(e)
        return

access_mongo()
