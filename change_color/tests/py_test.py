import pytest
from change_color.color import Colour
# pytest --cov - для вывода coverage


@pytest.fixture(params=['#01E305'])
def new_colour(request):
    """Фикстура, инициализирующая экземпляр класса Colour"""
    colour = Colour(request.param)
    return colour

# Тестирование метода lighten


def test_lighten_100(new_colour):
    assert new_colour.lighten(100) == '#FFFFFF', 'Тест на полное осветление'


def test_lighten_0(new_colour):
    old_colour = str(new_colour)
    assert new_colour.lighten(0) == old_colour, 'Тест на неизменение цвета'


@pytest.mark.parametrize('code, percent, result', [
    ('#0051F8', 50, '#0079FF'),
    ('#FEA9FB', 70, '#FFFFFF'),
    ('#95FC10', 20, '#B3FF13')
])
def test_lighten(code, percent, result):
    new_colour = Colour(code)
    assert new_colour.lighten(percent) == result, 'Тест с разными цветами'


@pytest.mark.parametrize('percent', [-0.25, 150])
def test_wrong_per_light(new_colour, percent):
    with pytest.raises(ValueError) as ex:
        new_colour.lighten(percent)
    assert 'Процент осветления должен быть от 0 до 100 %' \
           == ex.value.args[0], 'Тест с некорректным процентом'

# Тестирование метода darken


def test_darken_100(new_colour):
    assert new_colour.darken(100) == '#000000', 'Тест на полное затемнение'


def test_darken_0():
    colour = Colour('#E26FA5')
    old_colour = str(colour)
    assert colour.darken(0) == old_colour, 'Тест на неизменение цвета'


@pytest.mark.parametrize('code, percent, result', [
    ('#15F47A', 50, '#0B7A3D'),
    ('#110012', 70, '#050005'),
    ('#45A1F0', 20, '#3781C0')
])
def test_darken(code, percent, result):
    new_colour = Colour(code)
    assert new_colour.darken(percent) == result, 'Тесты с разными цветами'


@pytest.mark.parametrize('percent', [-20, 100.75])
def test_wrong_per_dark(new_colour, percent):
    with pytest.raises(ValueError) as ex:
        new_colour.darken(percent)
    assert 'Процент затемнения должен быть от 0 до 100 %'\
           == ex.value.args[0], 'Тесты с недопустимым процентом'


@pytest.mark.xfail(raises=ValueError, strict=True)
def test_with_wrong_code():
    """Тест задуман как провальный, неверно передан цвет в конструктор"""
    Colour('red')
