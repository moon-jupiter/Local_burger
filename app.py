from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index_boot.html')

@app.route('/number', methods=['GET'])
def draw_graph():
    graph_indexs = list(db.localburger.find({},{'_id':0}))
    return jsonify({'result': 'success', 'data': graph_indexs})


#burgerking
@app.route('/number', methods=['POST'])
def search_number():
    address_receive = request.form['address_give']

    #string 자르기
    split_address = address_receive.split(" ")

    address0 = split_address[0]
    address1 = split_address[1]
    address2 = split_address[2]

    search_address = list(db.localburger.find({'$and':[{'address0': address0}, {'address1': address1}]},{'_id':0}))
    if len(search_address) == 1: 
        search_burgerking = search_address[0]['king']
        search_rank = search_address[0]['rank']
        search_number = search_address[0]['number']
        search_people = search_address[0]['people']
        result_address = address0 + ' ' + address1
    else:
        search_temp = db.localburger.find_one({'address2': address2})
        search_burgerking = search_temp['king']
        search_rank = search_temp['rank']
        search_number = search_temp['number']
        search_people = search_temp['people']
        result_address = address0 + ' ' + address1 + ' ' + address2

    return jsonify({
        'result': 'success','king': search_burgerking, 'rank': search_rank, 'number': search_number, 'people': search_people, 'address': result_address
        })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)