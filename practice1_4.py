from practice1_5 import GPS, DistanceSensor, Camera
import time


class Drone:
    brand = "БПЛА РФ"
    n_rotors = 4

    def __init__(self, model, weight, payload, id):
        print("Создаём экземпляр класса Drone")
        self.model = model  # Модель беспилотника
        self.weight = weight  # Вес беспилостника в граммах
        self.payload = payload  # Полезная нагрузка (грузоподъёмность) в граммах
        self.id = id  # Идентификатор беспилотника
        self.altitude = 0  # Высота в метрах
        self.speed = 0  # Скорость в метрах в секунду

        self.pitch = 0  # Тангаж (наклон вперёд или назад) в градусах
        self.roll = 0  # Крен (наклон влево или вправо) в градусах
        self.yaw = 0  # Рысканье (поворот вокруг вертикальной оси) в градусах
        
        self.battery_capacity = 100  # Ёмкость батареи в процентах

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

        self.propellers_speed = [0, 0, 0, 0]  # Скорость вращения пропеллеров в об/мин
        self.propellers_direction = ['CCW', 'CW', 'CW', 'CCW']  # Направление движения пропеллеров

        self.direction = 0  # Направление
        self.is_flying = False  # Летит ли беспилотник?
        self.is_connected = False  # Есть ли связь с беспилотником?
        self.is_armed = False  # Арминг двигателя
        self.speed_k = 1000  # 1 м/с = 1000 об/мин

        self.coordinates = (50.1231, 30.5231)  # Начальные координаты (база)
        self.target_coord = (30.2344, 42.5332)  # Координаты цели
        self.cur_coordinates = (50.1231, 30.5231)  # Текущие координаты

        self.way_coords = []  # где был дрон, его координаты пути
        self.gps = GPS(self.coordinates)
        self.dist_sensor = DistanceSensor()
        self.camera = Camera()
        self.flight_controller = FlightController(self)

    def get_dist(self):
        self.dist_sensor.get_dist()

    def get_coords(self):
        self.cur_coordinates = self.gps.update_coordinates()
        print(f'id: {self.id}, координаты: {self.cur_coordinates}')

    def __del__(self):
        print("Экземпляр класса Drone уничтожен")

    def fly(self):
        pass

    def get_info(self):
        info = f'''
            _____________Квадрокоптер_______________
            Бренд: {self.brand}, Модель: {self.model}
            Количество роторов: {self.n_rotors}
            Высота: {self.altitude} м, Скорость: {self.speed} м/сек,
            Вес БПЛА: {self.weight} кг, Грузоподъёмность: {self.payload} г.
            
            Скорость вращения пропеллеров: {self.propellers_speed} об/мин.

            Тангаж: {self.pitch} град,
            Крен: {self.roll} град,
            Рысканье: {self.yaw} град.

            Скорости вращения пропеллеров:
            ({self.propellers_speed[0]})       ({self.propellers_speed[1]})
             {self.propellers_direction[0]}      {self.propellers_direction[1]}
              \\        /
               \\      /
                ------
               /      \\
              /        \\
             {self.propellers_direction[2]}       {self.propellers_direction[3]}
            ({self.propellers_speed[2]})       ({self.propellers_speed[3]})
            '''
        print(info)


class FlightController:
    """
    Этот класс симулирует управление дроном: взлёт, посадка, изменение высоты и координат
    """

    def __init__(self, drone: Drone):
        self.drone = drone
        self.drone.is_connected = True
        print(f'Соединение с дроном(ID{self.drone.id}) установлено')

    def takeoff(self):
        """
        Симулирует взлёт дрона
        :return:
        """
        if self.drone.is_connected:
            print('Армирование двигателя...')
            # симулируем проверку безопасности
            time.sleep(3)
            print('Проверка безопастности завершена')
            self.drone.is_armed = True
            start = 100
            self.drone.propellers_speed = [start, start, start, start]
            print(f'Армирование завершено. Скорость пропеллеров: {start} об/мин')
            print(f'Направление движение пропеллеров: {self.drone.propellers_direction}')
            self.drone.camera.live_video_on()
            start = 1000
            self.drone.propellers_speed = [start, start, start, start]
            self.drone.is_flying = True
            print(f'Дрон в воздухе!')
            self.drone.altitude = 20
            self.drone.gps.update_coordinates()
            self.drone.get_info()
        else:
            print('Взлететь не удалось. Проверьте соединение')



    def boarding(self):
        """
        Симулирует посадку дрона
        :return:
        """
        pass

    def altitude_change(self, new_altitude):
        """
        Симулирует изменение высоты дрона
        :return:
        """
        pass

    def coords_change(self, new_coords: ()):
        """
        Симулирует изменение координат дрона (полёт в горизонтальной плоскости)
        :param new_coords:
        """
        pass

if __name__ == '__main__':
    drone1 = Drone('Модель 1', 6, 1.5, 'T-1000')
    drone2 = Drone('Модель 2', 3, 1.5, 'T-1001')
    drone1.get_coords()
    drone1.get_coords()
    drone2.get_coords()

    drone1.get_info()
    drone2.get_info()
