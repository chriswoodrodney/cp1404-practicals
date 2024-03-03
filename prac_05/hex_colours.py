"""
name: CHRISWOOD RODNEY OKWIIRI
file: hex_colours
"""

class ColorLookup:
    def __init__(self):
        self.color_codes = {
            "ALICEBLUE": "#F0F8FF",
            "ANTIQUEWHITE": "#FAEBD7",
            "AQUA": "#00FFFF",
            "AQUAMARINE": "#7FFFD4",
            "AZURE": "#F0FFFF",
            "BEIGE": "#F5F5DC",
            "BISQUE": "#FFE4C4",
            "BLACK": "#000000",
            "BLANCHEDALMOND": "#FFEBCD",
            "BLUE": "#0000FF"
        }

    def lookup_color(self, color_name):
        return self.color_codes.get(color_name.upper(), "Invalid color name")


def main():
    color_lookup = ColorLookup()
    print("Welcome to Hexadecimal Color Code Lookup!")

    while True:
        color_name = input("Enter a color name (or blank to quit): ").upper()
        if not color_name:
            break

        color_code = color_lookup.lookup_color(color_name)
        print(f"The hexadecimal code for {color_name} is {color_code}")


if __name__ == "__main__":
    main()
