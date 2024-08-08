import requests
from flask import Flask

app = Flask(__name__)
BASE_URL = 'http://127.0.0.1:5000/drones'


drone = {
    "id": {
        "name": "MySuperDrone",
        "status": "landed",
        "location": None
        }
    }
mission = {
    "id": {
        "name": "patrol",
        "start_time": None,
        "end_time": None,
        "route": []
    }
}


# Создание нового БПЛА
@app.route("/drones", methods=["POST"])
def register_drone(drone_id, drone_info):
    url = BASE_URL
    payload = {
        "drone_id": drone_id,
        **drone_info
    }
    response = requests.post(url, json=payload)
    print(f"Ответ сервера на запрос создания нового дрона с ID {drone_id}: {response.json()}")
    return response.json()


# Получение списка всех БПЛА
@app.route("/drones", methods=["GET"])
def get_drones():
    url = BASE_URL
    response = requests.get(url)
    print(f"Ответ сервера на запрос списка всех дронов: {response.json()}")
    return response.json()


# Получение информации о конкретном БПЛА
@app.route("/drones/<drone_id>", methods=["GET"])
def get_drone(drone_id):
    url = f"{BASE_URL}/{drone_id}"
    response = requests.get(url)
    print(f"Ответ сервера на запрос дрона с ID {drone_id}: {response.json()}")
    return response.json()


# Обновление информации о БПЛА
@app.route("/drones/<drone_id>", methods=["PUT"])
def update_drone(drone_id, drone_info):
    url = f"{BASE_URL}/{drone_id}"
    response = requests.put(url, json=drone_info)
    print(f"Ответ сервера на запрос обновления информации дрона с ID {drone_id}: {response.json()}")
    return response.json()


# Удаление БПЛА
@app.route("/drones/<drone_id>", methods=["DELETE"])
def delete_drone(drone_id):
    url = f"{BASE_URL}/{drone_id}"
    response = requests.delete(url)
    print(f"Ответ сервера на запрос удаления дрона с ID {drone_id}: {response.json()}")
    return response.json()


if __name__ == '__main__':
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
    register_drone(1, drone1_info)
    register_drone(2, drone2_info)
    get_drones()
    get_drone(2)
    new_drone2_info = {
        "name": "БПЛА 2",
        "status": "В полёте",
        "location": "Координаты 3"
    }
    update_drone(2, new_drone2_info)
    get_drone(2)
    delete_drone(2)
    get_drone(2)
