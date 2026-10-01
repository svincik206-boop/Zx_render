def renderText(text, x, y):
    print(f"\033[{y};{x}H{text}")
#This function renders text at x, y coordinates,

def eraseText():
    print("\033[2J")
#This function erases text!

def colorText(text2, color_code):
    print(f"\033[{color_code}m{text2}")
    print(f"\033[0m")

def colorTerminal(color_code2):
    print(f"\033[{color_code2}m")
# Attention! Use only codes from 30-37.