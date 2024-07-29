from abc import ABC, abstractmethod

class DroneRepository(ABC):
    @abstractmethod
    def get_all_drones(self):
        """
        Получить список всех дронов
        :return:
        """
        pass

    @abstractmethod
    def get_drone_by_id(self, id: int):
        """
        Получить информацию о дроне по его id
        :param id:
        :return:
        """
        pass

    def update_drone_status(self, id: int, status: str):
        """
        Обновляем статус дрона по id (ожидание, в полёте, зарядка)
        :param id:
        :param status:
        :return:
        """
        pass

    @abstractmethod
    def add_drone(self, drone: dict):  # добавить реализацию класса Drone
        """
        Добавление дрона в рой
        :param drone:
        :return:
        """
        pass

    @abstractmethod
    def remove_drone(self, id: int):
        """
        Удаление дрона из роя по id
        :param id:
        :return:
        """
        pass


class MemoryDroneRepository(DroneRepository):
    def __init__(self):
        self._drones = {}

    def get_all_drones(self):
        """
        Получить список всех дронов в памяти
        :return:
        """
        return list(self._drones.values())

    def get_drone_by_id(self, id: int):
        """
        Получить дрона из памяти по id
        :param id:
        :return:
        """
        if self._drones[id]:
            return self._drones.get(id, None)
        else:
            return "Такой дрон в системе не найден"

    def update_drone_status(self, id: int, status: str):
        """
        Обновить статус дрона в памяти
        :param id:
        :param status:
        :return:
        """
        if id in self._drones:
            self._drones[id]['status'] = status  # если здесь будет объект класса Drone, то нужно сделать по другому

    def add_drone(self, drone: dict):
        """
        Добавление дрона в память устройства
        :param drone:
        :return:
        """
        id = drone['id']
        self._drones[id] = drone

    def remove_drone(self, id: int):
        """
        Удаление дрона в памяти устройства
        :param id:
        :return:
        """
        if self._drones[id]:
            del self._drones[id]
        else:
            return "Такого дрона в памяти не найдено"


def list_all_drones(drone_repository: DroneRepository):
    drones = drone_repository.get_all_drones()
    for drone in drones:
        print(f"Дрон id: {drone['id']}, status: {drone['status']}")


if __name__ == '__main__':
    drone_repository = MemoryDroneRepository()
    drone1 = {"id": 1, "status": "idle"}
    drone2 = {"id": 2, "status": "flying"}
    drone_repository.add_drone(drone1)
    drone_repository.add_drone(drone2)
    list_all_drones(drone_repository)
    drone_repository.update_drone_status(1, status="charge")
    print("---------------------------------------")
    list_all_drones(drone_repository)
    drone_repository.remove_drone(2)
    print("---------------------------------------")
    list_all_drones(drone_repository)

