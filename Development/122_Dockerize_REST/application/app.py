from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
import application

app = Flask(__name__)
application.app = app
cors_whitelist = ["http://localhost:8080"]
CORS(app, origins=cors_whitelist)

@app.route('/', methods=['GET'])
def index_get():
    return "Hello"

@app.route('/', methods=['POST'])
def index_post():
    return jsonify(
        message="World"
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
