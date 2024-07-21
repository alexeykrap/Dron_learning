# пример использования паттерна Итератор на примере выбора кусочков пиццы:
from abc import ABC, abstractmethod
from typing import List


class PizzaItem:  # класс "Кусочек пиццы"
    def __init__(self, number):
        self._number = number  # номер кусочка

    def __str__(self):
        return f'кусочек пиццы под номером: {self._number}'


class Iterator(ABC):  # заготовка (абстрактный класс) для нашего будущего итератора
    @abstractmethod
    def next(self) -> PizzaItem:
        pass

    @abstractmethod
    def has_next(self) -> bool:
        pass


class PizzaSliceIterator(Iterator):
    def __init__(self, pizza: List[PizzaItem]):
        self._pizza = pizza
        self._index = 0

    def next(self) -> PizzaItem:
        pizza_item = self._pizza[self._index]
        self._index += 1
        return pizza_item

    def has_next(self) -> bool:
        return True if self._index < len(self._pizza) else False  # мой вариант


class PizzaAggregate:
    def __init__(self, amount_slices: int = 10):
        self.slices = [PizzaItem(it + 1) for it in range(amount_slices)]
        print(f"Приготовили пиццу и порезали на {amount_slices} кусочков")

    def amount_slices(self) -> int:
        return len(self.slices)

    def iterator(self) -> Iterator:
        return PizzaSliceIterator(self.slices)


if __name__ == "__main__":
    pizza = PizzaAggregate(5)
    iterator = pizza.iterator()
    while iterator.has_next():
        item = iterator.next()
        print("Это " + str(item))
    print("*" * 20)
    iterator = pizza.iterator()
    iterator.next()
    while iterator.has_next():
        item = iterator.next()
        print("Это " + str(item))

