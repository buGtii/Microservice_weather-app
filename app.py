from flask import Flask, request, jsonify

import requests



app = Flask(__name__)



API_KEY = "b3e1ab417695317a69597128e480d32b"  # Replace with your OpenWeatherMap API key



@app.route('/weather', methods=['GET'])

def get_weather():

    city = request.args.get('city')

    if not city:

        return jsonify({"error": "Please provide a city name"}), 400



    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    

    if response.status_code != 200:

        return jsonify({"error": "City not found"}), 404



    data = response.json()

    return jsonify({

        "city": city,

        "temperature": data['main']['temp'],

        "description": data['weather'][0]['description']

    })



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)

