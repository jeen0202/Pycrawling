from flask import Flask
import requests

app = Flask(__name__)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler( #logging handler 선언
        'sejing_server.log',maxBytes=2000,backupCount=10)
    file_handler.setLevel(logging.WARNING) #loggin level 설정
    app.logger.addHandler(file_handler)

    @app.errorhandler(404)
    def page_not_found(error):
        app.logger.error(error)
        return '<h1>해당 경로에 맞는 웹 페이지가 없습니다. 문제가 지속되면, 관리자에게 연락해주세요</h1>',404

    if __name__ == "__main__":
        app.run(host='localhost', port='8085')