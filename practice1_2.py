import random

altitude = 0  # Высота в метрах
speed = 0  # Скорость в метрах в секунду
weight = 1.5  # Вес БПЛА в килограммах

pitch = 0  # Тангаж в градусах
roll = 0  # Крен в градусах
yaw = 0  # Рысканье в градусах

battery_capacity = 100  # Ёмкость батареи в процентах
# Против часовой стрелке (CСW)
# По часовой стрелке (CW)
# 1 (CCW)  2 (CW)
# 3 (CW)  4 (CСW)
# int - целое число
# float - вещественное число
# str - строка
# list - список
propellers_speed = [0, 0, 0, 0]  # Скорость вращения пропеллеров

direction = 0  # Направление
payload = 500  # Грузоподъёмность в граммах

is_flying = False  # Летит ли БПЛА
is_connected = False  # Подключён ли БПЛА
is_armed = False  # Арминг (армирование) двигателя


def dron_connect():
    global is_connected
    print('Подключение к БПЛА...')
    is_connected = True
    print('Подключение установлено \n')


def arm_dron():
    global is_armed, propellers_speed
    if is_connected:
        print('Армирование двигателя...')
        # симулируем проверку безопасности
        print('Проверка безопастности...')
        is_armed = True
        for i in range(len(propellers_speed)):
            propellers_speed[i] = random.randint(0, 100)
        print('Армирование завершено \n')
    else:
        print('Проверьте соединение \n')


def show_dron():
    print(
        f'''
    _____________Квадрокоптер_______________
    Высота: {altitude} м, Скорость: {speed} м/с,
    Вес БПЛА: {weight} кг, Грузоподъёмность: {payload} г.
    Скорость вращения пропеллеров: {propellers_speed} об/мин.

    Тангаж: {pitch} град,
    Крен: {roll} град,
    Рысканье: {yaw} град.

    Скорости вращения пропеллеров:
    ({propellers_speed[0]})       ({propellers_speed[1]})
     CCW      CW
      \        /
       \      /
        ------
       /      \\
      /        \\
     CW       CCW
    ({propellers_speed[2]})       ({propellers_speed[3]})
    '''
    )


show_dron()
dron_connect()
arm_dron()
show_dron()