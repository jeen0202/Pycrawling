from flask import Flask
import requests

app = Flask(__name__)

#error handler 기능
@app.errorhandler(404)
def page_not_found(error) :
    return "<h1>해당 경로에 맞는 페이지가 업습니다. 관리자에게 연락주세요.</h1>", 404

@app.route('/google')
def get_google():
    res = requests.get('http://wwww.google.com')
    return res.text

if __name__ == "__main__":
    app.run(host="localhost",port="8085",debug=True)