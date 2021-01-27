import pytest
from src.vector.vector import Vector


def test_constructor():
    a = Vector()
    assert a.a == 0
    assert a.b == 0


def test_eq_neq():
    a = Vector()
    b = Vector()
    assert a == b
    c = Vector(4, 6)
    assert a != c


@pytest.mark.parametrize('a, b, length', [
    (4, 2, 4.47),
    (-5, -2, 5.39)
])
def test_len(a, b, length):
    vector = Vector(a, b)
    assert vector.len() == length


def test_setters():
    vector = Vector()
    vector.a = 1
    assert vector.a == 1
    vector.b = 1
    assert vector.b == 1


def test_add_subtract():
    vector = Vector()
    vector_second = Vector(1, 1)
    vector += vector_second
    assert vector.a == 1
    assert vector.b == 1
    vector -= vector_second
    assert vector.a == 0
    assert vector.b == 0


@pytest.mark.parametrize('a, b, string', [
    (0, 0, '0.0 : x = 0.0, y = 0.0, direction: null vector'),
    (1, 0, '1.0 : x = 1.0, y = 0.0, direction: down')
])
def test_to_string(a, b, string):
    vector = Vector(a, b)
    assert str(vector) == string


def test_check_type_failed():
    vector = Vector()
    with pytest.raises(TypeError):
        vector += 12
