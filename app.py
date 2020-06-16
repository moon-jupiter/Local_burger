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
    if len(search_address) == 1: #바로 위 find()로 찾은 값의 개수가 1개라는 걸 표현하고 싶은데 어떻게 하면 좋을까요?
        search_burgerking = search_address['king']
    else:
        search_burgerking_temp = db.localburger.find_one({'address2': address2})
        search_burgerking = search_burgerking_temp['king']
        print(search_burgerking)
    return jsonify({'result': 'success'},{'number': search_burgerking})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)