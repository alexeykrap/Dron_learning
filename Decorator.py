from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):
    def __init__(self, component):
        self.component = component

    @abstractmethod
    def operation(self):
        pass


class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f'ConcreteDecoratorA({self.component.operation()})'


class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f'ConcreteDecoratorB({self.component.operation()})'

if __name__ == '__main__':
    concreteComponent = ConcreteComponent()
    print(concreteComponent.operation())
    decoratorA = ConcreteDecoratorA(concreteComponent)
    decoratorB = ConcreteDecoratorB(decoratorA)
    print(decoratorB.operation())