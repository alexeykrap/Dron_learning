from abc import ABC, abstractmethod

# Фабричный метод
class Sensor(ABC):
    @abstractmethod
    def get_data(self):
        pass


class Camera(Sensor):
    def get_data(self):
        return "Данные с камеры"


class Lidar(Sensor):
    def get_data(self):
        return "Данные с лидара"


class SensorFactory(ABC):
    @abstractmethod
    def create_sensor(self):
        pass


class CameraFactory(SensorFactory):
    def create_sensor(self):
        return Camera()


class LidarFactory(SensorFactory):
    def create_sensor(self):
        return Lidar()

sensor_factory = CameraFactory()
sensor = sensor_factory.create_sensor()
data = sensor.get_data()
print(data)

sensor_factory2 = LidarFactory()
sensor2 = sensor_factory2.create_sensor()
data = sensor2.get_data()
print(data)