import time


# task 1

class Rectangle:
    def __init__(self, w: float, h: float):
        self.w, self.h = w, h

    def area(self) -> float:
        return self.w * self.h

    def perimeter(self) -> float:
        return (self.w + self.h) * 2

    def scale(self, k) -> None:
        self.w, self.h = self.w * 2, self.h * 2


# task 2

class Point:
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y

    def move(self, dx: float, dy: float) -> None:
        self.x, self.y = self.x + dx, self.y + dy

    def distance_to(self, other) -> float:
        return ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5


# task 3

class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner, self.balance = owner, balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> bool | tuple[float, float]:
        if amount > self.balance: self.balance -= amount; return amount, self.balance
        else: return False

    def get_balance(self) -> float:
        return self.balance


# task 4

class TodoList:
    def __init__(self):
        self.tasks = set()

    def add(self, text: str) -> None:
        self.tasks.add(text)

    def remove(self, text: str) -> None:
        self.tasks.remove(text) if text in self.tasks else 'UwU'

    def has(self, text: str) -> bool:
        return True if text in self.tasks else False

    def list(self) -> set:
        return self.tasks

    def count(self) -> int:
        return len(self.tasks)


# task 5

class Timer:
    def __init__(self):
        self.t = []

    def start(self) -> None:
        self.t.append(time.perf_counter())

    def stop(self) -> None:
        self.t[-1] = time.perf_counter() - self.t[-1]

    def elapsed(self) -> float:
        return sum(self.t)


# task 6

class Student:
    def __init__(self, name: str, grades: list):
        self.name, self.grades = name, grades

    def add_grade(self, x: int) -> None:
        self.grades.append(x)

    def avg(self) -> float:
        return sum(self.grades)/len(self.grades) if len(self.grades) > 0 else 0

    def best(self) -> int | None:
        return max(self.grades) if len(self.grades) > 0 else None


# task 7

class ShoppingCart:
    def __init__(self):
        self.its = {}

    def add_item(self, name: str, price: float) -> None:
        self.its[name] = price

    def remove_item(self, name: str) -> None:
        self.its.pop(name)

    def total(self) -> float:
        return sum(self.its.items())

    def items(self) -> list[*tuple]:
        return [(k, self.its[k]) for k in self.its]
