import requests
from flask import Flask, Response, request, jsonify

app = Flask(__name__)
BASE_URL = "http://127.0.0.1:5000/drones"
drone = {
    "drone_index": {
        "model": "DJI Phantom",
        "battery": 100,
        "control_url": "http://127.0.0.1:8080/"
    }
}


@app.route("/takeoff", methods=["POST"])
def takeoff():
    altitude = request.json.get('altitude')
    #
    print(f"Взлетаем на высоту: {altitude}")
    return jsonify({
        'message': f"Успешно набрана высота: {altitude}"
    }), 200


@app.route("/drones", methods=["POST"])
def register_drone(drone_id, drone_info):
    url = BASE_URL
    payload = {
        "drone_id": drone_id,
        **drone_info
    }
    response = requests.post(url, json=payload)
    return response.json()


if __name__ == '__main__':
    drone_id = "drone_index"
    drone_info = drone[drone_id]
    response = register_drone(drone_id, drone_info)
    print(f"Соединяемся с сервером: {response.get('message')}")
    app.run(port=8080, debug=True)
