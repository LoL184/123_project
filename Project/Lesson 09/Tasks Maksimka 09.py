from abc import ABC, abstractmethod
from tasks08 import Car, Bike, Bus, trip_report  # for task 1

# task 1


class Transport(ABC):
    @abstractmethod
    def move(self, distance_km: float) -> str:
        return f'Moved {distance_km}km'

    @abstractmethod
    def cost(self, distance_km: float) -> float:
        return 0


class ElectricCar(Transport):
    def __init__(self, battery_capacity: float, energy_consumption_per_100km: float,
                 electricity_price_rub_for_kwh) -> None:
        self.battery_capacity = battery_capacity
        self.energy_consumption = energy_consumption_per_100km
        self.electricity_price = electricity_price_rub_for_kwh

    def move(self, distance_km: float) -> str:
        return super(ElectricCar, self).move(distance_km)

    def cost(self, distance_km: float) -> float | str:
        return distance_km * self.energy_consumption / 100 * self.electricity_price \
            if (distance_km * self.energy_consumption / 100) <= self.battery_capacity \
            else f'{self.battery_capacity * self.electricity_price} for full battery and need to refuel'


# task 2


class Playlist:
    def __init__(self, tracks: list[str]):
        self.tracks = tracks

    def __len__(self):
        return len(self.tracks)

    def __getitem__(self, item: int) -> str | list:
        return self.tracks[item]

    def __str__(self) -> str:
        return f'Playlist({len(self.tracks)}): {self.tracks}'

    def __add__(self, other: str):
        self.tracks.append(other)

    def __iadd__(self, other: str):  # same as __add__ but works with +=
        self.tracks.append(other)

    def __eq__(self, other) -> bool:
        return self.tracks == other.tracks

    def __iter__(self) -> list:
        return self.tracks
