from abc import ABC, abstractmethod
import random
from typing import List


print("\nИтератор\n")
class GPS:
    def __init__(self, init_coordinates=(0.0, 0.0)):
        self._coordinates = init_coordinates

    def __str__(self):
        return f"{self._coordinates}"

    def update_coordinates(self):
        latitude = round(random.uniform(-90.0, 91.0), 4)
        longitude = round(random.uniform(-180.0, 181.0), 4)
        return latitude, longitude


class WayPoint:  # класс "Точка маршрута"
    def __init__(self):
        self._way_point = GPS()

    def __str__(self):
        return f"точка маршрута: {self._way_point.update_coordinates()}"

    def get_coordinates(self):
        return self._way_point.update_coordinates


class MyIterator(ABC):  # Базовый (абстрактный) класс Итератора
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


class WayPointIterator(MyIterator):  # Конкретный класс Итератора для точек маршрута
    def __init__(self, way: List[WayPoint]):
        self._way = way
        self._index = 0

    def next(self) -> WayPoint:
        way_point = self._way[self._index]
        self._index += 1
        return way_point

    def has_next(self) -> bool:
        return True if self._index < len(self._way) else False

    def get_index(self):
        return self._index


class Way:  # класс Way для хранения набора точек маршрута
    def __init__(self, n_points: int = 10):
        self.n_points = n_points
        self.way = []
        for i in range(n_points):
            way_point = WayPoint()
            self.way.append(way_point)

    def __str__(self):
        return f"Этот путь состоит из {self.n_points} точек"

    def iter(self) ->  MyIterator:
        print(self.__str__())
        return WayPointIterator(self.way)


if __name__ == "__main__":
    way = Way(5)
    iterator = way.iter()  # итератор "заряжен" пятью точками маршрута
    while iterator.has_next():  # перебираем эти 5 точек
        way_point = iterator.next()
        print(f"Это {iterator.get_index()} {str(way_point)}")
    print("*" * 20)
    iterator = way.iter()
    iterator.next()  # вручную вызываем метод next() у итератора
    while iterator.has_next():  # перебираем оставшиеся 4 точки маршрута
        way_point = iterator.next()
        print(f"Это {iterator.get_index()} {str(way_point)}")


print("\nНаблюдатель\n")


class MyObserver(ABC):  # Базовый(абстрактный) класс Наблюдателя
    @abstractmethod
    def update(self, message: str):
        pass


class MonitoringSystem(MyObserver):
    def update(self, message: str):
        print(f"Система отслеживания получила сообщение: \n{message}")


class MySubject:  #  наблюдаемый объект
    def __init__(self):
        self._observers = []  # создаем пустой список наблюдателей

    def register(self, observer: MyObserver):
        self._observers.append(observer)  # добавляем в список наблюдателя

    def notify(self, message: str):
        if self._observers:
            for observer in self._observers:
                observer.update(message)


class BatteryLevelSensor(MySubject):  # Конкретный наблюдаемый объект: Датчик уровня заряда батареи
    def __init__(self, battery_level: int):
        super().__init__()
        if 0 <= battery_level <= 100:
            self._battery_level = battery_level
        else:
            print("Некорректный уровень заряда батареи!")

    def get_battery_level(self):
        if self._observers:
            self.notify(f"Уровень заряда батареи: {self._battery_level}%")
        return self._battery_level


if __name__ == "__main__":
    battery_level_sensor = BatteryLevelSensor(30)
    monitoring_system = MonitoringSystem()

    battery_level_sensor.register(monitoring_system)
    battery_level_sensor.get_battery_level()

print("\nШаблонный метод\n")


class MyBase(ABC):
    @abstractmethod
    def template_method(self):
        pass


class MyClass1(MyBase):
    def template_method(self):
        print(f"Это метод класса {self.__class__.__name__}")


class MyClass2(MyBase):
    def template_method(self):
        print(f"Это метод класса {self.__class__.__name__}")


if __name__ == "__main__":
    my_object1 = MyClass1()
    my_object2 = MyClass2()

    my_object1.template_method()
    my_object2.template_method()