# Single Responsibility Principle (Принцип единой ответственности)

class NavigationSystem:
    def calc_route(self, start, end):
        print(f'Расчёт маршрута от {start} до {end}')
        # логика
        pass

class CommunicationSystem:
    def send_data(self, data):
        print(f'Отправка данных: {data}')
        # логика
        pass


# Open/Closed Principle (Принцип открытости/закрытости)

from abc import ABC, abstractmethod

class FlightMode(ABC):
    @abstractmethod
    def execute(self):
        pass


class ManualMode(FlightMode):
    def execute(self):
        print("Ручной режим управления")
        # логика
        pass


class AutoMode(FlightMode):
    def execute(self):
        print("Режим управления автопилот")
        # логика
        pass


class EmergencyMode(FlightMode):
    def execute(self):
        print("Аварийный режим")
        # логика
        pass


class DestructionMode(FlightMode):
    def execute(self):
        print("Самоликвидация")
        # логика
        pass


class Drone:
    def __init__(self, mode: FlightMode):
        self.__mode = mode
        print('Дрон создан')

    def change_mode(self, mode: FlightMode):
        self.__mode = mode
        print('Изменён режим управления')

    def fly(self):
        self.__mode.execute()


manual_mode = ManualMode()
destraction_mode = DestructionMode()

drone = Drone(manual_mode)
drone.fly()
drone.change_mode(destraction_mode)
drone.fly()

print('\n ___________________ \n')

# Liskov Substitution Principle (Принцип подстановки Лисков)

class Sensor(ABC):
    @abstractmethod
    def get_data(self):
        pass


class Camera(Sensor):
    def get_data(self):
        print("Получение видео с камеры")
        return "Данные с камеры"


class Lidar(Sensor):
    def get_data(self):
        print("Чтение данных с лидара")
        return "Данные с лидара"


class Battery(Sensor):
    def get_data(self):
        print("Чтение уровня заряда")
        return "Данные с батареи"


class Drone2:
    def __init__(self, sensor: Sensor):
        self.__sensor = sensor

    def gather_data(self):
        data = self.__sensor.get_data()
        print(f'Собранные данные: {data}')


battery = Battery()
drone_2 = Drone2(battery)
drone_2.gather_data()