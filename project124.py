from flask import Flask, jsonify, request

api = Flask(__name__)
to_do_list = [{
    'contact':'9988776655',
    'name':'Ravi',
    'done':False,
    'id':1
},
{
    'contact':'9887769565',
    'name':'Raghav',
    'done':False,
    'id':2
},
]

@api.route('/')
def contacts():
    return 'hello'

@api.route('/add-contact', methods=['POST'])
def add_contact():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'Enter Your Task'
        })

    to_do_list_empty = [{
        'contact':request.json.get('contact',''),
        'name':request.json['name'],
        'done':False,
        'id':to_do_list[-1]['id']+1
    }]

    to_do_list.append(to_do_list_empty)
    return jsonify({
        'status':'success',
        'message':'Task Has Been Added'
    })

@api.route('/get-data')
def get_data():
    return jsonify({
        'data':to_do_list
    })
if __name__ == '__main__':
    api.run(debug=True)