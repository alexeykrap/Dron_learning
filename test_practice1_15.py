import unittest
from practice1_15 import Drone


class TestDrone(unittest.TestCase):
    def setUp(self):
        self.drone = Drone()

    def test_takeoff(self):
        # уровень заряда высокий
        self.drone.battery_level = 50
        result = self.drone.takeoff()
        self.assertTrue(self.drone.is_flying)
        self.assertEqual(result, 'Дрон взлетел')
        # уровень заряда низкий
        self.drone.battery_level = 10
        result = self.drone.takeoff()
        self.assertFalse(self.drone.is_flying)
        self.assertEqual(result, 'Взлёт не удался. Проверьте уровень заряда батареи')

    def test_land_not_flying(self):  # тест для приземления, если уже на земле
        self.drone.is_flying = False
        result = self.drone.langing()
        self.assertFalse(self.drone.is_flying)
        self.assertEqual(result, 'Дрон уже на земле')

    def test_land_flying(self):  # тест для приземления, если дрон в воздухе
        self.drone.is_flying = True
        result = self.drone.langing()
        self.assertFalse(self.drone.is_flying)
        self.assertEqual(result, 'Дрон приземлился')


if __name__ == 'main':
    unittest.main()