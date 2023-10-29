import rw_dbconnect as rwc




#Get all items from watchlist
def getList ():
    watchlist = rwc.wlist()
    print( type (watchlist))
    return(watchlist)

# getList()

