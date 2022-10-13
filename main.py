from flask import Flask, request, jsonify, Response
import requests
import redis
from rq import Worker, Queue, Connection
from pymongo import MongoClient
import json

app = Flask(__name__)

order_id='order1'
message='new message'
message_id='1'
order='Pizza'

@app.route('/getorders/'+order_id , methods=['GET'])
def addNewOrder():
	doc_info = {'orders': [order]}
	print('Order Added')
	return jsonify({'data': doc_info})


@app.route('/messages/'+message_id , methods=['GET'])
def addNewMessage():
	doc_info = {'message': message,
	'status':'pending'
	}

	print('Message Sent')
	return Response(json.dumps(doc_info),mimetype='application/json')
	return jsonify({'data': doc_info})


#task = [task for task in tasks if task['id'] == task_id]


@app.route('/getorders', methods=['GET'])
def addOrder():
	doc_info = {'orderIDs': order_id}

	print('Order added')
	return jsonify({'data': doc_info})



@app.route('/welcome', methods=['GET'])
def welcome():
	data = 'Welcome to Pizza House'
	return jsonify({'data': data})


if __name__ == '__main__':
	message=input('Write a new message: ')
	order=input('Item: ')
	app.run(debug=True)


