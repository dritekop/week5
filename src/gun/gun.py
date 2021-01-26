import src.car.car


def check_numeric(value) -> int:
    if not isinstance(value, int):
        raise TypeError(f'Value should have integer type')
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


class Gun:
    def __init__(self, model: str, capacity: int) -> None:
        self._amount = check_numeric(capacity)
        self._capacity = check_numeric(capacity)
        self._model = prettify_string(model)
        self._total_shots = 0
        self._is_ready = False

    @property
    def amount(self) -> int:
        return self._amount

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def model(self) -> str:
        return self._model

    @property
    def total_shots(self) -> int:
        return self._total_shots

    @property
    def is_ready(self) -> bool:
        return self._is_ready

    def reload(self) -> None:
        self._amount = self.capacity

    def prepare(self) -> None:
        if not self.is_ready:
            self._is_ready = True

    def shoot(self) -> None:
        if not self.is_ready:
            raise ValueError(f'Prepare gun before shoot')
        if self.amount == 0:
            raise ValueError(f'There is no bullets. Reload gun')
        print('Bang!')
        self._amount -= 1
        self._total_shots += 1
        self._is_ready = False

    def __str__(self) -> str:
        if self.is_ready and self.amount > 0:
            info = 'Prepared to shoot'
        else:
            info = 'Not prepared to shoot'
        return f'{self.model} : ({self.amount}, {self.capacity}), {info}'


if __name__ == '__main__':  # pragma: no cover
    colt = Gun('Colt', 10)
    print(colt)
    colt.prepare()
    print(colt)
    colt.shoot()
    print(colt)
    try:
        for i in range(10):
            colt.prepare()
            colt.shoot()
            print(colt)
    except ValueError:
        print(colt)