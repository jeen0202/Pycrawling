from flask import Flask,request,make_response, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app) # CORS 무시를 위해사용
@app.route('/test',methods=['GET','POST','PUT','DELETE'])
def test():
    if request.method =='POST':
        print('POST')
        data = request.get_json()
        print(data['email'])
    elif request.method == 'GET':
        print('GET')
        user = request.args.get('email')
        print(user)
    elif request.method == 'PUT':
        print('PUT')
        user = request.args.get('email')
        print(user)
    elif request.method == 'DELETE':
        print('DELETE')
        user = request.args.get('email')
        print(user)
    return make_response(jsonify({'status':True}),200)

if __name__== '__main__':
    app.run(host="localhost",port='8085')