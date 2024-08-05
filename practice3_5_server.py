import requests
from flask import Flask, Response, request, jsonify


app = Flask(__name__)

drones = {}


@app.route("/drones", methods=["GET"])
def get_drones():
    return jsonify(drones), 200


@app.route("/drones/<drone_id>", methods=["GET"])
def get_drone(drone_id):
    drone = drones.get(drone_id)
    if drone:
        return jsonify(drones), 200
    return jsonify({
        "error": f"Дрон с ID{drone_id} не найден"
    }), 404


@app.route("/drones", methods=["POST"])
def create_drone():
    drone_id = request.json.get("drone_id")
    if drone_id:
        drones[drone_id] = request.json
        return jsonify({
            "message": f"Дрон {drone_id} успешно создан"
        }), 201
    return jsonify({
        "error": "Ошибка при создании дрона"
    }), 404


@app.route("/drones/<drone_id>/takeoff", methods=["POST"])
def takeoff_drone(drone_id):
    if drone_id not in drones:
        return jsonify({
            "error": "Ошибка. Указанный дрон не существует"
        }), 404
    altitude = request.json.get("altitude")
    drone_info = drones[drone_id]
    drone_url = drone_info["control_url"] + "/takeoff"
    response = requests.post(drone_url, json={"altitude": altitude})
    if response.status_code == 200:
        return jsonify({
            "message": response.json().get("message")
        }), 200
    return jsonify({
        "error": f"Ошибка при взлёте дрона с id: {drone_id}"
    }), 500


if __name__ == '__main__':
    app.run(debug=True)