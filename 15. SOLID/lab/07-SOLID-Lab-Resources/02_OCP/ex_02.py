from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

def animal_sound(animals: list[Animal]):
    for animal in animals:
        print(animal.make_sound())

class Dog(Animal):
    def make_sound(self):
        return "woof-woof"

class Cat(Animal):
    def make_sound(self):
        return "meow"

class Chicken(Animal):
    def make_sound(self):
        return "cluck"

animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
