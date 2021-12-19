import unittest
from nose_parameterized import parameterized
from change_color.color import Colour


class ParametrizeTest(unittest.TestCase):
    @parameterized.expand([
        ['#0051F8', 50, '#0079FF'],
        ['#FEA9FB', 70, '#FFFFFF'],
        ['#95FC10', 20, '#B3FF13'],
    ])
    def test_lighten(self, code, percent, result):
        new_colour = Colour(code)
        assert new_colour.lighten(percent) == result, 'Тест с разными цветами'


class TestLighten(unittest.TestCase):
    def setUp(self) -> None:
        self.colour = Colour('#01E305')

    def test_lighten_100(self):
        self.assertEqual(self.colour.lighten(100), '#FFFFFF')

    def test_lighten_0(self):
        old_colour = str(self.colour)
        self.assertEqual(self.colour.lighten(0), old_colour)

    def test_lighten(self):
        self.assertEqual(self.colour.lighten(10), '#01FA05')

    def test_lighten_float(self):
        self.assertEqual(self.colour.lighten(12.5), '#01FF06')

    def test_over_light(self):
        new_colour = Colour('#FEA9FB')
        self.assertEqual(new_colour.lighten(70), '#FFFFFF')


class TestDarken(unittest.TestCase):
    def setUp(self) -> None:
        self.colour = Colour('#45A1F0')

    def test_darken_100(self):
        self.assertEqual(self.colour.darken(100), '#000000')

    def test_darken_0(self):
        old_colour = str(self.colour)
        self.assertEqual(self.colour.darken(0), old_colour)

    def test_darken(self):
        self.assertEqual(self.colour.darken(20), '#3781C0')

    def test_darken_float(self):
        self.assertEqual(self.colour.darken(55.33), '#1F486B')

    def test_over_dark(self):
        new_colour = Colour('#110012')
        self.assertEqual(new_colour.darken(70), '#050005')


class TestExceptions(unittest.TestCase):
    def test_wrong_rgb(self):
        with self.assertRaises(ValueError):
            Colour('blue')

    def test_high_percent(self):
        colour = Colour('#95FC10')
        with self.assertRaises(ValueError):
            colour.lighten(110)
        with self.assertRaises(ValueError):
            colour.darken(200)

    def test_negative_percent(self):
        colour = Colour('#B3FF13')
        with self.assertRaises(ValueError):
            colour.lighten(-10)
        with self.assertRaises(ValueError):
            colour.darken(-25.5)


if __name__ == '__main__':
    unittest.main()
