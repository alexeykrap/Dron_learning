import random
import time


class GPS:
    """
    Этот класс симулирует работу GPS-модуля дрона
    """
    def __init__(self, init_coordinates=(0.0, 0.0)):
        """
        Задает текущие координаты по-умолчанию (0.0, 0.0) в переменную coordinates
        :param init_coordinates:
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
        print(f'Обновление координат: {self.__coordinates}')
        return self.__coordinates


class DistanceSensor:
    """
    Этот класс симулирует работу дальномера дрона
    """
    def __init__(self, max_dist=10000.0):
        """
        Создает экзепляр класса с параметром по умолчанию max_dist(максимальная дистанция), равным 10000м,
        обращается к другому методу класса (update_dist) и присваивает возвращённое от него значение
        переменной cur_dist(текущая дистанция)
        :param max_dist:
        """
        self.__max_dist = max_dist
        self.__cur_dist = self.update_dist()

    def update_dist(self):
        """
        Симулирует измерение расстояния,
        задает случайное число от 0 до max_dist(по умолчанию 10000м) и возвращает его
        """
        return round(random.uniform(0, self.__max_dist), 2)

    def set_max_dist(self, new_max_dist):
        """
        Задаёт новое значение максимальной дистанции
        :param new_max_dist:
        :return:
        """
        if new_max_dist > 0:
            self.__max_dist = new_max_dist
        else:
            raise ValueError('Неверное значение максимальной дистанции')

    def get_dist(self):
        """
        Возвращает значение параметра текущих координат (cur_dist)
        :return:
        """
        return self.__cur_dist


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


if __name__ == '__main__':
    pass