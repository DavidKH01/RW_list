# dotenv syntax for python
# pip install python-dotenv
import os
from dotenv import load_dotenv, find_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


#turn mongodb connection into a module to be used
def connect():
    #allow variable to be used outside of function
    global client

    #code copied from mongobd connect
    from pymongo.mongo_client import MongoClient

    # if it wont connect, check that mongodb has the correct IP address listed 
    uri = os.getenv("mongodb_uri")
    # uri = removed...check .env"

    # Create a new client and connect to the server
    client = MongoClient(uri)

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)


def wlist():

    #.list_database_names are built in mongo feature
    mongocl = connect()
    #print(mongocl.list_database_names())
    mydb = mongocl["sample_list"]
    #print(mydb.list_collection_names())
    mywlist = mydb["watch_list"]


    res = []    
    for x in mywlist.find():
        # need to remove _id key as it turns item into an non iterable object
        x.pop('_id')

        for key, value in x.items():
            print(f"{key}: {value}")
            res.append(f"{key}: {value}")
    else:
        print('Else statement')
        print(res)
        return (res)
   
   
#wlist()