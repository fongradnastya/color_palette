import re


class Colour:
    """
    Класс Colour служит для хранения rgb цветов и манипуляций с ними
    Он содержит 2 публичных метода: darken и lighten
    и 3 публичных атрибута: red, green, blue, хранящих составляющие цвета
    """
    def __new__(cls, colour_code: str):
        """
        Метод __new__ проверяет корректность переданного цветового кода
        :param colour_code: rgb код цвета
        """
        pattern = r'#[\dA-F]{6}'
        if re.fullmatch(pattern, colour_code):
            return super().__new__(cls)
        else:
            raise ValueError('Передан некорректный цветовой код')

    def __init__(self, colour_code: str):
        """
        Метод __init__ создаёт атрибут класса, разделяя переданный код
        на 3 составляющие
        :param colour_code: rgb код цвета
        """
        self.red = int(colour_code[1:3], 16)
        self.green = int(colour_code[3:5], 16)
        self.blue = int(colour_code[5:7], 16)

    def __str__(self):
        """
        Преобразует текущий цвет в rgb код
        :return: строка с кодом в стандартном формате rgb
        """
        colour_code = "#{:0>2x}{:0>2x}{:0>2x}".format(
            self.red, self.green, self.blue)
        return colour_code.upper()

    def _change_colour(self, colour: str, percent: float, is_dark: int):
        """
        Служебный метод _change_colour изменяет один из трёх составных
        цвета на заданный процент
        :param colour: цветовая составляющая: red, green или blue
        :param percent: вещественное число в диапазоне от 0 до 100
        :param is_dark: 0 - если нужно сделать цвет темнее, 1 - если светлее
        :return:
        """
        attribute = getattr(self, colour)
        if attribute == 0 and is_dark == 1:
            attribute = round(percent * 255 / 100)
        else:
            attribute += round(attribute * percent / 100) * is_dark
        if attribute > 255:
            attribute = 255
        setattr(self, colour, attribute)

    def lighten(self, percent: float) -> str:
        """
        Метод lighten осветляет текущий цвет на заданный процент
        :param percent: вещественное число в диапазоне от 0 до 100
        :return: rgb код нового цвета в виде строки
        """
        if percent == 100:
            self.red = self.blue = self.green = 255
            return '#FFFFFF'
        elif percent > 100 or percent < 0:
            raise ValueError('Процент осветления должен быть от 0 до 100 %')
        elif percent != 0:
            self._change_colour('red', percent, 1)
            self._change_colour('green', percent, 1)
            self._change_colour('blue', percent, 1)
        return str(self)

    def darken(self, percent: float) -> str:
        """
        Метод darken делает текущий цвет на заданный процент темнее
        :param percent: вещественное число в диапазоне от 0 до 100
        :return: rgb код нового цвета в виде строки
        """
        if percent == 100:
            self.red = self.blue = self.green = 0
            return '#000000'
        elif percent > 100 or percent < 0:
            raise ValueError('Процент затемнения должен быть от 0 до 100 %')
        elif percent != 0:
            self._change_colour('red', percent, -1)
            self._change_colour('green', percent, -1)
            self._change_colour('blue', percent, -1)
        return str(self)
