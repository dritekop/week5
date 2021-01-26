import pytest

from src.gun.gun import Gun, check_numeric, prettify_string


def test_prettify_string_failed():
    with pytest.raises(TypeError):
        name = prettify_string(100)


def test_check_numeric_failed():
    with pytest.raises(ValueError):
        a = check_numeric(0)
    with pytest.raises(TypeError):
        a = check_numeric(1.)


@pytest.mark.parametrize('name, value', [
    ('Colt', 10),
    ('Beretta', 5)
])
def test_gun_construction(name, value):
    gun = Gun(name, value)
    assert gun.model == name
    assert gun.capacity == value
    assert gun.amount == value
    assert gun.total_shots == 0
    assert gun.is_ready == False


def test_shoot_and_reload():
    gun = Gun('Colt', 5)
    with pytest.raises(ValueError):
        gun.shoot()
    with pytest.raises(ValueError):
        for i in range(6):
            gun.prepare()
            gun.shoot()
    gun.reload()
    assert gun.amount == 5


def test_gun_to_string():
    gun = Gun('Colt', 10)
    assert str(gun) == 'Colt : (10, 10), Not prepared to shoot'
    gun.prepare()
    assert str(gun) == 'Colt : (10, 10), Prepared to shoot'
