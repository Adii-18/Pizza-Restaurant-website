from pymongo import MongoClient


def get_database():
    headers = {
		'Access-Control-Request-Headers': '*',
		'api-key': 'Idfkj9Oq9mZ23dZkDjhJDe9Sin0FOhjG4pR9Jl0bXCrIKEqrOT2PgScLRFek7kvl',
	}
    doc_info = {'message': 'My new message',
	'status':'pending'
	}
    json_data = {
		'collection': 'Messages',
		'database': 'Restaurant',
		'dataSource': 'Cluster0',
		'document': doc_info
	}
	
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "https://data.mongodb-api.com/app/data-aipuo/endpoint/data/v1/action/insertOne"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['user_shopping_list']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    dbname = get_database()