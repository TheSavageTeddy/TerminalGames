import os, re

try:
    height = re.search("(\d+)\)", str(os.get_terminal_size())).group(1)
    width = re.search("(\d+),", str(os.get_terminal_size())).group(1)
except OSError:
    print("This game should be played in the terminal.")
    # exit()

