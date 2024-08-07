from flask import Flask, Response, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

drones = {
    'status': 'landed',
    'position': {
        'latitude': 0.0,
        'longitude': 0.0,
        'altitude': 0.0
    },
    'telemetry_data': []
}


@app.route("/drones", methods=["GET"])
def get_drones():
    return jsonify(drones), 200


@app.route("/drones/<drone_id>", methods=["GET"])
def get_drone(drone_id):
    drone = drones.get(drone_id)
    if drone:
        return jsonify(drone), 200
    return jsonify({
            "error": "Такого дрона нет"
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
        "error": "Не передан id дрона"
    }), 404

# попробовать сделать самостоятельную реализацию методов:
# takeoff, land и move из практики 3.1


@app.route("/drones/<drone_id>", methods=["POST"])
def takeoff(drone_id):
    drone = drones.get(drone_id)
    if drone:
        try:
            drone.takeoff()  # реализовать метод takeoff
            return jsonify({
                "message": f"Дрон {drone_id} успешно взлетел"
            }), 200
        except Exception as e:
            return jsonify({
                "error": "Ошибка при взлёте"
            }), 500  # правильный код ошибки?
    return jsonify({
        "error": f"Дрон {drone_id} не найден"
    }), 404





app.run()
