import pytest
from src.complex.complex import Complex


def test_complex_construction():
    complex_number = Complex(1, 1)
    assert complex_number.re == 1
    assert complex_number.im == 1


def test_eq_ne():
    complex_number = Complex(1, 1)
    complex_number_second = Complex(1, 1)
    complex_number_third = Complex()
    assert complex_number == complex_number_second
    assert complex_number_third != complex_number


def test_add_sub():
    complex_number = Complex(5, -1)
    complex_number_second = Complex(4, 3)
    complex_number += complex_number_second
    complex_number_second -= complex_number
    assert complex_number.re == 9 and complex_number.im == 2
    assert complex_number_second.re == -5 and complex_number_second.im == 1


def test_mul():
    complex_number = Complex(5, -1)
    complex_number_second = Complex(4, 3)
    complex_number *= complex_number_second
    assert complex_number.re == 23 and complex_number.im == 11


@pytest.mark.parametrize('a, b, result', [
    (4, 3, 5),
    (-2, 6, 6.325)
])
def test_abs(a, b, result):
    complex_number = Complex(a, b)
    assert abs(complex_number) == result


@pytest.mark.parametrize('a, b, result', [
    (4, 3, '4 + 3i'),
    (4, -3, '4 - 3i'),
    (0, 0, '0'),
    (0, 3, '3i'),
    (3, 0, '3'),
    (0, -3, '-3i'),
    (3, 1, '3 + i'),
    (3, -1, '3 - i')
])
def test_to_string(a, b, result):
    complex_numb = Complex(a, b)
    assert str(complex_numb) == result


def test_check_type_failed():
    com_numb = Complex()
    with pytest.raises(TypeError):
        com_numb += 1
