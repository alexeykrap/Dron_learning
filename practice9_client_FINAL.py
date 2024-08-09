import requests
from flask import Flask, jsonify

app = Flask(__name__)
BASE_URL = 'http://127.0.0.1:5000'


# Создание нового БПЛА
@app.route("/drones", methods=["POST"])
def register_drone(drone_id, drone_info):
    try:
        url = f'{BASE_URL}/drones'
        payload = {
            "drone_id": drone_id,
            **drone_info
        }
        response = requests.post(url, json=payload)
        print(f"Ответ сервера на запрос создания нового дрона с ID {drone_id}:\n "
              f"{response.json()} Код - {response.status_code}")
        return response.json()
    except Exception as e:
        return jsonify({
            "error": f"Невозможно зарегистрировать дрон {drone_id} на сервере: {e}"
        }), 500


# Получение списка всех БПЛА
@app.route("/drones", methods=["GET"])
def get_drones():
    try:
        url = f'{BASE_URL}/drones'
        response = requests.get(url)
        print(f"Ответ сервера на запрос списка всех дронов:\n "
              f"{response.json()} Код - {response.status_code}")
        return response.json()
    except Exception as e:
        return jsonify({
            "error": f"Невозможно получить список дронов с сервера: {e}"
        }), 500


# Получение информации о конкретном БПЛА
@app.route("/drones/<drone_id>", methods=["GET"])
def get_drone(drone_id):
    try:
        url = f"{BASE_URL}/drones/{drone_id}"
        response = requests.get(url)
        print(f"Ответ сервера на запрос дрона с ID {drone_id}:\n "
              f"{response.json()} Код - {response.status_code}")
        return response.json()
    except Exception as e:
        return jsonify({
            "error": f"Невозможно получить информацию о дроне {drone_id} с сервера: {e}"
        }), 500


# Обновление информации о БПЛА
@app.route("/drones/<drone_id>", methods=["PUT"])
def update_drone(drone_id, drone_info):
    try:
        url = f"{BASE_URL}/drones/{drone_id}"
        response = requests.put(url, json=drone_info)
        print(f"Ответ сервера на запрос обновления информации дрона с ID {drone_id}:\n "
              f"{response.json()} Код - {response.status_code}")
        return response.json()
    except Exception as e:
        return jsonify({
            "error": f"Невозможно получить обновить информацию о дроне {drone_id} на сервере: {e}"
        }), 500


# Удаление БПЛА
@app.route("/drones/<drone_id>", methods=["DELETE"])
def delete_drone(drone_id):
    try:
        url = f"{BASE_URL}/drones/{drone_id}"
        response = requests.delete(url)
        print(f"Ответ сервера на запрос удаления дрона с ID {drone_id}:\n "
              f"{response.json()} Код - {response.status_code}")
        return response.json()
    except Exception as e:
        return jsonify({
            "error": f"Невозможно удалить дрон {drone_id} на сервере: {e}"
        }), 500


# Создание новой миссии
@app.route("/missions", methods=["POST"])
def register_mission(mission_id, mission_info):
    try:
        url = f'{BASE_URL}/missions'
        payload = {
            "mission_id": mission_id,
            **mission_info
        }
        response = requests.post(url, json=payload)
        print(f"Ответ сервера на запрос создания новой миссии с ID {mission_id}:\n "
              f"{response.json()} Код - {response.status_code}")
        return response.json()
    except Exception as e:
        return jsonify({
            "error": f"Невозможно зарегистрировать миссию {mission_id} на сервере: {e}"
        }), 500


# Получение списка всех миссий
@app.route("/missions", methods=["GET"])
def get_missions():
    try:
        url = f'{BASE_URL}/missions'
        response = requests.get(url)
        print(f"Ответ сервера на запрос списка всех миссий:\n "
              f"{response.json()} Код - {response.status_code}")
        return response.json()
    except Exception as e:
        return jsonify({
            "error": f"Невозможно получить список миссий с сервера: {e}"
        }), 500


# Получение информации о конкретной миссии
@app.route("/missions/<mission_id>", methods=["GET"])
def get_mission(mission_id):
    try:
        url = f"{BASE_URL}/missions/{mission_id}"
        response = requests.get(url)
        print(f"Ответ сервера на запрос миссии с ID {mission_id}:\n "
              f"{response.json()} Код - {response.status_code}")
        return response.json()
    except Exception as e:
        return jsonify({
            "error": f"Невозможно получить информацию о миссии {mission_id} с сервера: {e}"
        }), 500


# Обновление информации о миссии
@app.route("/missions/<mission_id>", methods=["PUT"])
def update_mission(mission_id, mission_info):
    try:
        url = f"{BASE_URL}/missions/{mission_id}"
        response = requests.put(url, json=mission_info)
        print(f"Ответ сервера на запрос обновления информации миссии с ID {mission_id}:\n "
              f"{response.json()} Код - {response.status_code}")
        return response.json()
    except Exception as e:
        return jsonify({
            "error": f"Невозможно получить обновить информацию о миссии {mission_id} на сервере: {e}"
        }), 500


# Удаление миссии
@app.route("/missions/<mission_id>", methods=["DELETE"])
def delete_mission(mission_id):
    try:
        url = f"{BASE_URL}/missions/{mission_id}"
        response = requests.delete(url)
        print(f"Ответ сервера на запрос удаления дрона с ID {mission_id}:\n "
              f"{response.json()} Код - {response.status_code}")
        return response.json()
    except Exception as e:
        return jsonify({
            "error": f"Невозможно удалить миссию {mission_id} на сервере: {e}"
        }), 500


if __name__ == '__main__':
    # ДРОНЫ
    # создаем новых дронов
    drone1_info = {
        "name": "БПЛА 1",
        "status": "В полёте",
        "location": "Координаты 1"
    }
    drone2_info = {
        "name": "БПЛА 2",
        "status": "На земле",
        "location": "Координаты 2"
    }
    # регистрируем их на сервере
    register_drone(1, drone1_info)
    register_drone(2, drone2_info)
    # выводим список всех дронов
    get_drones()
    # выводим информациою о дроне №2
    get_drone(2)
    # меняем информацию о дроне №2
    new_drone2_info = {
        "name": "БПЛА 2",
        "status": "В полёте",
        "location": "Координаты 3"
    }
    # обновляем информацию на сервере
    update_drone(2, new_drone2_info)
    # вызываем новую информацию о дроне №2
    get_drone(2)
    # удаляем дрон №2
    delete_drone(2)
    # проверяем, что нам ответит сервер на запрос удалённого дрона
    get_drone(2)

    # МИССИИ
    # создаем новые миссии
    mission1_info = {
        "name": "Миссия 1",
        "start_time": "Время начала 1",
        "end_time": "Время окончания 1",
        "location": "Координаты 1"
    }
    mission2_info = {
        "name": "Миссия 2",
        "start_time": "Время начала 2",
        "end_time": "Время окончания 2",
        "location": "Координаты 2"
    }
    # регистрируем их на сервере
    register_mission(1, mission1_info)
    register_mission(2, mission2_info)
    # выводим список всех миссий
    get_missions()
    # выводим информациою о миссии №2
    get_mission(2)
    # меняем информацию о миссии №2
    new_mission2_info = {
        "name": "Миссия 2",
        "start_time": "Время начала 3",
        "end_time": "Время окончания 3",
        "location": "Координаты 3"
    }
    # обновляем информацию на сервере
    update_mission(2, new_mission2_info)
    # вызываем новую информацию о миссии №2
    get_mission(2)
    # удаляем миссию №2
    delete_mission(2)
    # проверяем, что нам ответит сервер на запрос удалённой миссии
    get_mission(2)
