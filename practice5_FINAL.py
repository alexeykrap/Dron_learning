import warnings
from abc import ABC, abstractmethod

warnings.filterwarnings('ignore', category=DeprecationWarning)

# ------------------Singleton--------------------
print("\nSingleton\n")


class MySingleton:
    _instance = 0

    def __init__(self):
        if not MySingleton._instance:
            MySingleton._instance = self

    def get_instance(self):
        return self._instance


a1 = MySingleton()
a2 = MySingleton()

print(a1.get_instance())
print(a2.get_instance())
is_equal = a1.__eq__(a2)
if is_equal:
    print("Они одинаковые!")
else:
    print("Как так-то?")

# ------------------Adapter--------------------
print("\nAdapter\n")
class MyClass:
    def test(self):
        print(f"Привет из класса {self.__class__.__name__}")


class MyClassAdapter:
    def __init__(self, my_class: MyClass):
        self.my_class = my_class


my_class = MyClass()
my_class_adapter = MyClassAdapter(my_class)

my_class_adapter.my_class.test()

# ------------------Decorator------------------
print("\nDecorator\n")


def my_decorator(my_func):
    print(f"Это работает декоратор функции {my_func.__name__}")
    my_func()
    return my_func


# встроенный механизм декорирования
# @my_decorator
def my_function():
    print(f"А это работает сама функция my_function")


my_function = my_decorator(my_function)  # вместо этой строчки можно использовать @my_decorator сразу над функцией

