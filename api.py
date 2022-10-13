import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/getorders' , methods=['GET'])
def addOrder():
    doc_info = {'orderIDs': ['Pizza1', 'Pizza2']}
    return jsonify({'data': doc_info})


headers = {
    'Access-Control-Request-Headers': '*',
    'api-key': 'Idfkj9Oq9mZ23dZkDjhJDe9Sin0FOhjG4pR9Jl0bXCrIKEqrOT2PgScLRFek7kvl',
}

doc_info = {'orderIDs': ['Pizza1', 'Pizza3']}

json_data = {
    'collection': 'Orders',
    'database': 'Restaurant',
    'dataSource': 'Cluster0',
    'document': doc_info
}

response = requests.post('https://data.mongodb-api.com/app/data-aipuo/endpoint/data/v1/action/insertOne', headers=headers, json=json_data)
print('status',response.status_code)
if response.status_code == 200:
    app.run(debug=True)
    print('api added')

