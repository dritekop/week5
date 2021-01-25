import pytest

from src.Unit.Unit import Unit, UnitIsDeadException, check_numeric, prettify_string


@pytest.mark.parametrize('actual, expected', [
    ('soldier', 'Soldier'),
    (' dora\t', 'Dora'),
    ('dRAKE', 'Drake')
])
def test_prettify_string(actual, expected):
    assert prettify_string(actual) == expected


@pytest.mark.parametrize('value, get_back', [
    (1, 1),
    (0, 0)
])
def test_check_numeric(value, get_back):
    assert check_numeric(value) == get_back


@pytest.mark.parametrize('value', [
    -2,
    'arrest'
])
def test_check_numeric_failed(value):
    with pytest.raises(ValueError):
        check_numeric(value)


@pytest.mark.parametrize('name, hp, damage', [
    ('Soldier', 100, 20),
    ('Samurai', 120, 10),
])
def test_unit_construction(name, hp, damage):
    soldier = Unit(name, hp, damage)
    assert soldier.name == name
    assert soldier.hp == hp
    assert soldier.max_hp == hp
    assert soldier.damage == damage


def test_setter():
    soldier = Unit('Sol', 13, 4)

    soldier.hp += 14
    assert soldier.hp == 13

    soldier.hp = 120
    assert soldier.hp == 13

    with pytest.raises(TypeError):
        warrior = Unit(123, 12, 14)


def test_add_hp():
    soldier = Unit("Soldier", 15, 5)
    with pytest.raises(UnitIsDeadException):
        soldier.add_hp(5)
    soldier.hp = 10
    soldier.add_hp(3)
    assert soldier.hp == 13


def test_check_type():
    soldier = Unit('Soldier', 15, 10)

    with pytest.raises(TypeError):
        soldier.attack('somebody')


def test_ensure_is_alive():
    soldier = Unit('Sol', 13, 4)

    with pytest.raises(UnitIsDeadException):
        soldier.take_damage(14)


def test_attack_counter_attack():
    soldier = Unit("Soldier", 15, 5)
    warrior = Unit('warrior', 15, 5)

    soldier.attack(warrior)
    assert soldier.hp == 13
    assert warrior.hp == 10


def test_unit_to_string():
    soldier = Unit('Sol', 13, 4)

    assert str(soldier) == 'Sol: (13/13), damage is 4 points'
