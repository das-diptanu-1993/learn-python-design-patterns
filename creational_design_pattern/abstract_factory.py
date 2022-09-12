from __future__ import annotations
from abc import ABC, abstractmethod

# Creating the Abstract Facotry Skeleton

class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self) -> str:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        pass

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass
    
    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

# Generating Concrete Class for Factory-1

class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return 'Product-Type: {} | Product-Name: {}'.format('A', 'A1')

class ConcreateProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return 'Product-Type: {} | Product-Name: {}'.format('B', 'B1')

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return 'Collaboration b/n (Product-Type: {} | Product-Name: {}) & ({})'.format('B', 'B1', result)

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreateProductB1()

# Generating Concrete Class for Factory-2

class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return 'Product-Type: {} | Product-Name: {}'.format('A', 'A2')

class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return 'Product-Type: {} | Product-Name: {}'.format('B', 'B2')

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return 'Collaboration b/n (Product-Type: {} | Product-Name: {}) & ({})'.format('B', 'B2', result)

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

# Client-side code

def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f'{product_b.useful_function_b()}')
    print(f'{product_b.another_useful_function_b(product_a)}')

if __name__ == '__main__':

    print('Client: Testing client-code with factory-1:')
    client_code(ConcreteFactory1())

    print('\nClient: Testing client-code with factory-2:')
    client_code(ConcreteFactory2())





    