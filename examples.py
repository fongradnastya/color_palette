from change_color.color import Color


def check_on_examples():
    """
    Функция check_on_examples демонстрирует работу класса Colour
    на примерах
    """
    first_color = Color('#01E305')
    print(f'{first_color} был преобразован к {first_color.lighten(10)}')
    second_color = Color('#15F47A')
    print(f'{second_color} был преобразован к {second_color.darken(50)},'
          f'а затем обратно к {second_color.lighten(50)}')
    black = Color('#000000')
    print(f'{black} был преобразован к {black.lighten(100)}')
    new_color = Color('#99CCFF')
    print(f'{new_color} был преобразован к {new_color.darken(50)}')
    third_color = Color('#45A1F0')
    print(f'{third_color} был преобразован к {third_color.darken(20)}')


if __name__ == "__main__":
    check_on_examples()
