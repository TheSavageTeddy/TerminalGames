import os, re, time

try:
    height = int(re.search("(\d+)\)", str(os.get_terminal_size())).group(1))-1 #the terminal needs -1 because uh
    width = int(re.search("(\d+),", str(os.get_terminal_size())).group(1))
except OSError:
    print("This game should be played in the terminal.")
    # exit()

#
#    ASCII
#
#    ┃
#    ━
#    ┛
#    ┗
#    ┓
#    ┏
#    ●
#
#    SNAKE EXAMPLE
#
#    ━━━━━━┓
#        ┃
#        ┃
#        ●
#


speed = 0.4

while True:
    for i in range(0, height):
        print("."*width)

    time.sleep(speed)