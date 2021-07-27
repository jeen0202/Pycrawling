from flask import Flask, jsonify, request, render_template, make_response
#Flask : 서버
#jsonify, request, make_response : REST
#render_template : html 분리
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
# 로그인 세션 관리를 위한 모듈들
from flask_cors import CORS
import os
# https만을 지원하는 기능을 http에서 test하기 위한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

from blog_view import blog
from blog_control.user_mgmt import User

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secret_key = 'sejing_server1'

#blueprint 등록
app.register_blueprint(blog.blog_abtest, url_prefix='/blog')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False),401)

if __name__ == '__main__':
    app.run(host='localhost',port ='8085', debug=True)

