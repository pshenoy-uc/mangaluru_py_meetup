from flask import Flask
from flask import jsonify
from flask import request

application = Flask(__name__)

@application.route("/", methods=['GET'])
def sample():
    return jsonify({'test': 'sample'})

@application.route("/test")
def test():
    return "Hello"

@application.errorhandler(404)
def page_not_found(error):
    return jsonify({'ERROR': 404})

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8082)