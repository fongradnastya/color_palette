class Colour:
    def __init__(self, colour_code: str):
        self.red = int(colour_code[1:3], 16)
        self.green = int(colour_code[3:5], 16)
        self.blue = int(colour_code[5:7], 16)

    def __str__(self):
        colour_code = "#{:0>2x}{:0>2x}{:0>2x}".format(
            self.red, self.green, self.blue)
        return colour_code.upper()

    def lighten(self, percent: int):
        new_red = self.red + round(self.red * percent / 100)
        new_green = self.green + round(self.green * percent / 100)
        if new_green > 255:
            new_green = 255
        new_blue = self.blue + round(self.blue * percent / 100)
        colour_code = "#{:0>2x}{:0>2x}{:0>2x}".format(
            new_red, new_green, new_blue)
        print(colour_code)
        return Colour(colour_code)
