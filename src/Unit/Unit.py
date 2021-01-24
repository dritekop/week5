from typing import Any


def prettify_string(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f'value should be of type str: {value}')

    value = value.strip().lower()
    value = value.capitalize()
    return value


def check_numeric(value: int):
    value = int(value)
    if value < 0:
        raise ValueError(f'value should be positive, got {value} instead')
    elif value == 0:
        return 0
    return value


def check_attack(value: int):
    dmg = check_numeric(value)
    dmg *= -1
    if dmg > 0:
        print('Are you healer? OK!')


class UnitIsDeadException(Exception):
    pass


class Unit:
    def __init__(self, name: str, hp: int, damage: int) -> None:
        self._name = prettify_string(name)
        self._hp = check_numeric(hp)
        self._max_hp = check_numeric(hp)
        self._damage = check_numeric(damage)

    @property
    def name(self) -> str:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def max_hp(self) -> int:
        return self._max_hp

    @property
    def damage(self) -> int:
        return self._damage

    @hp.setter
    def hp(self, value) -> None:
        self._hp = check_numeric(value)

    def __str__(self) -> str:
        return f'{self.name}: ({self.hp}/{self.max_hp}), damage is {self.damage} points'

    def __ensure_is_alive(self):
        if self.hp == 0:
            print(f'Warrior {self.name} is dead')
            raise UnitIsDeadException()

    def add_hp(self, value: int) -> None:
        self.hp += value

    def take_damage(self, value: int) -> None:
        if self.hp - value <= 0:
            self.hp = 0
        else:
            self.hp -= value
        self.__ensure_is_alive()

    def __check_type(self, other) -> None:
        if not isinstance(other, self.__class__):
            raise TypeError(f'This guy is ugly {other.__class__.__name__}, but not {self.__class__.__name__} ')

    def attack(self, other: Any) -> None:
        other.__ensure_is_alive()
        self.__ensure_is_alive()
        self.__check_type(other)
        other.take_damage(self.damage)
        self.counter_attack(other)

    def counter_attack(self, other):
        self.__ensure_is_alive()
        counter_dmg = other.damage / 2
        self.take_damage(counter_dmg)


if __name__ == '__main__':  # pragma: no cover
    unit = Unit('SoLdIeR', 100, 15)
    print(unit)

    inut = Unit('Regurel', 45, 12)
    print(inut)
    print()

    inut.attack(unit)
    print(unit)
    print(inut)
    print()

    try:
        for i in range(4):
            unit.attack(inut)
            print(unit)
            print(inut)
            print()
    except UnitIsDeadException:
        print(unit)
        print(inut)
