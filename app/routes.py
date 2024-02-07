#routes.py
from flask import Blueprint, jsonify, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
def test_route():
    return jsonify({"message": "LAT API Test Successful"})

# Add a route for displaying the form
@main.route('/form')
def form():
    return render_template('form.html')


@main.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    object_name = request.form.get('objectname')
    coordinates = request.form.get('coordinates')
    search_radius = request.form.get('search_radius')
    observation_dates = request.form.get('observation_dates')
    time_system = request.form.get('time_system')
    energy_range = request.form.get('energy_range')
    lat_data_type = request.form.get('lat_data_type')
    include_spacecraft = 'includeSpacecraft' in request.form
    
    # Construct a response dict
    response_data = {
        "object_name": object_name,
        "coordinates": coordinates,
        "search_radius": search_radius,
        "observation_dates": observation_dates,
        "time_system": time_system,
        "energy_range": energy_range,
        "lat_data_type": lat_data_type,
        "include_spacecraft": include_spacecraft
    }
    
    # Process data here (e.g., query your database or API with these parameters)
    # This part of your code would contain the logic for handling the query based on the form data
    
    # Return the response with the form data and any query results or statuses you need to include
    return jsonify(response_data)