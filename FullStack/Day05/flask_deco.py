from flask import Flask
import requests

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    print("HTTP Request가 최초 있을때 실행")

@app.before_request
def before_request():
    print("HTTP Request가 있을때 마다 실행")

@app.after_request
def after_request(response):
    print("HTTP Request가 끝나고 브라우저에 응답하기 전에 실행")
    return response

@app.route('/hello')
def hello():
    print("hello")
    return "<h1>Hello Flask!</h1>"

if __name__ == '__main__':
    app.run(host='localhost', port="8085", debug=True)