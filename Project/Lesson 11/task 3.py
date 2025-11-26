class Temperature:
    def __init__(self, c: float | int):
        self._c = c
        self._f = c * 1.8 + 32

    @property
    def celsius(self):
        return self._c

    @celsius.setter
    def celsius(self, value: float | int):
        if value <= -273.15:
            raise ValueError('Too low!')
        else:
            self._c = value
            self._f = self._c * 1.8 + 32

    @property
    def fahrenheit(self):
        return self._f


t = Temperature(0)
print(t.fahrenheit)
t.celsius = -300



