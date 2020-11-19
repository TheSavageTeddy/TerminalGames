import os

try:
    size = os.get_terminal_size()
except OSError:
    print("This game should be played in the terminal")
    exit()

