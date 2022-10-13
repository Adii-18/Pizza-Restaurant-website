from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

order_id='order1'
newOrder = ['Pizza1', 'Pizza2']

@app.route('/getorders/'+order_id , methods=['GET'])
def addNewOrder():
	headers = {
		'Access-Control-Request-Headers': '*',
		'api-key': 'Idfkj9Oq9mZ23dZkDjhJDe9Sin0FOhjG4pR9Jl0bXCrIKEqrOT2PgScLRFek7kvl',
	}
	doc_info = {'orderIDs': newOrder}
	json_data = {
		'collection': 'Orders',
		'database': 'Restaurant',
		'dataSource': 'Cluster0',
		'document': doc_info
	}
	return jsonify({'data': doc_info})


#task = [task for task in tasks if task['id'] == task_id]


@app.route('/getorders', methods=['GET'])
def addOrder():
	headers = {
		'Access-Control-Request-Headers': '*',
		'api-key': 'Idfkj9Oq9mZ23dZkDjhJDe9Sin0FOhjG4pR9Jl0bXCrIKEqrOT2PgScLRFek7kvl',
	}
	doc_info = {'orderIDs': ['Pizza1', 'Pizza2']}
	json_data = {
		'collection': 'Orders',
		'database': 'Restaurant',
		'dataSource': 'Cluster0',
		'document': doc_info
	}

	print('api added')
	return jsonify({'data': doc_info})



@app.route('/welcome', methods=['GET'])
def welcome():
	data = 'Welcome to Pizza House'
	return jsonify({'data': data})


if __name__ == '__main__':
	app.run(debug=True)


