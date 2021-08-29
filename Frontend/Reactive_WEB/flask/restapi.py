from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
import requests #html load를 위한 library
from bs4 import BeautifulSoup # parsing을 위한 library

app = Flask(__name__)
CORS(app)

@app.route('/news',methods=['GET','POST'])
def news():
    res = requests.get('https://news.naver.com',
    headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(res.content, 'html.parser')
    myData = soup.find(class_ ='lnk_hdline_article') 

    #print(myData.string)
    news_data = dict()
    news_data['info'] = myData.string
    news_data['status'] = True
    #print(news_data)
    if request.method == "POST":
        print("POST")
        data = request.get_json()
        #print(data)
        print(data['email'])
    if request.method == 'GET':
        print("GET")
        user = request.args.get('email')
        print(user)

    return make_response(jsonify(news_data), 200)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8085")