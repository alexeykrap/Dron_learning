# паттерн Легковес (Flyweight)

class DroneFlyweight:
    def __init__(self, model, manufacturer, sensors):
        self._model = model
        self._manufacturer = manufacturer
        self._sensors = sensors

    def operation(self, unique_state):
        print(f"""
        Дрон: модель {self._model}, производитель {self._manufacturer};
        Датчики: {self._sensors};
        Координаты: {unique_state['coordinates']},
        Скорость: {unique_state['speed']},
        Миссия: {unique_state['mission']},
        Высота: {unique_state['altitude']},
        Заряд батареи: {unique_state['battery']},        
""")

    @property
    def model(self):
        return self._model

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def sensors(self):
        return self._sensors


class DroneFactory:
    def __init__(self):
        self._drones = {}

    def get_drone(self, model, manufacturer, sensors):
        key = (model, manufacturer, sensors)
        if key not in self._drones:
            self._drones[key] = DroneFlyweight(model, manufacturer, sensors)
        return self._drones[key]

    def list_drones(self):
        count = len(self._drones)
        print(f'Всего дронов: {count}')
        for drone in self._drones:
            print(f"""Ключ: 
    модель - {drone[0]}, 
    производитель - {drone[1]}, 
    датчики - {drone[2]}""")


def client_code():
    factory = DroneFactory()

    drone1 = factory.get_drone('ModelX', 'DroneCorp', 'camera, GPS')
    drone1.operation({
        'coordinates': '10, 20, 30',
        'speed': '50',
        'mission': 'Surveillance',
        'altitude': '100',
        'battery': '80',
    })

    drone2 = factory.get_drone('ModelX', 'DroneCorp', 'camera, GPS')
    drone2.operation({
        'coordinates': '50, 80, 40',
        'speed': '100',
        'mission': 'Surveillance',
        'altitude': '120',
        'battery': '30',
    })

    drone3 = factory.get_drone('ModelY', 'SkyTech', 'lidar, GPS')
    drone3.operation({
        'coordinates': '40, 50, 38',
        'speed': '75',
        'mission': 'Surveillance',
        'altitude': '80',
        'battery': '99',
    })

    factory.list_drones()


if __name__ == '__main__':
    client_code()




