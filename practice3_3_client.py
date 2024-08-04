import requests
import cv2
import json
import time

base_url = 'http://127.0.0.1:5000/'


def send_telemetry(latitude, longitude, altitude):
    json_data = {
        'latitude': latitude,
        'longitude': longitude,
        'altitude': altitude
    }
    response = requests.post(f'{base_url}telemetry', json=json_data)
    print(response.json())


def send_video(video_frame):
    _, buffer = cv2.imencode('.jpeg', video_frame)
    response = requests.post(f'{base_url}video', data=buffer.tobytes())
    if response.status_code == 204:
        print('Видео отправлено')
    else:
        print('Видео не отправлено')


def takeoff():
    response = requests.post(f"{base_url}drone/takeoff")
    print(f"Взлёт: {response.json()}")


def land():
    response = requests.post(f"{base_url}drone/land")
    print(f"Посадка: {response.json()}")


def update_position(latitude, longitude, altitude):
    data = {
        "latitude": latitude,
        "longitude": longitude,
        "altitude": altitude
    }
    response = requests.put(f"{base_url}update_position", json=data)
    print(f"Обновление позиции: {response.json()}")


if __name__ == '__main__':
    takeoff()
    time.sleep(2)

    update_position(55.7558, 37.6176, 100)
    time.sleep(2)

    update_position(56.1366, 40.3966, 50)
    time.sleep(2)

    land()
