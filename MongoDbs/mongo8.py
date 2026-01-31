collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")