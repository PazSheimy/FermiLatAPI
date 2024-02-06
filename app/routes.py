from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def test_route():
    return jsonify({"message": "LAT API Test Successful"})
