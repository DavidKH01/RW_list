import pymongo
#turn mongodb connection into a module to be used

def connect():
    #allow variable to be used outside of function
    global client

    #code copied from mongobd connect
    from pymongo.mongo_client import MongoClient

    # if it wont connect, check that mongodb has the correct IP address listed 
    uri = "mongodb+srv://danny:0@cluster0.hgtihbs.mongodb.net/?retryWrites=true&w=majority"
    # uri = "mongodb+srv://danny:0@cluster0.hgtihbs.mongodb.net/"

    # Create a new client and connect to the server
    client = MongoClient(uri)

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)


