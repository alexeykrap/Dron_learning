class Drone:
    def __init__(self, id='ABC729',
                 max_altitude=300,
                 max_speed=60,
                 flight_time=30,
                 weight=1.5):
        self.__id = id
        self.__max_altitude = max_altitude
        self.__max_speed = max_speed
        self.__flight_time = flight_time
        self.__weight = weight
        self.__cur_altitude = 0
        self.__cur_speed = 0
        self.__cur_coord = (0.0, 0.0)
        self.__flight_path = []

    def set_max_altitude(self, max_altitude: float):
        if 0 < max_altitude < 3000:
            self.__max_altitude = max_altitude
        else:
            raise ValueError('Неверное значение максимальной высоты')

    def get_max_altitude(self):
        return self.__max_altitude

    def set_max_speed(self, max_speed: float):
        if max_speed > 0:
            self.__max_speed = max_speed
        else:
            raise ValueError('Неверное значение максимальной скорости')

    def get_max_speed(self):
        return self.__max_speed

    def set_flight_time(self, flight_time: int):
        if flight_time > 0:
            self.__flight_time = flight_time
        else:
            raise ValueError('Неверное значение времени полёта')

    def get_flight_time(self):
        return self.__flight_time

    # Добавление методов для управления полётом

    def set_cur_altitude(self, altitude):
        if 0 <= altitude <= self.__max_altitude:
            self.__cur_altitude = altitude
        else:
            raise ValueError(f'Высота должна быть в диапазоне от 0 до {self.__max_altitude}')

    def get_cur_altitude(self):
        return self.__cur_altitude

    def get_flight_path(self):
        return self.__flight_path

    def add_waypoint(self, coord: tuple):
        self.__flight_path.append(coord)
        print(f'Добавлена точка маршрута: {self.__flight_path[-1]}')

    def set_cur_coord(self, coord: tuple):
        self.__cur_coord = coord

    def get_cur_coord(self):
        return self.__cur_coord

    def follow_flight_path(self):
        if not self.__flight_path:
            print('Маршрут не задан')
            return  # Аналог записи "return None"
        print(f'Дрон {self.__id}: следую по маршруту')
        for waypoint in self.__flight_path:
            self.set_cur_coord(waypoint)
            print(f'Дрон {self.__id}: достигнута точка {self.__cur_coord}')


class ProfessionalDron(Drone):
    def __init__(self, id='ABC730',
                 max_altitude=1300,
                 max_speed=120,
                 flight_time=90,
                 weight=3):
        super().__init__(id, max_altitude, max_speed, flight_time, weight)
        self.__night_vision = True

    # Добавляем методы управления ночным видением

    def night_vision_on(self):
        if not self.__night_vision:
            self.__night_vision = True
            print(f'Дрон {self.__id}: ночное видение включено!')
        else:
            print(f'Дрон {self.__id}: ночное видение уже включено!')

    def night_vision_off(self):
        if self.__night_vision:
            self.__night_vision = False
            print(f'Дрон {self.__id}: ночное выключено!')
        else:
            print(f'Дрон {self.__id}: ночное уже выключено!')


if __name__ == '__main__':
    drone1 = Drone('0001', flight_time=40)
    print(drone1.__dict__)
    print(drone1.get_max_altitude())
    drone1.set_max_altitude(350)
    print(drone1.get_max_altitude())

    drone1.set_cur_coord((55.7900, 37.7897))
    drone1.add_waypoint((38.8976763, -77.0365298)) # Координаты Белого Дома, Вашинтон
    drone1.add_waypoint((51.50083, -0.12444))  # Координаты Биг Бена, Лондон
    drone1.add_waypoint((48.35000000, 7.45000000))  # Координаты Европарламента, Страстбург

    drone1.follow_flight_path()


