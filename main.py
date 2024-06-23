import random
import time

altitude = 0  # Высота в метрах
speed = 0  # Скорость в метрах в секунду
weight = 1.5  # Вес БПЛА в килограммах
speed_k = 1000  # 1 м/с = 1000 об/мин

coordinates = (50.2223, 30.1234)  # начальные координаты
target_coord = (30.4533, 42.5779)  # координаты цели
way_coords = []

pitch = 0  # Тангаж в градусах (поворот поперечной оси, наклон вперёд/назад)
roll = 0  # Крен в градусах (поворот вокруг продольной оси, наклон влево/вправо)
yaw = 0  # Рысканье в градусах (поворот относительно вертикальной оси)

battery_capacity = 100  # Ёмкость батареи в процентах
propellers_speed = [0, 0, 0, 0]  # Скорость вращения пропеллеров
propellers_direction = ['CCW', 'CW', 'CCW', 'CW']  # Направление движения пропеллеров
# Против часовой стрелке (CСW)
# По часовой стрелке (CW)

direction = 0  # Направление
payload = 500  # Грузоподъёмность в граммах

is_flying = False  # Летит ли БПЛА
is_connected = False  # Подключён ли БПЛА
is_armed = False  # Арминг (армирование) двигателя


def dron_connect():
    global is_connected
    print('Подключение к БПЛА...')
    time.sleep(1)
    is_connected = True
    print('Подключение установлено \n')


def arm_dron():
    global is_armed, propellers_speed
    if is_connected:
        print('Армирование двигателя...')
        # симулируем проверку безопасности
        time.sleep(3)
        print('Проверка безопастности завершена')
        is_armed = True
        start = 100
        propellers_speed = [start, start, start, start]
        way_coords.append(coordinates)
        print(f'Армирование завершено. Скорость пропеллеров: {start} об/мин')
        print(f'Направление движение пропеллеров: {propellers_direction}')
    else:
        print('Армирование не завершено. Проверьте соединение')


def get_info():
    info = f'''
    _____________Квадрокоптер_______________
    Высота: {altitude} м, Скорость: {speed} м/с,
    Вес БПЛА: {weight} кг, Грузоподъёмность: {payload} г.
    Скорость вращения пропеллеров: {propellers_speed} об/мин.

    Тангаж: {pitch} град,
    Крен: {roll} град,
    Рысканье: {yaw} град.

    Скорости вращения пропеллеров:
    ({propellers_speed[0]})       ({propellers_speed[1]})
     {propellers_direction[0]}      {propellers_direction[1]}
      \\        /
       \\      /
        ------
       /      \\
      /        \\
     {propellers_direction[2]}       {propellers_direction[3]}
    ({propellers_speed[2]})       ({propellers_speed[3]})
    '''
    print(info)


def set_propellers_speed(speed):
    global propellers_speed
    if is_armed:
        propellers_speed = [speed * speed_k, speed * speed_k, speed * speed_k, speed * speed_k]
        print(f'Скорость вращения пропеллеров: {propellers_speed}')
    else:
        print('Не удалось установить скорость вращения пропеллеров. Двигатель не армирован!')


def move_to_coords(target):
    global coordinates, altitude, speed, direction
    if is_armed and is_flying:
        print(f'Перемещаемся к координатам: {target}...')
        coordinates = target
        altitude = 10
        speed = 6
        direction = 200
        time.sleep(5)
        print(f'Достигли цели')
        way_coords.append(coordinates)


get_info()
dron_connect()
arm_dron()
get_info()

if is_armed and is_connected:
    set_propellers_speed(100)
    print('Взлёт!')
    speed = 5
    altitude = 10
    pitch = 15
    roll = 5
    yaw = 10
    direction = 90
    is_flying = True
    battery_capacity -= 5
    telemetry = {
        'speed': speed,
        'altitude': altitude,
        'pitch': pitch,
        'roll': roll,
        'yaw': yaw,
        'direction': direction,
        'propellers_direction': propellers_direction,
        'propellers_speed': propellers_speed,
        'coordinates': coordinates,
        'battery_capacity': battery_capacity,
    }
    print(f'Телеметрия: {telemetry}')
else:
    print('Взлететь не удалось!')

if is_flying:
    move_to_coords(target_coord)

get_info()

# Выводим весь путь дрона
print(way_coords)
# Скрываем начальные координаты (в случае с военными дронами)
# Подменяем начальные координаты на случайные вещественные числа
# с помощью функции uniform
# функция round позволяет округлить числа до 4 знаков после запятой
# чтобы число было похоже на реальную координату
way_coords[0] = (
    round(random.uniform(1, 50), 4),
    round(random.uniform(1, 50), 4)
)
print(way_coords)