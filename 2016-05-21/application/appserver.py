from flask import Flask
application = Flask(__name__)
from flask import jsonify
from flask import request

@application.route("/", methods=['GET'])
def sample():
    x = request.form.get('dd')
    print request.args
    return jsonify({'test': x})

if __name__ == "__main__":
    application.run(host='0.0.0.0')