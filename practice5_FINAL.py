import warnings
from abc import ABC, abstractmethod

warnings.filterwarnings('ignore', category=DeprecationWarning)

# ------------------Singleton--------------------
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

class MyClass:
    def test(self):
        return 'Привет из класса MyClass!'


class MyClassAdapter:
    def __init__(self, a: MyClass):
        print(a.test)


a = MyClass()
b = MyClassAdapter(a)


