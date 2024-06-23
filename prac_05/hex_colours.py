COLOR_TO_CODE = {"absolutezero": "#0048ba", "acidgreen": "#b0bf1a", "aliceblue": "#f0f8ff",
                 "alizarincrimson": "#e32636",
                 "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc", "antiquewhite": "#faebd7"
                 , "apricot": "#fbceb1", "aqua": "#00ffff"}
print(COLOR_TO_CODE)

color_code = input("Enter color name: ").lower()
while color_code != "":
    try:
        print(f"{color_code:3} is {COLOR_TO_CODE[color_code]}")
        color_code = input("Enter color name: ").lower()
    except KeyError:
        print("Invalid color code")
        color_code = input("Enter color name: ").lower()
