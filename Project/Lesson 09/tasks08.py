from abc import ABC, abstractmethod
import math

# task 1.1


class Shape(ABC):
    @abstractmethod
    def area(self):
        return "If you read this, I forgot to redefine area() method"


class Circle(Shape):
    def __init__(self, r: int | float):
        self.r = r

    def area(self):
        return math.pi * (self.r ** 2)


class Rectangle(Shape):
    def __init__(self, w: int | float, h: int | float):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Triangle(Shape):
    def __init__(self, a: int | float, h: int | float):
        self.a = a
        self.h = h

    def area(self):
        return self.a * self.h / 2


def total_area(shapes):
    return sum(s.area() for s in shapes)


# task 2.1


class Money:
    def __init__(self, amount: int | float, currency: str):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __str__(self):
        return f'{self.amount}{self.currency}'


# task 1.2


class Animal(ABC):
    @abstractmethod
    def speak(self):
        return None


class Cat(Animal):
    def speak(self):
        return 'Meow'


class Dog(Animal):
    def speak(self):
        return 'Argf'


class Bird(Animal):
    def speak(self):
        return 'Sqrl'


def make_animals_speak(animals):
    return (a.speak() for a in animals)


# task 2.2


class Team:
    def __init__(self, name: str, members: list[str]):
        self.name = name
        self.members = members

    def __contains__(self, item):
        return item in self.members

    def __str__(self):
        return f'Team {self.name}: {self.members}'


# task 1.3


class Transport(ABC):
    @abstractmethod
    def move(self, distance_km: float) -> str:
        return f'Moved {distance_km}km'

    @abstractmethod
    def cost(self, distance_km: float) -> float:
        return 0


class Car(Transport):
    def __init__(self, liters_per_100km: int | float, fuel_price: int | float):
        self.lit_100km = liters_per_100km
        self.price = fuel_price

    def move(self, distance_km: float) -> str:
        return super(Car, self).move(distance_km)

    def cost(self, distance_km: float) -> float:
        return distance_km * self.lit_100km / 100 * self.price


class Bike(Transport):
    def move(self, distance_km: float) -> str:
        return super(Bike, self).move(distance_km)

    def cost(self, distance_km: float) -> float:
        return 0


class Bus(Transport):
    def __init__(self, fare_per_km: int | float):
        self.fare = fare_per_km

    def move(self, distance_km: float) -> str:
        return super(Bus, self).move(distance_km)

    def cost(self, distance_km: float) -> float:
        return self.fare * distance_km


def trip_report(vehicles: list, distance_km: float) -> None:
    for v in vehicles: print(v.move(distance_km))
    print('-'*40)
    c = [v.cost(distance_km) for v in vehicles]
    print(*c, sep='\n')
    print('-' * 40)
    print(max(c))


# task 2.3


class Playlist:
    def __init__(self, tracks: list[str]):
        self.tracks = tracks

    def __len__(self):
        return len(self.tracks)

    def __getitem__(self, item: int):
        return self.tracks[item]

    def __str__(self):
        return f'Playlist({len(self.tracks)}): {self.tracks}'


# task 2.4


class MathBoom:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __add__(self, other):
        return self.args * other.args

    def __sub__(self, other):
        return '+'

    def __mul__(self, other):
        return other.args, 'UwU'

    def __matmul__(self, other):
        return 'No matrix today gal'

    def __truediv__(self, other):
        return bin(1986)

    def __floordiv__(self, other):
        return [i+['*' for i in range(len(other.args))] for i in other.args]

    def __mod__(self, other):
        return '|||\n|||\n|||'

    def __divmod__(self, other):
        raise ValueError('You picked the wrong house, fool!')

    def __pow__(self, power, modulo=33):
        return power*modulo

    def __lshift__(self, other):
        return "I don't wanna do it..."

    def __rshift__(self, other):
        return other*math.pi

    def __and__(self, other):
        return set(self.args) | set(other.args)

    def __xor__(self, other):
        return 'Have you really read all of these?'

    def __or__(self, other):
        return set(self.args) & set(other.args)


