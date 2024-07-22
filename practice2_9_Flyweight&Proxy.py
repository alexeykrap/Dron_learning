# pattern Flyweight
import time
import math
import matplotlib.pyplot as plt


class CoordinateFlyweight:
    _coordinates = {}

    @staticmethod
    def get_coordinates(lat, lng):
        key = (lat, lng)
        if key not in CoordinateFlyweight._coordinates:
            CoordinateFlyweight._coordinates[key] = key
        return CoordinateFlyweight._coordinates[key]


# pattern Proxy
class DJIDroneProxy:
    def __init__(self, real_drone):
        self._real_drone = real_drone

    def global_position_control(self, lat=None, lng=None, alt=None):  # реализовать, способность вернуться на базу
        # приступаем к логированию
        print(f"Запрос на перемещение к широте: {lat}, долготе: {lng} и высоте: {alt}")
        # обращаемся к SDK дрона
        self._real_drone.global_position_control(lat, lng, alt)
        # time.sleep(1)  # имитация задержки работы программы

    def connect(self):
        print("Запрос на подключение к дрону через использование SDK")
        self._real_drone.request_sdk_permission_control()

    def arming(self):
        print("Выполняем армирование двигателей")
        self._real_drone.arming()

    def takeoff(self):
        print("Взлёт инициирован")
        self._real_drone.takeoff()

    def land(self):
        print("Посадка инициирована")
        self._real_drone.land()


class DJIDrone:
    def global_position_control(self, lat=None, lng=None, alt=None):
        print(f"Запрос на перемещение к широте: {lat}, долготе: {lng} и высоте: {alt}")

    def request_sdk_permission_control(self):
        # print("Запрос на управление через SDK")
        pass

    def arming(self):
        # print("Выполняем армирование дрона")
        pass


    def takeoff(self):
        print("Выполняем взлёт")

    def land(self):
        print("Выполняем приземление")


# строим квадрат по двум точкам (нижняя левая и верхняя правая):
min_lat = 57.826873
min_lng = 55.475823

max_lat = 57.922174
max_lng = 55.671439

begin_lat = min_lat + (max_lat - min_lat) / 2
begin_lng = min_lng + (max_lng - min_lng) / 2

step = 0.00005
altitude = 50   # в метрах

real_drone = DJIDrone()
drone = DJIDroneProxy(real_drone)

coordinates = []

def spiral(drone):
    radius = 0
    angle = 0
    while radius <= (max_lat - min_lat) / 2:
        radius += step
        angle += math.pi / 180  # увеличиваем угол на 1 градус в радианах
        x = math.sin(angle) * radius
        y = math.cos(angle) * radius
        lat_currant = begin_lat + x
        lng_currant = begin_lng + y
        # используем паттерн Flyweight
        coordinate = CoordinateFlyweight.get_coordinates(lat_currant, lng_currant)
        coordinates.append(coordinate)
        drone.global_position_control(lat=lat_currant, lng=lng_currant, alt=altitude)
        # time.sleep(1)  # имитация задержки выполнения команды

drone.connect()
time.sleep(2)
drone.arming()
time.sleep(1)
drone.takeoff()
time.sleep(3)

# отправляем дрон на выполнение миссии
spiral(drone)

# возврат на базу
drone.global_position_control(begin_lat, begin_lng, altitude)
time.sleep(2)
drone.land()

latitude, longitude = zip(*coordinates)
plt.plot(latitude, longitude)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Движение дрона по спирали")
plt.show()
