from flask import Flask,render_template
import requests

app = Flask(__name__)

@app.route('/google')
def get_google():
    res = requests.get('http://google.co.kr')
    return res.text
    

if (__name__ == '__main__'):
    app.run(host="localhost",port="8085")