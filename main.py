class Colour:
    def __init__(self, colour_code: str):
        self.red = int(colour_code[1:3], 16)
        self.green = int(colour_code[3:5], 16)
        self.blue = int(colour_code[5:7], 16)

    def __str__(self):
        colour_code = "#{:0>2x}{:0>2x}{:0>2x}".format(
            self.red, self.green, self.blue)
        return colour_code.upper()

    def _colour_transform(self, percent: int, is_lighten: bool) -> str:
        new_red = self.red + round(self.red * percent / 100) * (-1)
        new_green = self.green + round(self.green * percent / 100)
        new_blue = self.blue + round(self.blue * percent / 100)
        colours = [new_red, new_green, new_blue]
        for i, colour in enumerate(colours):
            if colour > 255:
                colours[i] = 255
        colour_code = "#{:0>2x}{:0>2x}{:0>2x}".format(*colours)
        return colour_code

    def lighten(self, percent: int) -> str:
        r = g = b = 0
        colours = [r, g, b]
        for i, colour in enumerate(colours):
            colours[i] = self.red + round(self.red * percent / 100)
            if colour > 255:
                colours[i] = 255
        colour_code = "#{:0>2x}{:0>2x}{:0>2x}".format(*colours)
        return colour_code
