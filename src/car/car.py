from src.point.point import Point


def check_numeric(value) -> float:
    if value <= 0:
        raise ValueError(f'Value {value} should be positive')
    else:
        return value


def prettify_string(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f'Value should be of type str: {value}')

    value = value.strip().lower()
    value = value.capitalize()
    return value


def prettify_point(value: Point) -> Point:
    if not isinstance(value, Point):
        raise TypeError(f'Value should be of type Point: {value}')

    return value


def check_coordinate(x) -> int:
    if not isinstance(x, int):
        raise TypeError(f'Wrong type of coordinate, must be integers')

    return x


class OutOfFuel(Exception):
    pass


class TooMuchFuel(Exception):
    pass


class Car:
    def __init__(self, capacity: float, consumption: float, model: str, location: Point) -> None:
        self._capacity = float(check_numeric(capacity))
        self._amount = float(check_numeric(capacity))
        self._consumption = float(check_numeric(consumption))
        self._model = prettify_string(model)
        self._location = prettify_point(location)
        if self._consumption > self._capacity:
            raise ValueError(f'No sense value of consumption {self._consumption}, \
                             because capacity of tank is {self._capacity}')

    @property
    def capacity(self) -> float:
        return self._capacity

    @property
    def amount(self) -> float:
        return self._amount

    @property
    def consumption(self) -> float:
        return self._consumption

    @property
    def model(self) -> str:
        return self._model

    @property
    def location(self) -> Point:
        return self._location

    @amount.setter
    def amount(self, value) -> None:
        if check_numeric(value) > self._capacity:
            raise ValueError(f'Tank is full')
        self._amount = check_numeric(value)

    def drive(self, destination) -> None:
        destination = prettify_point(destination)
        way = self._location.distance(destination)
        fuel_needed = float(way) * self._consumption

        if fuel_needed > self._amount:
            raise OutOfFuel(f'lack of fuel, refill your car')

        self._location = destination
        self._amount -= fuel_needed

    def drive_to(self, x: float, y: float) -> None:
        x = check_coordinate(x)
        y = check_coordinate(y)
        destination = Point(x, y)
        self.drive(destination)

    def refill(self, value) -> None:
        self.amount += check_numeric(value)

    def __str__(self) -> str:
        amount = "{:.2f}".format(self._amount)
        return f'{self.model} : ({amount} l/{self.capacity}l, point of location: {self.location}'


if __name__ == '__main__':  # pragma: no cover
    print('test')
