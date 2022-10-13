from database import get_database
dbname = get_database()
collection_name = dbname["Orders"]

item_1 = {
  "_id": ['Pizza1', 'Pizza2']
}

collection_name.insert_many([item_1])