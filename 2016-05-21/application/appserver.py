from flask import Flask
application = Flask(__name__)
from flask import jsonify
from flask import request

@application.route("/", methods=['GET'])
def sample():
    return jsonify({'test': 'sample'})

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'ERROR': 404})

if __name__ == "__main__":
    application.run(host='0.0.0.0')