import rw_dbconnect as rwc
rwlist = rwc.wlist()



#Get all items from watchlist
def getList ():
    print( type (rwlist))
    return(rwlist)



print(rwlist['name'])












getList()

