# паттерн Наблюдатель (Observer)
from abc import ABC, abstractmethod
import cv2

class Observer(ABC):  # наблюдатель
    @abstractmethod
    def update(self, message: str, image=None):
        pass


class Observable:  # наблюдаемый
    def __init__(self):
        self._observers = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self, message: str, image=None):
        if self._observers:
            for observer in self._observers:
                observer.update(message, image)


class DataLogger(Observer):
    def update(self, message: str, image=None):
        print(f"Система записи получила сообщение {message}")
        if image is not None:
            self.save_image(image)

    @staticmethod
    def save_image(image):
        filename = "camera.png"
        cv2.imwrite(filename, image)
        print(f"Снимок сохранён!")


class AlertSystem(Observer):
    def update(self, message: str, image=None):
        print(f"Система предупреждений получила сообщение {message}")


class AnalysisSystem(Observer):
    def update(self, message: str, image=None):
        print(f"Система анализа получила сообщение {message}")


class Camera(Observable):
    def __init__(self):
        super().__init__()
        self._zoom_lvl = 1.0

    def set_zoom(self, zoom_lvl: float):
        self._zoom_lvl = zoom_lvl
        self.notify_observers(f"Зум установлен на {self._zoom_lvl}")

    def take_image(self):
        caption = cv2.VideoCapture(0)
        meta, frame = caption.read()
        if meta:
            self.notify_observers("Захвачено изображение!", frame)
        caption.release()


data_logger = DataLogger()
alert_system = AlertSystem()
analysis_system = AnalysisSystem()

camera = Camera()

camera.add_observer(data_logger)
camera.add_observer(alert_system)
camera.add_observer(analysis_system)

camera.set_zoom(2.0)
camera.take_image()

