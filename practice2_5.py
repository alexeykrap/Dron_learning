# паттерн Мост
from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def set_rotation_speed(self, speed: int):
        pass


class SingleEngine(Engine):
    def start(self):
        return "Запуск двигателя"

    def stop(self):
        return "Остановка двигателя"

    def status(self):
        return "Статус одного двигателя"

    def set_rotation_speed(self, speed: int):
        power = speed * 10  # Каждый процент скорости потребляет 10 мА
        print(f"Скорость вращения одного двигателя установлена на {speed}%")
        return power  # Возвращаем потребляемую мощность


class TripleEngine(Engine):
    def start(self):
        return "Запуск 3 двигателей"

    def stop(self):
        return "Остановка 3 двигателей"

    def status(self):
        return "Статус 3 двигателей"

    def set_rotation_speed(self, speed: int):
        power = speed * 30  # Каждый процент скорости потребляет 10 мА
        print(f"Скорость вращения трёх двигателей установлена на {speed}%")
        return power  # Возвращаем потребляемую мощность


class QuadEngine(Engine):
    def start(self):
        return "Запуск 4 двигателей"

    def stop(self):
        return "Остановка 4 двигателей"

    def status(self):
        return "Статус 4 двигателей"

    def set_rotation_speed(self, speed: int):
        power = speed * 30  # Каждый процент скорости потребляет 10 мА
        print(f"Скорость вращения четырёх двигателей установлена на {speed}%")
        return power  # Возвращаем потребляемую мощность


class Drone(ABC):
    def __init__(self, engine: Engine):
        self.engine = engine

    @abstractmethod
    def fly(self):
        pass


class StandartDrone(Drone):
    def fly(self):
        print(self.engine.start())
        print("Стандартный дрон в полёте")
        speed = 50  # Двигатель запущен на 50% мощности
        print(f"Потребляемый ток: {self.engine.set_rotation_speed(speed)} мА")
        print(self.engine.status())
        print(self.engine.stop())


class AdvancedDrone(Drone):
    def fly(self):
        print(self.engine.start())
        print("Продвинутый дрон в полёте")
        speed = 50  # Двигатель запущен на 50% мощности
        print(f"Потребляемый ток: {self.engine.set_rotation_speed(speed)} мА")
        print(self.engine.status())
        print(self.engine.stop())

    def get_status(self):
        print(self.engine.status())

    def set_speed(self, speed: int):
        current = self.engine.set_rotation_speed(speed)
        print(f"Установлена скорость: {speed}%, \nПотребляемый ток: {current}")


if __name__ == "__main__":
    single_engine = SingleEngine()
    triple_engine = TripleEngine()
    quad_engine = QuadEngine()

    standart_drone = StandartDrone(single_engine)
    advanced_drone = AdvancedDrone(quad_engine)

    standart_drone.fly()
    print()

    advanced_drone.fly()
    advanced_drone.set_speed(75)
    advanced_drone.get_status()
    print()

    print("Замена двигателя")
    advanced_drone.engine = triple_engine
    advanced_drone.fly()
    advanced_drone.get_status()

