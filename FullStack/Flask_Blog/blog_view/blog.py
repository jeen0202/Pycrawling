from flask import Flask, Blueprint, request, render_template,jsonify,make_response,redirect,url_for
from flask.helpers import make_response

blog_abtest = Blueprint('blog', __name__)

@blog_abtest.route('/set_email', methods=['GET','POST'])
def set_email():
    if request.method == "GET":
        print(request.headers)
        print('set_email', request.args.get('user_email'))
    else:
        print(request.headers)
        print('set_email', request.form['user_email'])
        # content tyhpe 이 application/json 일경우 get_json()
    return redirect('/blog/test')

@blog_abtest.route('/test')
def test():
    return render_template('blog_A.html')