from math import hypot
from typing import Any


class Complex:
    def __init__(self, re: float = 0, im: float = 0) -> None:
        self._re = float(re)
        self._im = float(im)

    @property
    def re(self) -> float:
        return self._re

    @property
    def im(self) -> float:
        return self._im

    def __eq__(self, other) -> bool:
        self.__check_type(other)
        return self.re == other.re and self.im == other.im

    def __ne__(self, other) -> bool:
        self.__check_type(other)
        return not self.re == other.re or self.im == other.im

    def __add__(self, other) -> Any:
        self.__check_type(other)
        result = Complex()
        result._re = self.re + other.re
        result._im = self.im + other.im
        return result

    def __sub__(self, other) -> Any:
        self.__check_type(other)
        result = Complex()
        result._re = self.re - other.re
        result._im = self.im - other.im
        return result

    def __mul__(self, other) -> Any:
        self.__check_type(other)
        result = Complex()
        result._re = self.re * other.re - self.im * other.im
        result._im = self.im * other.re + other.im * self.re
        return result

    def __abs__(self) -> float:
        result_abs = "{:.3f}".format(hypot(self.re, self.im))
        return float(result_abs)

    def __str__(self) -> str:
        if self.im == 0:
            formatted = '{0:g}'.format(self.re)
            string = f'{formatted}'
        elif self.im < 0:
            if self.im == -1 and self.re != 0:
                formatted = '{0:g}'.format(self.re)
                string = f'{formatted} - i'
            elif self.re == 0:
                formatted = '{0:g}'.format(self.im)
                string = f'{formatted}i'
            else:
                transformed_im = '{0:g}'.format(self.im * -1)
                formatted = '{0:g}'.format(self.re)

                string = f'{formatted} - {transformed_im}i'
        else:
            if self.im == 1 and self.re != 0:
                formatted = '{0:g}'.format(self.re)
                string = f'{formatted} + i'
            elif self.re == 0:
                formatted = '{0:g}'.format(self.im)
                string = f'{formatted}i'
            else:
                formatted_re = '{0:g}'.format(self.re)
                formatted_im = '{0:g}'.format(self.im)
                string = f'{formatted_re} + {formatted_im}i'
        return string

    def __check_type(self, other) -> None:
        if not isinstance(other, self.__class__):
            raise TypeError(f'Other parameter should be of type {self.__class__.__name__}')


if __name__ == '__main__':  # pragma no cover
    print('no cover')
