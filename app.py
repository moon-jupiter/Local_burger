from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

#burgerking
@app.route('/number', methods=['POST'])
def search_number():
    address_receive = request.form['address_give']

    #string 자르기
    split_address = address_receive.split(" ")

    address0 = split_address[0]
    address1 = split_address[1]
    address2 = split_address[2]

    search_address = db.localburger.find({'$and':[{'address0': address0}, {'address1': address1}]})
    # if search_address.count() == 1: 
    #     search_burgerking = search_address['king']
    # else:
    #     search_burgerking_temp = db.localburger.find_one({'address2': address2})
    #     search_burgerking = search_burgerking_temp['king']
    search_result = list(search_address)
    search_burgerking = search_result[0].get('king', None)
    search_percent = search_result[0].get('percent', None)
    return jsonify({
        'result': 'success','number': search_burgerking, 'percent': search_percent
        })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)