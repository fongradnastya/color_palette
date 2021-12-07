from .colour import Colour


def check_on_examples():
    """
    Функция check_on_examples демонстрирует работу класса Colour
    на примерах
    """
    first_colour = Colour('#01E305')
    print(f'{first_colour} был преобразован к {first_colour.lighten(10)}')
    second_colour = Colour('#15F47A')
    print(f'{second_colour} был преобразован к {second_colour.darken(50)},'
          f'а затем обратно к {second_colour.lighten(50)}')
    black = Colour('#000000')
    print(f'{black} был преобразован к {black.lighten(100)}')
    new_colour = Colour('#99CCFF')
    print(f'{new_colour} был преобразован к {new_colour.darken(50)}')
    third_colour = Colour('#45A1F0')
    print(f'{third_colour} был преобразован к {third_colour.darken(20)}')


if __name__ == "__main__":
    check_on_examples()
