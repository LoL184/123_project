# task 1

class Rectangle:
    def __init__(self, w: int, h: int):
        self._w, self._h = w, h

    @property
    def get(self) -> tuple[int | float, int | float]:
        return self._w, self._h

    @get.setter
    def get(self, value: tuple[int, int]):
        if value[0] <= 0 or value[1] <= 0:
            raise ValueError("Wrong input")
        self._w, self._h = value

    def rect(self):
        return self._w * self._h, (self._w + self._h) * 2



