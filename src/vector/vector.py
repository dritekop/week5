from math import hypot
from typing import Any


class Vector:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self._a = float(x)
        self._b = float(y)

    @property
    def a(self) -> float:
        return self._a

    @property
    def b(self) -> float:
        return self._b

    @a.setter
    def a(self, value) -> None:
        self._a = float(value)

    @b.setter
    def b(self, value) -> None:
        self._b = float(value)

    def len(self) -> float:
        length = hypot(self.a, self.b)
        length = "{:.2f}".format(length)
        return float(length)

    def __eq__(self, other) -> bool:
        self.__check_type(other)
        return self.a == other.a and self.b == other.b

    def __ne__(self, other) -> bool:
        self.__check_type(other)
        return not self == other

    def __add__(self, other) -> Any:
        self.__check_type(other)
        result = Vector()
        result.a = self.a + other.a
        result.b = self.b + other.b
        return result

    def __sub__(self, other) -> Any:
        self.__check_type(other)
        result = Vector()
        result.a = self.a - other.a
        result.b = self.b - other.b
        return result

    def __str__(self) -> str:
        direction = 'up'
        if self.b < self.a:
            direction = 'down'
        elif self.b == 0 and self.a == 0:
            direction = 'null vector'
        return f'{self.len()} : x = {self.a}, y = {self.b}, direction: {direction}'

    def __check_type(self, other: Any) -> None:
        if not isinstance(other, self.__class__):
            raise TypeError(f'Other param should be of type {self.__class__.__name__}')


if __name__ == '__main__':  # pragma: no cover
    print('no cover')
