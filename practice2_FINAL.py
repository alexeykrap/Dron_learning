import random
import time


class GPS:
    """
    Этот класс симулирует работу GPS-модуля дрона
    """
    def __init__(self, init_coordinates=(0.0, 0.0)):
        """
        Задает текущие координаты по-умолчанию (0.0, 0.0) в переменную coordinates
        """
        self.__coordinates = init_coordinates

    def update_coordinates(self):
        """
        Симулирует обновление координат GPS
        """
        lat_variation = random.uniform(-0.0001, 0.0001)  # симулирует изменение широты
        lon_variation = random.uniform(-0.0001, 0.0001)  # симулирует изменение долготы
        lat = round(self.__coordinates[0] + lat_variation, 4)
        lon = round(self.__coordinates[1] + lon_variation, 4)
        self.__coordinates = (lat, lon)
        print(f'Обновление координат по GPS: {self.__coordinates}')
        return self.__coordinates


class Camera:
    """
    Этот класс симулирует работу камеры дрона
    """
    def __init__(self, model='Model-1', matrix=(600, 800)):
        """
        Задает первоначальные параметры для нашей камеры (модель и размеры матрицы в пикселах)
        :param model:
        :param matrix:
        """
        self.__model = model
        self.__matrix = matrix

    # Сеттеры и геттеры

    def set_model(self, new_model: str):
        self.__model = new_model
        print(f'Модель успешно обновлена. Новая модель - {self.__model}')

    def get_model(self):
        return self.__model

    def set_matrix(self, new_matrix: tuple):
        self.__matrix = new_matrix
        print(f'Модель успешно обновлена. Новая модель - {self.__matrix}')

    def get_matrix(self):
        return self.__matrix

    # Другие методы класса Camera

    def get_foto(self):
        """
        Симулирует создание фото
        """
        print('Фото сделано')

    def live_video_on(self):
        """
        Симулирует включение трансляции видеопотока
        """
        print('Включается трансляция видео...')
        time.sleep(2)
        print('Трансляция видео включена')

    def live_video_off(self):
        """
        Симулирует отключение трансляции видеопотока
        """
        print('Трансляция видео выключена')


class Drone:
    brand = "БПЛА РФ"
    n_rotors = 4
    max_altitude = 300

    def __init__(self, model, weight, payload, id):
        # print("Создаём экземпляр класса Drone")
        self.__model = model  # Модель беспилотника
        self.__weight = weight  # Вес беспилостника в граммах
        self.__payload = payload  # Полезная нагрузка (грузоподъёмность) в граммах
        self.__id = id  # Идентификатор беспилотника
        self.__altitude = 0  # Высота в метрах
        self.__speed = 0  # Скорость в метрах в секунду

        self.__pitch = 0  # Тангаж (наклон вперёд или назад) в градусах
        self.__roll = 0  # Крен (наклон влево или вправо) в градусах
        self.__yaw = 0  # Рысканье (поворот вокруг вертикальной оси) в градусах

        self.__battery_capacity = 100  # Ёмкость батареи в процентах

        # Против часовой стрелки (CCW)
        # По часовой стрелке (CW)
        # (1)       (2)
        #  CCW      CW
        #   \        /
        #    \      /
        #     ------
        #    /      \
        #   /        \
        #  CW       CCW
        # (3)       (4)

        self.__propellers_speed = [0, 0, 0, 0]  # Скорость вращения пропеллеров в об/мин
        self.__propellers_direction = ['CCW', 'CW', 'CW', 'CCW']  # Направление движения пропеллеров

        self.__direction = 0  # Направление
        self.__is_flying = False  # Летит ли беспилотник?
        self.__is_connected = False  # Есть ли связь с беспилотником?
        self.__is_armed = False  # Арминг двигателя
        self.__speed_k = 1000  # 1 м/с = 1000 об/мин

        self.__coordinates = (50.1231, 30.5231)  # Начальные координаты (база)
        self.__cur_coord = (50.1231, 30.5231)  # Текущие координаты
        self.__flight_path = []

        self.__way_coords = []  # где был дрон, его координаты пути

        # Эти функции для управления дроном, поэтому их лучше оставить public
        self.gps = GPS(self.__coordinates)
        self.camera = Camera()
        self.flight_controller = FlightController(self)
        self.get_info()

    # Геттеры и сеттеры

    def get_id(self):
        return self.__id

    def get_gron_connect(self):
        return self.__is_connected

    def set_dron_connect(self, connect_status):
        self.__is_connected = connect_status

    def get_dron_status(self):
        return self.__is_flying

    def set_dron_status(self, new_status):
        self.__is_flying = new_status

    def set_propellers_speed(self, new_propellers_speed: []):
        self.__propellers_speed = new_propellers_speed

    def get_propellers_speed(self):
        return self.__propellers_speed

    def set_altitude(self, new_altitude: int):
        self.__altitude = new_altitude

    def get_propellers_direction(self):
        return f'{self.__propellers_direction}'

    def set_is_armed(self, new_status):
        self.__is_armed = new_status

    # Другие методы класса

    def get_coords(self):
        self.__cur_coord = self.gps.update_coordinates()
        # print(f'id: {self.__id}, координаты: {self.__cur_coord}')

    def fly(self, new_coords: ()):
        if self.__is_flying and new_coords != self.get_coords():
            # print(f'Текущие координаты: {self.__cur_coord}')
            print(f'Выдвигаемся к цели: {new_coords}')
            self.__cur_coord = new_coords
            self.__way_coords.append(self.__cur_coord)
            print('Цель достигнута!')
        else:
            print(f'Дрон {self.get_id()} не в воздухе')

    def get_info(self):
        info = f'''
            _____________Квадрокоптер_______________
            Бренд: {self.brand}, Модель: {self.__model}
            ID: {self.__id}, Количество роторов: {self.n_rotors}
            Высота: {self.__altitude} м, Скорость: {self.__speed} м/сек,
            Вес БПЛА: {self.__weight} кг, Грузоподъёмность: {self.__payload} г.

            Скорость вращения пропеллеров: {self.__propellers_speed} об/мин.

            Тангаж: {self.__pitch} град,
            Крен: {self.__roll} град,
            Рысканье: {self.__yaw} град.

            Скорости вращения пропеллеров:
            ({self.__propellers_speed[0]})       ({self.__propellers_speed[1]})
             {self.__propellers_direction[0]}      {self.__propellers_direction[1]}
              \\        /
               \\      /
                ------
               /      \\
              /        \\
             {self.__propellers_direction[2]}       {self.__propellers_direction[3]}
            ({self.__propellers_speed[2]})       ({self.__propellers_speed[3]})
            '''
        print(info)


class FlightController:
    """
    Этот класс симулирует управление дроном: взлёт, посадка, изменение высоты и координат
    """
    def __init__(self, drone: Drone):
        self.drone = drone
        self.drone.set_gron_connect = True
        print(f'Контроллер полёта: соединение с дроном {self.drone.get_id()} установлено')

    def takeoff(self):
        """
        Симулирует взлёт дрона
        """
        if self.drone.get_gron_connect:
            print('Армирование двигателя...')
            # симулируем проверку безопасности
            time.sleep(1)
            print('Проверка безопастности завершена')
            self.drone.set_is_armed = True
            start = 100
            self.drone.set_propellers_speed([start, start, start, start])
            print(f'Армирование завершено. Скорость пропеллеров: {start} об/мин')
            print(f'Направление движение пропеллеров: {self.drone.get_propellers_direction()}')
            self.drone.camera.live_video_on()
            start = 1000
            self.drone.set_propellers_speed([start, start, start, start])
            print(f'Скорость вращение пропеллеров: {self.drone.get_propellers_speed()}')
            self.drone.set_dron_status(True)
            print(f'Дрон в воздухе!')
            self.drone.set_altitude(20)
            self.drone.gps.update_coordinates()
            # self.drone.get_info()
        else:
            print('Взлететь не удалось. Проверьте соединение')

    def landing(self):
        """
        Симулирует посадку дрона
        """
        if self.drone.get_dron_status:
            self.drone.set_altitude(0)
            print(f'Дрон {self.drone.get_id()} успешно приземлился')
        else:
            print(f'Дрон {self.drone.get_id()} не в воздухе')

    def altitude_change(self, new_altitude):
        """
        Симулирует изменение высоты дрона
        :return:
        """
        if self.drone.get_dron_status and 0 < new_altitude <= self.drone.max_altitude:
            self.drone.set_altitude(new_altitude)
            print(f'Дрон {self.drone.get_id()} поднялся на высоту {new_altitude}м')
        else:
            print(f'Дрон {self.drone.get_id()} не в воздухе или неверные значения высоты')

    def coords_change(self, new_coords: ()):
        """
        Симулирует изменение координат дрона (полёт в горизонтальной плоскости)
        """
        if self.drone.get_dron_status():
            self.drone.fly(new_coords)
        else:
            print(f'Дрон не в воздухе')



# Создаём экземпляр класса Drone
drone1 = Drone('T-1000', 5, 2000, '12342341')
# Начинаем управление им
drone1.flight_controller.takeoff()
drone1.flight_controller.altitude_change(300)
drone1.flight_controller.coords_change((38.8976763, -77.0365298))  # Good bay, America!
drone1.flight_controller.landing()