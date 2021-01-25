import pytest

from src.point.point import Point
from src.car.car import Car, check_numeric, prettify_string, prettify_point, OutOfFuel


def test_car_construction():
    place = Point(0, 2)
    car = Car(15, 0.5, 'Bugatti', place)
    assert car.capacity == 15
    assert car.amount == 15
    assert car.consumption == 0.5
    assert car.model == 'Bugatti'
    assert car.location == place


def test_car_construction_failed():
    place = Point(0, 2)
    with pytest.raises(ValueError):
        car = Car(15, 16, 'Bugatti', place)
        x = car.consumption


def test_check_numeric():
    with pytest.raises(ValueError):
        x = check_numeric(-2)


def test_prettify_string():
    with pytest.raises(TypeError):
        name = prettify_string(100)


def test_prettify_point():
    with pytest.raises(TypeError):
        start = prettify_point(100)


def test_drive():
    place = Point(0, 2)
    far_place = Point(1425, 1365)
    place_two = Point(1, 1)
    car = Car(10, 0.5, 'Renault', place)

    car.drive(place_two)
    assert car.location == place_two

    with pytest.raises(OutOfFuel):
        car.drive(far_place)


def test_drive_to():
    place = Point(0, 2)
    car = Car(10, 0.5, 'Renault', place)

    car.drive_to(1, 5)

    with pytest.raises(TypeError):
        car.drive_to(1, 2.5)


def test_refill():
    place = Point(0, 2)
    destination = Point(0, 10)
    car = Car(10, 0.5, 'Renault', place)

    car.drive(destination)

    car.refill(3)

    assert car.amount == 9

    with pytest.raises(ValueError):
        car.refill(8)


def test_car_to_string():
    place = Point(0, 2)
    car = Car(10, 0.5, 'Renault', place)

    assert str(car) == 'Renault : (10.00 l/10.0l, point of location: (0.0, 2.0)'
