class Colour:
    def __init__(self, colour_code: str):
        self.red = int(colour_code[1:3], 16)
        self.green = int(colour_code[3:5], 16)
        self.blue = int(colour_code[5:7], 16)

    def __str__(self):
        colour_code = "#{:0>2x}{:0>2x}{:0>2x}".format(
            self.red, self.green, self.blue)
        return colour_code.upper()

    def _change_colour(self, colour: str, percent: int, is_dark: int):
        attribute = getattr(self, colour)
        attribute += round(attribute * percent / 100) * is_dark
        if attribute > 255:
            attribute = 255
        if attribute < 0:
            attribute = 0
        setattr(self, colour, attribute)

    def lighten(self, percent: int) -> str:
        self._change_colour('red', percent, 1)
        self._change_colour('green', percent, 1)
        self._change_colour('blue', percent, 1)
        return str(self)

    def darken(self, percent: int) -> str:
        colours = [self.red, self.green, self.blue]
        for i, _ in enumerate(colours):
            colours[i] -= round(colours[i] * percent / 100)
            if colours[i] < 0:
                colours[i] = 0
        return str(self)
    