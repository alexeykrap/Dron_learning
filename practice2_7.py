# паттерн "Команда"

from abc import ABC, abstractmethod


class Command(ABC):  # абстрактный интерфейс команды
    @abstractmethod
    def execute(self):  # метод выполнить
        pass

    @abstractmethod
    def undo(self):  # метод отмена
        pass


class Drone:  # получатель команд
    def take_off(self):  # команда для взлёта
        print('БПЛА взлетает')

    def landing(self):  # команда для посадки
        print('БПЛА приземлился')

    def set_course(self, course):  # команда для изменения курса
        print(f'Меняем курс на {course}')


class TakeOff(Command):  # реализация команды Взлёт
    def __init__(self, drone: Drone):
        self._drone = drone

    def execute(self):
        self._drone.take_off()

    def undo(self):
        self._drone.landing()


class Landing(Command):  # реализация команды Посадка
    def __init__(self, drone: Drone):
        self._drone = drone

    def execute(self):
        self._drone.landing()

    def undo(self):
        print('Отмена посадки невозможна')


class SetCourse(Command):
    def __init__(self, drone: Drone, course):
        self._drone = drone
        self._course = course  # новый курс
        self._previous_course = None  # предыдущий курс

    def execute(self):
        self._previous_course = 'предыдущий курс'  # здесь нужна логика добавления курса в историю
        self._drone.set_course(self._course)

    def undo(self):
        if self._previous_course:
            self._drone.set_course(self._previous_course)
        else:
            print('Отменить текущий курс невозможно! Задайте новый курс.')


class RemoteControl:
    def __init__(self):
        self._commands = []
        self._history = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:  # итератор по командам
            command.execute()  # выполняем команду
            self._history.append(command)  # добавляем команду в историю
        self._commands.clear()  # очищаем список команд

    def undo_command(self):  # отмена операции
        if self._history:  # если история операций не пуста
            command = self._history.pop()  # берём последнюю команду
            command.undo()  # выполняем её


if __name__ == '__main__':
    drone = Drone()

    land = Landing(drone)
    take_off = TakeOff(drone)
    set_course = SetCourse(drone, 'новый курс')
    set_course2 = SetCourse(drone, 'ещё более новый курс')

    remote_control = RemoteControl()

    remote_control.add_command(take_off)
    remote_control.add_command(set_course)
    remote_control.add_command(set_course2)
    remote_control.add_command(land)

    remote_control.execute_commands()

    remote_control.undo_command()

