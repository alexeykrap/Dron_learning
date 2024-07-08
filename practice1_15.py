class Drone:
    def __init__(self):
        self.is_flying = False
        self.battery_level = 100

    def takeoff(self):
        if self.battery_level > 20:
            self.is_flying = True
            return 'Дрон взлетел'
        else:
            self.is_flying = False
            return 'Взлёт не удался. Проверьте уровень заряда батареи'

    def langing(self):
        if self.is_flying == True:
            self.is_flying = False
            return 'Дрон приземлился'
        else:
            return 'Дрон уже на земле'


if __name__ == 'main':
    my_drone = Drone()
    print(my_drone.takeoff())
    print(my_drone.langing())

