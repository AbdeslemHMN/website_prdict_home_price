from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_locations' , methods=['GET'])
def get_locations():
    response = jsonify({
        'locations': util.get_location_names(),
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_price', methods=['POST'])
def predict_price():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400
    total_sqft = float(data['total_sqft'])
    location = data['location']
    bhk = int(data['bhk'])
    bath = int(data['bath'])

    response = jsonify({
        'estimated_price': util.predict_price(location, total_sqft, bath, bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("Starting the server...")
    util.loaded_saved_artifacts()
    app.run()