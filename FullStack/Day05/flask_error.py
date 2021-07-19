from flask import Flask
import requests

app = Flask(__name__)

#error handler 기능
@app.errorhandler(404)
def page_not_found(error) :
    return "<h1>404 Error</h1>", 404

@app.route('/google')
def get_google():
    res = requests.get('http://wwww.google.com')
    return res.text

if __name__ == "__main__":
    app.run(host="localhost",port="8085")