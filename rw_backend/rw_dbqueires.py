import rw_dbconnect as cn

#.list_database_names are built in mongo feature
mongocl = cn.connect()
#print(mongocl.list_database_names())
mydb = mongocl["sample_list"]
#print(mydb.list_collection_names())
mywlist = mydb["watch_list"]


def full_list():
    # count number of items in collections 
    count = mywlist.count_documents({})
    f_list=[]
    for x in range(count):
        # need to remove _id key as it turns item into an non iterable object
        # print(mywlist.find()[x])
        lit = mywlist.find()[x]
        del lit['_id']
        f_list.append(lit)
        print(lit)
    return f_list

def get_names():
    #db.collection.distinct('x') <= how to get values from keys with specific id
    names = mywlist.distinct('name')
    return names




# full_list()
# get_names()

