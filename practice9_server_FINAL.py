from flask import Flask, request, jsonify

app = Flask(__name__)

drones = {}
missions = {}


# Создание нового БПЛА
@app.route("/drones", methods=["POST"])
def create_drone():
    drone_id = request.json.pop("drone_id")
    if drone_id:
        drones[drone_id] = request.json
        return drones[drone_id], 201
    return jsonify({
        "error": f"Ошибка при регистрации дрона"
    }), 404


# Получение списка всех БПЛА
@app.route("/drones", methods=["GET"])
def get_drones():
    drones_list = []
    for id, drone in drones.items():
        result = {
            "id": id,
            **drone
        }
        drones_list.append(result)
    return jsonify(drones_list), 200


# Получение информации о конкретном БПЛА
@app.route("/drones/<drone_id>", methods=["GET"])
def get_drone(drone_id):
    if int(drone_id) in drones:
        drone = drones[int(drone_id)]
        return jsonify(drone), 200
    return jsonify({
        "error": f"Дрон c ID {drone_id} не найден"
    }), 404


# Обновление информации о БПЛА
@app.route("/drones/<drone_id>", methods=["PUT"])
def update_drone(drone_id):
    global drones
    new_drone_info = request.json
    if int(drone_id) in drones:
        drones[int(drone_id)] = new_drone_info
        return jsonify({
            "message": f"Информация о дроне {drone_id} обновлена"
        }), 200
    return jsonify({
        "error": f"Дрон {drone_id} не найден"
    }), 404


# Удаление БПЛА
@app.route("/drones/<drone_id>", methods=["DELETE"])
def delete_drone(drone_id):
    if drones.pop(int(drone_id), False):
        return jsonify({
            "message": f"Дрон {drone_id} успешно удалён"
        }), 200
    return jsonify({
        "error": f"Не могу удалить дрон {drone_id}. Нет такого дрона в базе."
    }), 404


# Создание новой миссии
@app.route("/missions", methods=["POST"])
def create_mission():
    global missions
    mission_id = request.json.get[0]
    if mission_id:
        missions[mission_id] = request.json
        return jsonify({
            "message": f"Миссия c ID {mission_id} создана"
        }), 201
    return jsonify({
        "error": f"Не могу создать такую миссию"
    }), 400


# Получение списка всех миссий
@app.route("/missions", methods=["GET"])
def get_missions():
    return jsonify(missions), 200


# Получение информации о конкретной миссии
@app.route("/missions/<id>", methods=["GET"])
def get_mission(mission_id):
    mission = missions.get(mission_id)
    if mission:
        return jsonify(mission), 200
    return jsonify({
        "error": f"Миссия с ID {mission_id} не найдена"
    }), 404


# Обновление информации о миссии
@app.route("/missions/<id>", methods=["PUT"])
def update_mission(mission_id):
    global missions
    new_mission_info = request.json.get[mission_id]
    if new_mission_info:
        missions[mission_id] = new_mission_info
        return jsonify({
            "message": f"Миссия {mission_id} успешно обновлена"
        }), 200
    return jsonify({
        "error": f"Миссия {mission_id} не найдена"
    }), 404


# Удаление миссии
@app.route("/missions/<id>", methods=["DELETE"])
def delete_mission(mission_id):
    if missions.pop(mission_id, False):
        return jsonify({
            "message": f"Миссия {mission_id} успешно удалена"
        }), 200
    return jsonify({
        "error": f"Не нашёл миссию с ID {mission_id}"
    }), 404


if __name__ == '__main__':
    app.run(debug=True)



