from flask import Flask
from flask import jsonify
from flask import request
from stats import AAPDonationStats

application = Flask(__name__)

@application.route("/", methods=['GET'])
def sample():
    return jsonify({'test': 'sample'})

@application.route("/get_state_with_num_of_donations")
def get_state_with_num_of_donations():

    aap = AAPDonationStats()
    result = aap.get_state_with_num_of_donations()
    return jsonify({'result': result})

@application.route("/get_n_persons_with_top_donations", methods=['POST'])
def get_n_persons_with_top_donations():

    n = request.args.get('n', 5)

    aap = AAPDonationStats()
    result = aap.get_n_persons_with_top_donations(int(n))
    return jsonify({'result': result})

@application.errorhandler(404)
def page_not_found(error):
    return jsonify({'ERROR': 404})

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8082)