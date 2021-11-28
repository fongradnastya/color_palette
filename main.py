class Colour:
    """
    Класс Colour служит для хранения цветов в rgb кодировке
    """
    def __init__(self, colour_code: str):
        self.red = int(colour_code[1:3], 16)
        self.green = int(colour_code[3:5], 16)
        self.blue = int(colour_code[5:7], 16)

    def __str__(self):
        colour_code = "#{:0>2x}{:0>2x}{:0>2x}".format(
            self.red, self.green, self.blue)
        return colour_code.upper()

    def _change_colour(self, colour: str, percent: int, is_dark: int):
        """
        Служебный метод _change_colour изменяет обин из трёх составных
        цвета на заданный процент
        """
        attribute = getattr(self, colour)
        attribute += round(attribute * percent / 100) * is_dark
        if attribute > 255:
            attribute = 255
        elif attribute < 0:
            attribute = 0
        setattr(self, colour, attribute)

    def lighten(self, percent: int) -> str:
        """
        Метод lighten осветляет цвет на заданный процент
        """
        if percent == 100:
            self.red = self.blue = self.green = 255
            return '#FFFFFF'
        self._change_colour('red', percent, 1)
        self._change_colour('green', percent, 1)
        self._change_colour('blue', percent, 1)
        return str(self)

    def darken(self, percent: int) -> str:
        """
        Метод darken затемняет цвет на заданный процент
        """
        if percent == 100:
            self.red = self.blue = self.green = 0
            return '#000000'
        self._change_colour('red', percent, -1)
        self._change_colour('green', percent, -1)
        self._change_colour('blue', percent, -1)
        return str(self)


def check_on_examples():
    """
    Функция check_on_examples демонстрирует работу класса Colour
    на примерах
    """
    first_colour = Colour('#02E305')
    print(f'{first_colour} был преобразован к {first_colour.lighten(50)}')
    second_colour = Colour('#15F47A')
    print(f'{second_colour} был преобразован к {second_colour.darken(10)},'
          f'а затем обратно к {second_colour.lighten(10)}')
    black = Colour('#000000')
    print(f'{black} был преобразован к {black.lighten(100)}')
    new_colour = Colour('#99CCFF')
    print(f'{new_colour} был преобразован к {new_colour.darken(50)}')
    third_colour = Colour('#45A1F0')
    print(f'{third_colour} был преобразован к {third_colour.darken(20)}')


if __name__ == "__main__":
    check_on_examples()